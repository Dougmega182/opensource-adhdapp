#!/usr/bin/env python3
import os
from apps.adhd_app.agents.web_agent import WebAgent
from apps.adhd_app.agents.devops_agent import DevOpsAgent

WORKSPACE_DIR = os.path.join(os.path.dirname(__file__), "workspace")

def main():
    print("=== ADHD Assistant Starting ===")

    # Initialize agents
    web_agent = WebAgent(WORKSPACE_DIR)
    devops_agent = DevOpsAgent(WORKSPACE_DIR)

    # 1. Create base app structure
    web_agent.create_app_skeleton()

    # 2. Setup database and storage
    devops_agent.setup_database()

    # 3. Demo AI task breakdown
    tasks = web_agent.ai_task_breakdown("Write report. Make coffee. Check emails.")
    print("[Main] AI generated tasks:", tasks)

    # 4. Demo brain dump
    raw_brain_dump = "Buy groceries\nCall dentist\nFinish coding project"
    processed_tasks = web_agent.brain_dump(raw_brain_dump)
    print("[Main] Processed brain dump tasks:", processed_tasks)

    # 5. Run Pomodoro timer
    devops_agent.pomodoro_timer(minutes=3)  # demo timer (3 simulated minutes)

    print("=== ADHD Assistant Setup Complete ===")
    print(f"Workspace directory: {WORKSPACE_DIR}")

if __name__ == "__main__":
    main()
