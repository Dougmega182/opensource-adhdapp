import json
from pathlib import Path

class ADHDAIAssistant:
    def __init__(self, workspace: Path):
        self.workspace = workspace

    def break_down_task(self, task: str):
        """
        Simulate breaking a task into 3 micro-steps.
        """
        steps = [
            f"Step 1: {task} - prep (5 min)",
            f"Step 2: {task} - execute (10 min)",
            f"Step 3: {task} - review (5 min)"
        ]
        output_file = self.workspace / f"{task.replace(' ', '_')}_steps.json"
        output_file.write_text(json.dumps(steps, indent=2), encoding="utf8")
        return steps

    def suggest_next_action(self, context: dict):
        """
        Simulate context-aware suggestion.
        """
        return f"Do '{context.get('next_task', 'organize desk')}' next for optimal focus"
