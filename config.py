# config.py
import os

class Config:
    SECRET_KEY = 'e73b6bc3ec95cc1782205d37f03b3a299d0c6364f654dd44'
    SQLALCHEMY_DATABASE_URI = 'postgresql://istionia:R2GqZKv9xG@localhost:5432/food_allergen_watch'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    NINJAS_API_KEY = os.getenv('NINJAS_API_KEY', 'default_api_key')