import json
import os

class DataStorage:
    def __init__(self):
        os.makedirs("data", exist_ok=True)
        self.file = "data/results.json"

    def save(self, data):
        try:
            with open(self.file, "r") as f:
                existing = json.load(f)
        except:
            existing = []

        existing.append(data)

        with open(self.file, "w") as f:
            json.dump(existing, f, indent=2, ensure_ascii=False)
