from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import List

from .. import models, schemas, database
from ..utils.security import get_current_user

router = APIRouter()

@router.get("/", response_model=List[schemas.Institution], summary="Listar todas as instituições")
def index(db: Session = Depends(database.get_db), skip: int = 0, limit: int = 100):
    institutions = db.query(models.Institution).offset(skip).limit(limit).all()
    return institutions

@router.get("/{institution_id}", response_model=schemas.Institution, summary="Listar uma instituição específica")
def show(institution_id: int, db: Session = Depends(database.get_db)):
    db_institution = db.query(models.Institution).filter(models.Institution.id == institution_id).first()
    if db_institution is None:
        raise HTTPException(status_code=404, detail="Institution not found.")
    return db_institution

@router.post("/", status_code=status.HTTP_201_CREATED, summary="Criar um perfil de instituição")
def store(institution: schemas.InstitutionCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    if current_user.user_type != 3:
        raise HTTPException(status_code=403, detail="Only institution owners can create institution profiles.")

    db_institution = models.Institution(**institution.dict(), owner_id=current_user.id)
    db.add(db_institution)
    
    try:
        db.commit()
        db.refresh(db_institution)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="There is already a institution registered with this CNPJ."
        )

    return {
        "message": "institution created has successfully!"
    }

@router.put("/{institution_id}", summary="Atualizar uma instituição")
def update(institution_id: int, institution: schemas.InstitutionCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    db_institution = db.query(models.Institution).filter(models.Institution.id == institution_id).first()
    if db_institution is None:
        raise HTTPException(status_code=404, detail="Institution not found.")
    
    if db_institution.owner_id != current_user.id and current_user.user_type != 1:
        raise HTTPException(status_code=403, detail="Not authorized to perform this action.")

    for key, value in institution.dict().items():
        setattr(db_institution, key, value)
    
    try:
        db.commit()
        db.refresh(db_institution)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The CNPJ provided is already in use by another institution."
        )

    return {
        "message": "institution updated has successfully!"
    }

@router.delete("/{institution_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Deletar uma instituição")
def destroy(institution_id: int, db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    db_institution = db.query(models.Institution).filter(models.Institution.id == institution_id).first()
    if db_institution is None:
        raise HTTPException(status_code=404, detail="Institution not found.")
        
    if db_institution.owner_id != current_user.id and current_user.user_type != 1:
        raise HTTPException(status_code=403, detail="Not authorized to perform this action.")

    db.delete(db_institution)
    db.commit()
    
    return {
        "message": "company deleted has successfully!"
    }