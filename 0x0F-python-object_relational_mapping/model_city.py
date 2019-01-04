#!/usr/bin/python3

from sqlalchemy import Column, Integer, String, ForeignKey 
from model_state import Base, State



class City(Base):
    """City class to represent records in cities table"""

    __tablename__ = 'cities'
    id = Column("id", Integer, primary_key=True, nullable=False)
    name = Column("name", String(128), nullable=False)
    state_id = Column("state_id", Integer, ForeignKey('states.id'), nullable=False)
