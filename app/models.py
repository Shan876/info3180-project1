from . import db
from sqlalchemy import Integer, Enum
import enum


class PropertyEnum(enum.Enum):
    apartment = 'apartment'
    house = 'house'


class PropertyModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    no_bedrooms = db.Column(db.Integer)
    description = db.Column(db.String(500))
    no_bathrooms = db.Column(db.Integer)
    location = db.Column(db.String(100))
    price = db.Column(db.Numeric(10, 2))
    property_photo = db.Column(db.String(255))
    property_type = db.Column(Enum(PropertyEnum))

    def __init__(self, title, description, price, location, no_bedrooms, no_bathrooms, property_type, property_photo):
        super().__init__()

        self.title = title
        self.description = description
        self.price = price
        self.location = location
        self.no_bedrooms = no_bedrooms
        self.no_bathrooms = no_bathrooms
        self.property_type = property_type
        self.property_photo = property_photo
