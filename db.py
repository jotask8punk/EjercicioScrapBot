from pymongo import MongoClient
from config import MONGO_USER, MONGO_PASS, MONGO_HOST


class MongoManager:
    def __init__(self):
        self.client = MongoClient(f"mongodb+srv://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}")
        self.db = self.client.get_database("EjercicioScraping")