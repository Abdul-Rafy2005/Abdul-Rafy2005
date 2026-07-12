import json
import os

path = "logs/stats.json"
data = {"total_entries": 0}

if os.path.exists(path):
    with open(path) as f:
        data = json.load(f)

data["total_entries"] = data.get("total_entries", 0) + 1

with open(path, "w") as f:
    json.dump(data, f, indent=2)
