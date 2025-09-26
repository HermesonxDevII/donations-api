from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from .. import models, schemas, database
from ..utils.security import get_current_user

router = APIRouter()

@router.get("/", response_model=List[schemas.Company], summary="Listar todas as empresas")
def index(db: Session = Depends(database.get_db), skip: int = 0, limit: int = 100):
    companies = db.query(models.Company).offset(skip).limit(limit).all()
    return companies

@router.get("/{company_id}", response_model=schemas.Company, summary="Listar uma empresa específica")
def show(company_id: int, db: Session = Depends(database.get_db)):
    db_company = db.query(models.Company).filter(models.Company.id == company_id).first()
    if db_company is None:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    return db_company

@router.post("/", response_model=schemas.Company, status_code=status.HTTP_201_CREATED, summary="Criar um perfil de empresa")
def store(company: schemas.CompanyCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    if current_user.user_type != 2:
        raise HTTPException(status_code=403, detail="Apenas donos de empresa podem criar perfis de empresa.")
    if current_user.company:
        raise HTTPException(status_code=400, detail="Este usuário já possui uma empresa cadastrada.")

    db_company = models.Company(**company.dict(), owner_id=current_user.id)
    db.add(db_company)
    db.commit()

    return {
        "message": "company created has successfully!"
    }

@router.put("/{company_id}", response_model=schemas.Company, summary="Atualizar uma empresa")
def update(company_id: int, company: schemas.CompanyCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    db_company = db.query(models.Company).filter(models.Company.id == company_id).first()
    if db_company is None:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    
    if db_company.owner_id != current_user.id and current_user.user_type != 1:
        raise HTTPException(status_code=403, detail="Não autorizado a realizar esta ação")

    for key, value in company.dict().items():
        setattr(db_company, key, value)
    
    db.commit()

    return {
        "message": "company updated has successfully!"
    }

@router.delete("/{company_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Deletar uma empresa")
def destroy(company_id: int, db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    db_company = db.query(models.Company).filter(models.Company.id == company_id).first()
    if db_company is None:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
        
    if db_company.owner_id != current_user.id and current_user.user_type != 1:
        raise HTTPException(status_code=403, detail="Não autorizado a realizar esta ação")

    db.delete(db_company)
    db.commit()

    return {
        "message": "company deleted has successfully!"
    }