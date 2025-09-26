from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

class DonationBase(BaseModel):
    food_name: str
    description: str
    quantity: str
    expiration_date: str

class CompanyBase(BaseModel):
    cnpj: str
    corporate_reason: str
    fantasy_name: str
    street: Optional[str] = None
    neighborhood: Optional[str] = None
    number: Optional[str] = None
    postal_code: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[EmailStr] = None

class InstitutionBase(BaseModel):
    cnpj: str
    public_name: str
    mission: str
    area_of_activity: str
    street: Optional[str] = None
    neighborhood: Optional[str] = None
    number: Optional[str] = None
    postal_code: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[EmailStr] = None

class UserBase(BaseModel):
    name: str
    cpf: str
    email: EmailStr

class DonationCreate(DonationBase):
    donor_id: int
    receiver_id: int

class CompanyCreate(CompanyBase):
    pass

class InstitutionCreate(InstitutionBase):
    pass

class UserCreate(UserBase):
    password: str
    user_type: int

class Donation(DonationBase):
    id: int
    donor_id: int
    receiver_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class Company(CompanyBase):
    id: int
    owner_id: int
    donations_made: List[Donation] = []

    class Config:
        orm_mode = True

class Institution(InstitutionBase):
    id: int
    owner_id: int
    donations_received: List[Donation] = []
    
    class Config:
        orm_mode = True

class User(UserBase):
    id: int
    user_type: int
    created_at: datetime
    updated_at: datetime
    company: Optional[Company] = None
    institution: Optional[Institution] = None

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

User.update_forward_refs()
Company.update_forward_refs()
Institution.update_forward_refs()