from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/")
def read_data():
    try:
        with open("data/results.json", "r") as f:
            return json.load(f)
    except:
        return []
