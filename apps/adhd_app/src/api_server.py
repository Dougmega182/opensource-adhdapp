#!/usr/bin/env python3
"""
Flask REST API Server for ADHD Assistant
Bridges React Native app with Python backend agents
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from pathlib import Path
import sys

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from apps.adhd_app.agents.web_agent import WebAgent
from apps.adhd_app.agents.devops_agent import DevOpsAgent
from apps.adhd_app.agents.validator_agent import ValidatorAgent
from apps.adhd_app.src.storage import TaskStorage

app = Flask(__name__)
CORS(app)  # Enable CORS for React Native requests

# Initialize workspace and agents
workspace_dir = Path(__file__).parent / "workspace"
workspace_dir.mkdir(exist_ok=True, parents=True)

web_agent = WebAgent(workspace_dir=workspace_dir)
devops_agent = DevOpsAgent(workspace_dir=workspace_dir)
validator_agent = ValidatorAgent(workspace_dir=workspace_dir)
storage = TaskStorage(db_path=workspace_dir / "adhd_assistant.db")

# Initialize database
devops_agent.setup_database()


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'ADHD Assistant API',
        'version': '1.0.0'
    })


@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    """Get all tasks"""
    try:
        tasks = storage.get_all_tasks()
        return jsonify({
            'success': True,
            'tasks': tasks
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/tasks', methods=['POST'])
def create_task():
    """Create a new task"""
    try:
        data = request.get_json()
        title = data.get('title')
        description = data.get('description', '')
        status = data.get('status', 'pending')
        
        if not title:
            return jsonify({
                'success': False,
                'error': 'Title is required'
            }), 400
        
        task_id = storage.add_task(title, description, status)
        
        return jsonify({
            'success': True,
            'task_id': task_id,
            'message': 'Task created successfully'
        }), 201
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    """Get a specific task"""
    try:
        task = storage.get_task(task_id)
        if task:
            return jsonify({
                'success': True,
                'task': task
            })
        else:
            return jsonify({
                'success': False,
                'error': 'Task not found'
            }), 404
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """Update a task"""
    try:
        data = request.get_json()
        status = data.get('status')
        
        if not status:
            return jsonify({
                'success': False,
                'error': 'Status is required'
            }), 400
        
        storage.update_task_status(task_id, status)
        
        return jsonify({
            'success': True,
            'message': 'Task updated successfully'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Delete a task"""
    try:
        storage.delete_task(task_id)
        return jsonify({
            'success': True,
            'message': 'Task deleted successfully'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/brain-dump', methods=['POST'])
def brain_dump():
    """Process brain dump text and save tasks"""
    try:
        data = request.get_json()
        text = data.get('text', '')
        
        if not text:
            return jsonify({
                'success': False,
                'error': 'Text is required'
            }), 400
        
        result = web_agent.brain_dump(text)
        
        return jsonify({
            'success': True,
            'tasks_saved': result.get('tasks_saved', 0),
            'message': f"Saved {result.get('tasks_saved', 0)} tasks from your brain dump"
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/ai/task-breakdown', methods=['POST'])
def ai_task_breakdown():
    """Break down a task using AI"""
    try:
        data = request.get_json()
        text = data.get('text', '')
        
        if not text:
            return jsonify({
                'success': False,
                'error': 'Text is required'
            }), 400
        
        tasks = web_agent.ai_task_breakdown(text)
        
        return jsonify({
            'success': True,
            'tasks': tasks
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/pomodoro/start', methods=['POST'])
def start_pomodoro():
    """Start a Pomodoro timer session"""
    try:
        data = request.get_json()
        minutes = data.get('minutes', 25)
        
        # Note: This is a synchronous call - in production, you'd want to use
        # async/background tasks or WebSockets for real-time updates
        result = devops_agent.pomodoro_timer(minutes=minutes)
        
        return jsonify({
            'success': True,
            'message': 'Pomodoro session completed',
            'duration': minutes
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/validate', methods=['POST'])
def validate_workspace():
    """Validate the workspace structure"""
    try:
        result = validator_agent.validate()
        
        return jsonify({
            'success': True,
            'validation': result
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get task statistics"""
    try:
        all_tasks = storage.get_all_tasks()
        
        total = len(all_tasks)
        completed = sum(1 for task in all_tasks if task.get('status') == 'completed')
        pending = sum(1 for task in all_tasks if task.get('status') == 'pending')
        
        return jsonify({
            'success': True,
            'stats': {
                'total_tasks': total,
                'completed_tasks': completed,
                'pending_tasks': pending,
                'completion_rate': round((completed / total * 100) if total > 0 else 0, 2)
            }
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


if __name__ == '__main__':
    print("🚀 Starting ADHD Assistant API Server...")
    print("📱 React Native app can connect to: http://localhost:5000/api")
    print("💡 Health check: http://localhost:5000/api/health")
    app.run(host='0.0.0.0', port=5000, debug=True)
