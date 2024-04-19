from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)

    places = relationship("Place", secondary='place_amenity', back_populates="amenities")
