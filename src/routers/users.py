from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta

from .. import models, schemas, database
from ..utils.security import create_access_token, get_password_hash, verify_password

router = APIRouter()

@router.post(
    "/register",
    response_model=schemas.User,
    summary="Registrar um novo usuário"
)
def signUp(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    db_user_by_email = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user_by_email:
        raise HTTPException(status_code=400, detail="Este e-mail já está em uso.")
    
    db_user_by_cpf = db.query(models.User).filter(models.User.cpf == user.cpf).first()
    if db_user_by_cpf:
        raise HTTPException(status_code=400, detail="Este CPF já está cadastrado.")

    hashed_password = get_password_hash(user.password)
    
    db_user = models.User(
        email=user.email, 
        hashed_password=hashed_password, 
        name=user.name, 
        cpf=user.cpf,
        user_type=user.user_type
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.post(
    "/login",
    response_model=schemas.Token,
    summary="Autenticar um usuário"
)
def signIn(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(database.get_db)
):
    user = db.query(models.User).filter(models.User.email == form_data.username).first()

    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="E-mail ou senha incorretos",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=60)

    access_token = create_access_token(
        data={"sub": user.email},
        expires_delta=access_token_expires
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }