import sqlite3
import os
from datetime import datetime

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
                status TEXT NOT NULL,
                description TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        c.execute("""
            CREATE TABLE IF NOT EXISTS brain_dumps (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
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


class TaskStorage:
    """Extended storage class with full CRUD operations for tasks"""
    
    def __init__(self, db_path):
        self.db_path = db_path
        self._initialize_db()
    
    def _initialize_db(self):
        """Initialize database with proper schema"""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                status TEXT NOT NULL DEFAULT 'pending',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        c.execute("""
            CREATE TABLE IF NOT EXISTS brain_dumps (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
        conn.close()
    
    def add_task(self, title, description='', status='pending'):
        """Add a new task"""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute(
            "INSERT INTO tasks (title, description, status) VALUES (?, ?, ?)",
            (title, description, status)
        )
        task_id = c.lastrowid
        conn.commit()
        conn.close()
        return task_id
    
    def get_task(self, task_id):
        """Get a single task by ID"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
        row = c.fetchone()
        conn.close()
        
        if row:
            return dict(row)
        return None
    
    def get_all_tasks(self):
        """Get all tasks"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute("SELECT * FROM tasks ORDER BY created_at DESC")
        rows = c.fetchall()
        conn.close()
        
        return [dict(row) for row in rows]
    
    def update_task_status(self, task_id, status):
        """Update task status"""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute(
            "UPDATE tasks SET status = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?",
            (status, task_id)
        )
        conn.commit()
        conn.close()
    
    def update_task(self, task_id, title=None, description=None, status=None):
        """Update task fields"""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        
        updates = []
        params = []
        
        if title is not None:
            updates.append("title = ?")
            params.append(title)
        if description is not None:
            updates.append("description = ?")
            params.append(description)
        if status is not None:
            updates.append("status = ?")
            params.append(status)
        
        if updates:
            updates.append("updated_at = CURRENT_TIMESTAMP")
            params.append(task_id)
            query = f"UPDATE tasks SET {', '.join(updates)} WHERE id = ?"
            c.execute(query, params)
        
        conn.commit()
        conn.close()
    
    def delete_task(self, task_id):
        """Delete a task"""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
        conn.close()
    
    def add_brain_dump(self, content):
        """Save brain dump content"""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute("INSERT INTO brain_dumps (content) VALUES (?)", (content,))
        dump_id = c.lastrowid
        conn.commit()
        conn.close()
        return dump_id
    
    def get_all_brain_dumps(self):
        """Get all brain dumps"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute("SELECT * FROM brain_dumps ORDER BY created_at DESC")
        rows = c.fetchall()
        conn.close()
        
        return [dict(row) for row in rows]
