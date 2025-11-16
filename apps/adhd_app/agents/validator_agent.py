from pathlib import Path

class ValidatorAgent:
    """
    ValidatorAgent - Validates workspace, folder structure, and stub AI integration
    """
    def __init__(self, workspace_path: Path):
        self.workspace = workspace_path

    def validate_workspace(self):
        """
        Checks key folders/files exist and reports summary
        """
        app_dir = self.workspace / "adhd_assistant_app"
        required_folders = ["components", "screens", "services", "assets", "styles"]
        required_files = ["App.js", "ai_agent.js"]

        missing_folders = [f for f in required_folders if not (app_dir / f).exists()]
        missing_files = [f for f in required_files if not (app_dir / f).exists()]

        if missing_folders or missing_files:
            print(f"[ValidatorAgent] Missing folders: {missing_folders}, Missing files: {missing_files}")
        else:
            print("[ValidatorAgent] Workspace validated successfully. All key folders and files are present.")
