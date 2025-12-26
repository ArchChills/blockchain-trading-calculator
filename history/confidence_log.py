import json
from datetime import datetime

FILE = "history/confidence.json"

def log_confidence(asset, confidence):
    data = []
    try:
        with open(FILE) as f:
            data = json.load(f)
    except:
        pass

    data.append({
        "asset": asset,
        "confidence": confidence,
        "time": datetime.now().isoformat()
    })

    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)
