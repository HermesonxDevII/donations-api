from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import models, schemas, database
from ..utils.security import get_current_user

router = APIRouter()

@router.post("/", response_model=schemas.Donation, status_code=status.HTTP_201_CREATED, summary="Criar uma nova doação")
def store(donation: schemas.DonationCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    if current_user.user_type != 2:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="Apenas empresas podem registrar doações."
        )

    if not current_user.company:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="O usuário precisa ter um perfil de empresa para registrar uma doação."
        )

    if donation.donor_id != current_user.company.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="Não autorizado a criar uma doação em nome de outra empresa."
        )

    db_institution = db.query(models.Institution).filter(models.Institution.id == donation.receiver_id).first()
    if not db_institution:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Instituição com o ID {donation.receiver_id} não foi encontrada."
        )
    
    db_donation = models.Donation(**donation.dict())
    db.add(db_donation)
    db.commit()
    db.refresh(db_donation)
    
    return db_donation