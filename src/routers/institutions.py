from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
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
        raise HTTPException(status_code=404, detail="Instituição não encontrada")
    return db_institution

@router.post("/", response_model=schemas.Institution, status_code=status.HTTP_201_CREATED, summary="Criar um perfil de instituição")
def store(institution: schemas.InstitutionCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    if current_user.user_type != 3:
        raise HTTPException(status_code=403, detail="Apenas donos de instituição podem criar perfis de instituição.")
    if current_user.institution:
        raise HTTPException(status_code=400, detail="Este usuário já possui uma instituição cadastrada.")

    db_institution = models.Institution(**institution.dict(), owner_id=current_user.id)
    db.add(db_institution)
    db.commit()
    db.refresh(db_institution)
    return db_institution

@router.put("/{institution_id}", response_model=schemas.Institution, summary="Atualizar uma instituição")
def update(institution_id: int, institution: schemas.InstitutionCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    db_institution = db.query(models.Institution).filter(models.Institution.id == institution_id).first()
    if db_institution is None:
        raise HTTPException(status_code=404, detail="Instituição não encontrada")
    
    if db_institution.owner_id != current_user.id and current_user.user_type != 1:
        raise HTTPException(status_code=403, detail="Não autorizado a realizar esta ação")

    for key, value in institution.dict().items():
        setattr(db_institution, key, value)
    
    db.commit()
    db.refresh(db_institution)
    return db_institution

@router.delete("/{institution_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Deletar uma instituição")
def destroy(institution_id: int, db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    db_institution = db.query(models.Institution).filter(models.Institution.id == institution_id).first()
    if db_institution is None:
        raise HTTPException(status_code=404, detail="Instituição não encontrada")
        
    if db_institution.owner_id != current_user.id and current_user.user_type != 1:
        raise HTTPException(status_code=403, detail="Não autorizado a realizar esta ação")

    db.delete(db_institution)
    db.commit()
    return None