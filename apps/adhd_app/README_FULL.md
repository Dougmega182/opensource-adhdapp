# ADHD Assistant App

An AI-powered productivity assistant designed for people with ADHD, featuring a React Native mobile app with Python backend.

## Features

- **AI Task Breakdown**: Automatically break down complex tasks into manageable steps
- **Brain Dump**: Quickly capture thoughts and organize them into tasks
- **Pomodoro Timer**: Focus timer with automated breaks
- **Pattern Learning**: Learn from your productivity patterns over time
- **Mobile App**: Native iOS and Android apps built with React Native
- **REST API**: Flask-based API connecting mobile app to Python agents

## Architecture

```
apps/adhd_app/
├── src/                      # Python Backend
│   ├── main.py              # CLI entry point
│   ├── api_server.py        # Flask REST API server
│   ├── ai_assistant.py      # AI task processing
│   ├── storage.py           # SQLite database layer
│   ├── pattern_learner.py   # Pattern recognition
│   └── workspace/           # Generated files and database
├── agents/                   # AI Agents
│   ├── web_agent.py         # Task breakdown & brain dump
│   ├── devops_agent.py      # Database & Pomodoro timer
│   └── validator_agent.py   # Validation & QA
└── rn_app/                  # React Native Mobile App
    ├── src/
    │   ├── screens/         # App screens
    │   ├── components/      # Reusable UI components
    │   └── utils/           # API client & utilities
    ├── android/             # Android native code
    └── ios/                 # iOS native code
```

## Quick Start

### 1. Python Backend Setup

```bash
# Navigate to the app directory
cd apps/adhd_app

# Install Python dependencies
pip install -r requirements.txt

# Run the CLI application
python src/main.py

# OR run the API server for mobile app
python src/api_server.py
```

### 2. React Native Mobile App Setup

```bash
# Navigate to the React Native app
cd apps/adhd_app/rn_app

# Install dependencies
npm install

# For iOS (macOS only)
cd ios && pod install && cd ..
npm run ios

# For Android
npm run android
```

## Running the Full Stack

### Start the Backend API Server

**Option 1: Using Python directly**
```bash
cd apps/adhd_app/src
export PYTHONPATH="$(cd ../../.. && pwd)"  # Linux/Mac
# or for Windows PowerShell: $env:PYTHONPATH = (Get-Item ..\..\..).FullName
python api_server.py
```

**Option 2: Using the provided scripts**

Linux/Mac:
```bash
cd apps/adhd_app/src
chmod +x run_server.sh
./run_server.sh
```

Windows (PowerShell):
```powershell
cd apps/adhd_app/src
.\run_server.ps1
```

The API server will start at: `http://localhost:5000/api`

### Start the Mobile App

In a separate terminal:
```bash
cd apps/adhd_app/rn_app
npm start
```

Then run the app:
```bash
# iOS
npm run ios

# Android
npm run android
```

## API Endpoints

The Flask REST API provides the following endpoints:

### Tasks
- `GET /api/health` - Health check
- `GET /api/tasks` - Get all tasks
- `POST /api/tasks` - Create a new task
  ```json
  {
    "title": "Task title",
    "description": "Optional description",
    "status": "pending"
  }
  ```
- `GET /api/tasks/:id` - Get a specific task
- `PUT /api/tasks/:id` - Update a task
  ```json
  {
    "status": "completed"
  }
  ```
- `DELETE /api/tasks/:id` - Delete a task

### AI Features
- `POST /api/brain-dump` - Process brain dump text
  ```json
  {
    "text": "Buy groceries\nCall dentist\nFinish project"
  }
  ```
- `POST /api/ai/task-breakdown` - AI task breakdown
  ```json
  {
    "text": "Write report. Make coffee. Check emails."
  }
  ```

### Tools
- `POST /api/pomodoro/start` - Start Pomodoro timer
  ```json
  {
    "minutes": 25
  }
  ```
- `POST /api/validate` - Validate workspace
- `GET /api/stats` - Get task statistics

## Components

### Python Agents

1. **WebAgent** (`agents/web_agent.py`)
   - AI task breakdown
   - Brain dump processing
   - Creates structured tasks from free-form text

2. **DevOpsAgent** (`agents/devops_agent.py`)
   - Database setup and management
   - Pomodoro timer implementation
   - Workspace initialization

3. **ValidatorAgent** (`agents/validator_agent.py`)
   - Workspace validation
   - Data integrity checks
   - Quality assurance

### React Native Screens

1. **HomeScreen**: Main dashboard with feature cards
2. **TasksScreen**: Full task management (create, view, complete, delete)
3. **BrainDumpScreen**: Quick thought capture with AI processing
4. **PomodoroScreen**: Focus timer with break management

### React Native Components

- **TaskCard**: Reusable task display component
- **Button**: Custom styled button
- **LoadingSpinner**: Loading indicator

### Utilities

- **api.js**: Backend API client with axios
- **storage.js**: Local AsyncStorage helpers
- **notifications.js**: Push notification helpers (stub)

## Development

### Testing the Backend

```bash
# Run CLI to test agents
cd apps/adhd_app/src
export PYTHONPATH="$(cd ../../.. && pwd)"
python main.py

# Test API endpoints
curl http://localhost:5000/api/health
curl http://localhost:5000/api/tasks
curl -X POST http://localhost:5000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Test task","status":"pending"}'
```

### Testing the Mobile App

The mobile app includes mock data fallbacks for development without the backend running. See `rn_app/src/utils/api.js` for configuration.

To connect to your local backend:
1. Update `API_BASE_URL` in `rn_app/src/utils/api.js`
2. For Android emulator, use `http://10.0.2.2:5000/api`
3. For iOS simulator, use `http://localhost:5000/api`
4. For physical devices, use your computer's IP address (e.g., `http://192.168.1.100:5000/api`)

## Database

The app uses SQLite for storage:
- **Location**: `apps/adhd_app/src/workspace/adhd_assistant.db`
- **Tables**: 
  - `tasks` - User tasks with title, description, status, timestamps
  - `brain_dumps` - Brain dump history with content and timestamps

### Schema

**tasks table:**
```sql
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    status TEXT NOT NULL DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**brain_dumps table:**
```sql
CREATE TABLE brain_dumps (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

To reset the database:
```bash
rm apps/adhd_app/src/workspace/adhd_assistant.db
# Restart the API server to recreate
```

## Configuration

### Backend Configuration

Edit `src/api_server.py` to customize:
- Port (default: 5000)
- Host (default: 0.0.0.0)
- Debug mode (default: True)
- Database location
- CORS settings

### Mobile App Configuration

Edit `rn_app/src/utils/api.js` to customize:
- Backend API URL
- Request timeout (default: 10000ms)
- Headers
- Mock data fallbacks

## Deployment

### Backend Deployment

For production deployment:
1. Set `debug=False` in `api_server.py`
2. Use a production WSGI server (e.g., Gunicorn, uWSGI)
3. Set up proper environment variables
4. Use a production database (PostgreSQL, MySQL) instead of SQLite
5. Implement proper authentication and authorization

Example with Gunicorn:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 api_server:app
```

### Mobile App Deployment

**Android:**
1. Generate a release keystore
2. Configure `android/app/build.gradle`
3. Build release APK: `cd android && ./gradlew assembleRelease`
4. Upload to Google Play Store

**iOS:**
1. Configure signing in Xcode
2. Archive the app in Xcode
3. Upload to App Store Connect

## Future Features

See [roadmap.md](roadmap.md) for planned features and improvements:
- Real AI integration (OpenAI, Ollama)
- User authentication
- Cloud sync
- Advanced pattern learning
- Habit tracking
- Calendar integration
- Notifications and reminders
- Data export/import
- Dark mode
- Accessibility features

## Troubleshooting

### Backend Issues

**Import errors:**
```bash
# Make sure PYTHONPATH is set correctly
export PYTHONPATH="$(cd /path/to/workspace/root && pwd)"
```

**Database errors:**
```bash
# Delete and recreate the database
rm src/workspace/adhd_assistant.db
python src/api_server.py
```

**Port already in use:**
```bash
# Find and kill the process using port 5000
# Linux/Mac:
lsof -ti:5000 | xargs kill -9
# Windows:
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

### Mobile App Issues

**Metro bundler issues:**
```bash
npm start -- --reset-cache
```

**iOS build issues:**
```bash
cd ios
pod deintegrate
pod install
cd ..
```

**Android build issues:**
```bash
cd android
./gradlew clean
cd ..
```

**Can't connect to backend:**
- Check if API server is running (`curl http://localhost:5000/api/health`)
- Verify the API_BASE_URL in `src/utils/api.js`
- For Android emulator, use `10.0.2.2` instead of `localhost`
- For iOS simulator, use `localhost`
- For physical devices, ensure both devices are on the same network
- Check firewall settings

**React Native navigation errors:**
```bash
# Reinstall dependencies
rm -rf node_modules
npm install
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Development Guidelines

1. Follow PEP 8 for Python code
2. Use ESLint/Prettier for JavaScript code
3. Write tests for new features
4. Update documentation
5. Create meaningful commit messages

## License

MIT License - See LICENSE file for details.

## Support

For issues and questions:
- Open an issue on GitHub
- Check the [roadmap](roadmap.md) for planned features
- Review existing issues for solutions

## Acknowledgments

Built with:
- Python 3.11+
- Flask
- React Native
- SQLite
- React Navigation
