import json
import os

class DatabaseManager:
    def __init__(self,filename = "database.json"):
        self.filename = filename