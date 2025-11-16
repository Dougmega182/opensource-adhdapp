# 🚀 ADHD Assistant - Quick Start Guide

Get your ADHD Assistant app running in **3 minutes**!

---

## 🎯 Option 1: Mobile App Only (Fastest!)

Run the React Native app with mock data (no backend needed):

```bash
cd apps/adhd_app/rn_app
npm install
npx expo start
```

Then:
- **Press `a`** for Android
- **Press `i`** for iOS (Mac only)
- **Scan QR code** with Expo Go app on your phone

✅ **Done!** The app works with mock data for testing UI.

---

## 🎯 Option 2: Full Stack (Backend + Mobile)

Run both Python backend and React Native app:

### Terminal 1: Start Backend API

```bash
cd apps/adhd_app/src

# Windows PowerShell
$env:PYTHONPATH = (Get-Item ..\..\..).FullName
python api_server.py

# Mac/Linux
export PYTHONPATH="$(cd ../../.. && pwd)"
python api_server.py
```

### Terminal 2: Start Mobile App

```bash
cd apps/adhd_app/rn_app
npm install
npx expo start
```

### Configure API Connection

Edit `rn_app/src/utils/api.js`:

```javascript
// For physical device, use your computer's IP
const API_BASE_URL = 'http://YOUR_IP_ADDRESS:5000/api';

// For iOS simulator
const API_BASE_URL = 'http://localhost:5000/api';

// For Android emulator
const API_BASE_URL = 'http://10.0.2.2:5000/api';
```

To find your IP:
- **Windows**: Run `ipconfig` in Command Prompt
- **Mac/Linux**: Run `ifconfig` or `ip addr`

✅ **Done!** Full-stack app running with real backend.

---

## 🎯 Option 3: CLI Only (Python Backend)

Test the Python agents without mobile app:

```bash
cd apps/adhd_app/src
export PYTHONPATH="$(cd ../../.. && pwd)"
python main.py
```

✅ **Done!** CLI version runs the agents directly.

---

## 📱 Testing on Your Phone

### 1. Install Expo Go
- **iOS**: [Download from App Store](https://apps.apple.com/app/expo-go/id982107779)
- **Android**: [Download from Play Store](https://play.google.com/store/apps/details?id=host.exp.exponent)

### 2. Start Expo
```bash
cd apps/adhd_app/rn_app
npx expo start
```

### 3. Scan QR Code
- **iOS**: Use Camera app
- **Android**: Use Expo Go app

✅ **Done!** App loads on your phone.

---

## 🔧 Prerequisites

### For Backend (Python)
- Python 3.11+
- pip (comes with Python)

Install dependencies:
```bash
cd apps/adhd_app
pip install -r requirements.txt
```

### For Mobile App (React Native)
- Node.js 16+
- npm (comes with Node.js)

Install dependencies:
```bash
cd apps/adhd_app/rn_app
npm install
```

---

## 📊 What You Get

### Features Available:
- ✅ **Task Management** - Create, view, complete tasks
- ✅ **Brain Dump** - Quick thought capture with AI processing
- ✅ **Pomodoro Timer** - Focus timer with breaks
- ✅ **AI Task Breakdown** - Break complex tasks into steps
- ✅ **Pattern Learning** - Learn from productivity patterns

### Tech Stack:
- **Backend**: Python 3.11 + Flask + SQLite
- **Mobile**: React Native + Expo
- **Platform**: iOS, Android, Web

---

## 🎨 What's Included

```
apps/adhd_app/
├── src/                    # Python Backend
│   ├── api_server.py      # REST API (Flask)
│   ├── main.py            # CLI interface
│   └── agents/            # AI agents
│
└── rn_app/                # React Native App
    ├── App.js             # Main app
    ├── src/
    │   ├── screens/       # 4 screens
    │   ├── components/    # UI components
    │   └── utils/         # API client
    └── package.json       # Expo config
```

---

## 🆘 Troubleshooting

### "Module not found" error
```bash
# Backend
pip install -r requirements.txt

# Mobile
cd rn_app
rm -rf node_modules
npm install
```

### Can't connect to backend from phone
1. Make sure backend is running
2. Use your computer's IP (not localhost)
3. Both devices must be on same WiFi
4. Check firewall allows port 5000

### Expo won't start
```bash
cd rn_app
npx expo start --clear
```

### Port 5000 already in use
```bash
# Find and kill process on Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# On Mac/Linux
lsof -ti:5000 | xargs kill -9
```

---

## 📚 Documentation

- **EXPO_SETUP.md** - Detailed Expo setup guide
- **README_EXPO.md** - React Native app documentation
- **README_FULL.md** - Complete full-stack documentation
- **SETUP_COMPLETE.md** - Architecture overview

---

## ✨ You're Ready!

Choose your option and start building:

1. **Quick UI Test** → Option 1 (Mobile only)
2. **Full Development** → Option 2 (Full stack)
3. **Backend Testing** → Option 3 (CLI only)

**Most Popular**: Start with **Option 1** to see the UI, then move to **Option 2** for full functionality!

```bash
cd apps/adhd_app/rn_app
npm install
npx expo start
```

Press **`a`** for Android or **`i`** for iOS! 🎉

---

Need help? Check the detailed guides in the documentation files above! 📖
