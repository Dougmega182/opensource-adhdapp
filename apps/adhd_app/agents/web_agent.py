import os
import json
from apps.adhd_app.src.storage import Storage

class WebAgent:
    def __init__(self, workspace_dir):
        self.workspace_dir = workspace_dir
        self.storage = Storage(workspace_dir)

    def create_app_skeleton(self):
        """Create minimal React Native folder structure and placeholder files."""
        app_dir = os.path.join(self.workspace_dir, "adhd_assistant_app")
        os.makedirs(app_dir, exist_ok=True)
        for folder in ["components", "screens", "services", "assets", "styles"]:
            os.makedirs(os.path.join(app_dir, folder), exist_ok=True)

        # Minimal app.js
        app_js_path = os.path.join(app_dir, "App.js")
        if not os.path.exists(app_js_path):
            with open(app_js_path, "w", encoding="utf8") as f:
                f.write("// ADHD Assistant main app entry (stub)\n")

        # AI agent placeholder
        ai_agent_path = os.path.join(app_dir, "ai_agent.js")
        if not os.path.exists(ai_agent_path):
            with open(ai_agent_path, "w", encoding="utf8") as f:
                f.write("// Ollama AI integration stub\n")

        print(f"[WebAgent] App skeleton created at {app_dir}")

    def ai_task_breakdown(self, task_description):
        """Stub AI: break down a task into sub-tasks."""
        print(f"[WebAgent] AI Task Breakdown for: {task_description}")
        # Simple stub splitting by sentence
        subtasks = [s.strip() for s in task_description.split(".") if s]
        return subtasks

    def brain_dump(self, raw_input):
        """Stub AI: convert raw brain dump into structured notes/tasks."""
        print(f"[WebAgent] Brain dump processing...")
        # Split by lines as dummy tasks
        entries = [line.strip() for line in raw_input.split("\n") if line.strip()]
        tasks = [{"task": e, "status": "pending"} for e in entries]
        # Save to SQLite via storage
        self.storage.save_tasks(tasks)
        return tasks
