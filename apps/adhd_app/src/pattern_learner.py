import json
from pathlib import Path
import numpy as np

class PatternLearner:
    """
    Lightweight on-device pattern recognition for ADHD task optimization.
    Uses historical completion data to suggest best times for tasks.
    """

    def __init__(self, storage_path: Path):
        self.storage_path = storage_path / "patterns.json"
        self.data = self._load_data()

    def _load_data(self):
        if self.storage_path.exists():
            try:
                return json.loads(self.storage_path.read_text(encoding="utf8"))
            except json.JSONDecodeError:
                return {}
        return {}

    def log_task_completion(self, task_name: str, hour: int):
        """
        Log when a task is completed (0-23 hour)
        """
        if task_name not in self.data:
            self.data[task_name] = []
        self.data[task_name].append(hour)
        self._save_data()

    def _save_data(self):
        self.storage_path.write_text(json.dumps(self.data, indent=2), encoding="utf8")

    def predict_best_hour(self, task_name: str):
        """
        Predict the best hour to perform the task based on past completions.
        Returns an integer (0-23).
        """
        hours = self.data.get(task_name, [])
        if not hours:
            return 9  # default to 9 AM if no data
        return int(np.round(np.mean(hours)))
