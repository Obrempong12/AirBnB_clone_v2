from models.base_model import BaseModel
from models import storage


class Place(BaseModel):
    """Place class"""

    def __init__(self, *args, **kwargs):
        """Initialization"""
        super().__init__(*args, **kwargs)
        self.amenity_ids = []

    @property
    def amenities(self):
        """Getter attribute that returns the list of Amenity instances."""
        amenities_list = []
        for amenity_id in self.amenity_ids:
            amenity = storage.get('Amenity', amenity_id)
            if amenity:
                amenities_list.append(amenity)
        return amenities_list

    @amenities.setter
    def amenities(self, obj):
        """Setter attribute that handles append method for adding an Amenity.id."""
        if isinstance(obj, storage.classes['Amenity']):
            if obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
