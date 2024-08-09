# models.py
from .extensions import db

class Item(db.Model):
    """
    Item model representing an item in the system.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(200), nullable=True)


