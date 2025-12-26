import json
from datetime import datetime

FILE_PATH = "data/history.json"

def simpan_data(data):
    try:
        with open(FILE_PATH, "r") as f:
            existing = json.load(f)
    except:
        existing = []

    data["timestamp"] = datetime.now().isoformat()
    existing.append(data)

    with open(FILE_PATH, "w") as f:
        json.dump(existing, f, indent=4)
