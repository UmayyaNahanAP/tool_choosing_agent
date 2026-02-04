import json
import os
from datetime import datetime

class DecisionLogger:
    def __init__(self, log_dir="logs"):
        os.makedirs(log_dir, exist_ok=True)
        self.log_file = os.path.join(log_dir, "decision_log.json")

    def log(self, data):
        data["timestamp"] = datetime.now().isoformat()
        with open(self.log_file, "a") as f:
            f.write(json.dumps(data, indent=2))
            f.write("\n")
