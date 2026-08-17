# NOTE: This project currently uses the Supabase client (see database.py),
# not SQLAlchemy, so this file is not imported or used anywhere yet.
# It's kept here in case SQLAlchemy models are wanted later.
# Base is defined locally so this file works on its own instead of
# depending on a Base that doesn't exist in database.py.

from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    mobile_number = Column(String(15), unique=True, nullable=False)

    password_hash = Column(String(255), nullable=False)

    role = Column(String(20), nullable=False)

    is_active = Column(Boolean, default=True)

    created_at = Column(DateTime, default=datetime.utcnow)