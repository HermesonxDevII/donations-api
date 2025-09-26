from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    cpf = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    user_type = Column(Integer, nullable=False) # 1 - admin, 2 - company_owner, 3 - institution_owner

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())

    company = relationship("Company", back_populates="owner", uselist=False)
    institution = relationship("Institution", back_populates="owner", uselist=False)

class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False, unique=True)
    cnpj = Column(String, unique=True, nullable=False)
    corporate_reason = Column(String, nullable=False)
    fantasy_name = Column(String, nullable=False)
    street = Column(String, nullable=True)
    neighborhood = Column(String, nullable=True)
    number = Column(String, nullable=True)
    postal_code = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    email = Column(String, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())

    owner = relationship("User", back_populates="company")
    donations_made = relationship("Donation", back_populates="donor")

class Institution(Base):
    __tablename__ = "institutions"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False, unique=True)
    cnpj = Column(String, unique=True, nullable=False)
    public_name = Column(String, nullable=False)
    street = Column(String, nullable=True)
    neighborhood = Column(String, nullable=True)
    number = Column(String, nullable=True)
    postal_code = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    email = Column(String, nullable=True)
    mission = Column(String, nullable=False)
    area_of_activity = Column(String, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())

    owner = relationship("User", back_populates="institution")
    donations_received = relationship("Donation", back_populates="receiver")

class Donation(Base):
    __tablename__ = "donations"

    id = Column(Integer, primary_key=True, index=True)
    donor_id = Column(Integer, ForeignKey("companies.id"), nullable=False)
    receiver_id = Column(Integer, ForeignKey("institutions.id"), nullable=False)
    food_name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    quantity = Column(String, nullable=False)
    expiration_date = Column(String, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())

    donor = relationship("Company", back_populates="donations_made")
    receiver = relationship("Institution", back_populates="donations_received")