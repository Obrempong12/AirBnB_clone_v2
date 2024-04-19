import os
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class Place(BaseModel, Base):
    __tablename__ = 'places'

    # Your existing columns and relationships go here...

    amenities = relationship("Amenity", secondary='place_amenity', back_populates="places", viewonly=False)

    if os.getenv('HBNB_TYPE_STORAGE') != 'file':
        @property
        def amenities(self):
            """Getter attribute that returns the list of Amenity instances."""
            return self.amenities

        @amenities.setter
        def amenities(self, obj):
            """Setter attribute that handles appending Amenity instances."""
            if isinstance(obj, Amenity):
                if obj not in self.amenities:
                    self.amenities.append(obj)
