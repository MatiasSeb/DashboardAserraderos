from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from config.database import engine_users

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    hashed_password = Column(String(128))
    role_id = Column(Integer, ForeignKey('roles.id'), nullable=False)
    
    role = relationship("Role", back_populates="users")

class Role(Base):
    __tablename__ = 'roles'
    
    id = Column(Integer, primary_key=True, index=True)
    role_name = Column(String(15), unique=True, nullable=False)
    
    users = relationship("User", back_populates="role")

Base.metadata.create_all(engine_users)