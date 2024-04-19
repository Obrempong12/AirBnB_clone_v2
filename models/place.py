import os
from sqlalchemy import Column, String, Table, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class Place(BaseModel, Base):
    __tablename__ = 'places'

    # Your existing columns and relationships go here...

    # Define association table for the Many-To-Many relationship
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60), ForeignKey('places.id'), primary_key=True),
                          Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True),
                          UniqueConstraint('place_id', 'amenity_id')
                          )

    amenities = relationship("Amenity", secondary=place_amenity, back_populates="places")

    if os.getenv('HBNB_TYPE_STORAGE') == 'file':
        @property
        def amenities(self):
            """Getter attribute that returns the list of Amenity instances."""
            from models import storage
            amenities_list = []
            for amenity_id in self.amenity_ids:
                amenity = storage.get('Amenity', amenity_id)
                if amenity:
                    amenities_list.append(amenity)
            return amenities_list

        @amenities.setter
        def amenities(self, obj):
            """Setter attribute that handles append method for adding an Amenity.id."""
            if isinstance(obj, Amenity):
                if obj.id not in self.amenity_ids:
                    self.amenity_ids.append(obj.id)
