#!/usr/bin/python3
"""
Module class definition state and
instance declarative_base
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    """
    State class id and name attribute
    """
    __tablename__ = 'states'
    id = Column(Integer,
                primary_key=True,
                autoincrement=True,
                unique=True,
                nullable=False)

    name = Column(String(128),
                  nullable=False)

    cities = relationship("City",
                          backref="state",
                          cascade="all, delete-orphan")
