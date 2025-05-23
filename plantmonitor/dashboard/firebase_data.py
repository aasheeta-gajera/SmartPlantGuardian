# dashboard/firebase_data.py
from .firebase_config import db

def get_plant_data():
    ref = db.reference('smartPlantMonitor/')
    return ref.get()
