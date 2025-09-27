from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import models, schemas, database
from ..utils.security import get_current_user

router = APIRouter()

@router.post("/", status_code=status.HTTP_200_OK, summary="Criar uma nova doação")
def store(
    donation: schemas.DonationCreate, 
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(get_current_user)
):
    if current_user.user_type != 2:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="Only companies can register donations."
        )

    if not current_user.companies:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="The user must have a business profile to register a donation."
        )

    company_ids = [c.id for c in current_user.companies]
    if donation.donor_id not in company_ids:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="Not authorized to create a donation on behalf of a company that does not belong to you."
        )

    db_institution = db.query(models.Institution).filter(models.Institution.id == donation.receiver_id).first()
    if not db_institution:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Institution with ID {donation.receiver_id} not found."
        )
    
    db_donation = models.Donation(**donation.dict())
    db.add(db_donation)
    db.commit()
    
    return {
        "message": "donation created has successfully!"
    }