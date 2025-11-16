import sqlite3
import os

class Storage:
    def __init__(self, workspace_dir):
        self.workspace_dir = workspace_dir
        self.db_path = os.path.join(workspace_dir, "adhd_assistant.db")

    def initialize_db(self, db_path=None):
        self.db_path = db_path or self.db_path
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task TEXT NOT NULL,
                status TEXT NOT NULL
            )
        """)
        c.execute("""
            CREATE TABLE IF NOT EXISTS brain_dumps (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()

    def save_tasks(self, tasks):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        for t in tasks:
            c.execute("INSERT INTO tasks (task, status) VALUES (?, ?)", (t["task"], t["status"]))
        conn.commit()
        conn.close()
