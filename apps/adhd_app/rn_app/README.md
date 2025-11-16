# ADHD Assistant - React Native Mobile App

A React Native mobile application for the ADHD Assistant, providing task management, brain dump, and Pomodoro timer features.

## Features

- **Task Management**: Create, view, and complete tasks
- **Brain Dump**: Quick capture of thoughts and ideas with AI processing
- **Pomodoro Timer**: Focus timer with automated breaks
- **AI Task Breakdown**: Automatically break down complex tasks
- **Pattern Learning**: Learn from your productivity patterns

## Prerequisites

- Node.js >= 16
- React Native development environment set up
- For iOS: Xcode, CocoaPods
- For Android: Android Studio, JDK

## Installation

```bash
# Install dependencies
npm install

# iOS only - Install pods
cd ios && pod install && cd ..
```

## Running the App

### Android
```bash
npm run android
```

### iOS
```bash
npm run ios
```

### Start Metro Bundler
```bash
npm start
```

## Backend Setup

The app requires the Python backend to be running. By default, it connects to `http://localhost:5000/api`.

To change the backend URL, edit `src/utils/api.js`:

```javascript
const API_BASE_URL = 'http://your-backend-url:5000/api';
```

## Project Structure

```
rn_app/
├── src/
│   ├── screens/          # Main app screens
│   │   ├── HomeScreen.js
│   │   ├── TasksScreen.js
│   │   ├── BrainDumpScreen.js
│   │   └── PomodoroScreen.js
│   ├── components/       # Reusable components
│   │   ├── TaskCard.js
│   │   ├── Button.js
│   │   └── LoadingSpinner.js
│   └── utils/           # Utilities
│       ├── api.js       # Backend API calls
│       ├── storage.js   # Local storage
│       └── notifications.js
├── android/             # Android native code
├── ios/                # iOS native code
└── App.js              # Main app component
```

## Development Mode

The app includes mock data for development when the backend is not available. See `src/utils/api.js` for fallback responses.

## Building for Production

### Android
```bash
cd android
./gradlew assembleRelease
```

### iOS
```bash
# Open Xcode
open ios/ADHDAssistant.xcworkspace
# Then build from Xcode
```

## Troubleshooting

### Metro Bundler Issues
```bash
npm start -- --reset-cache
```

### iOS Build Issues
```bash
cd ios
pod deintegrate
pod install
```

### Android Build Issues
```bash
cd android
./gradlew clean
```

## Contributing

Please read the main project README for contribution guidelines.

## License

See the main project LICENSE file.
