# 🚀 Expo Setup Complete!

Your ADHD Assistant app is now ready to run with Expo!

## ✅ What's Been Configured

- ✅ **package.json** - Updated with Expo dependencies
- ✅ **app.json** - Expo configuration with app metadata
- ✅ **App.js** - Updated for Expo compatibility
- ✅ **babel.config.js** - Expo Babel preset
- ✅ **4 Screens** - Home, Tasks, Brain Dump, Pomodoro
- ✅ **Components** - Reusable UI components
- ✅ **API Client** - Backend connection with mock fallbacks

---

## 🎯 Quick Start (3 Steps)

### Step 1: Install Dependencies
```bash
cd apps/adhd_app/rn_app
npm install
```

### Step 2: Start Expo
```bash
npx expo start
```

### Step 3: Run on Device
Once Expo starts, you'll see options:

- **Press `a`** → Android emulator
- **Press `i`** → iOS simulator (Mac only)
- **Press `w`** → Web browser
- **Scan QR** → Physical device with Expo Go app

---

## 📱 Testing on Your Phone (Easiest!)

### 1. Install Expo Go App
- **iOS**: [App Store - Expo Go](https://apps.apple.com/app/expo-go/id982107779)
- **Android**: [Play Store - Expo Go](https://play.google.com/store/apps/details?id=host.exp.exponent)

### 2. Start Expo on Your Computer
```bash
cd apps/adhd_app/rn_app
npx expo start
```

### 3. Scan QR Code
- **iOS**: Open Camera app → Point at QR code
- **Android**: Open Expo Go app → Tap "Scan QR Code"

### 4. Connect to Backend (Optional)
To connect to the Python backend API:

1. Find your computer's IP address:
   - Windows: `ipconfig` (look for IPv4)
   - Mac/Linux: `ifconfig` (look for inet)

2. Edit `src/utils/api.js`:
   ```javascript
   const API_BASE_URL = 'http://YOUR_IP:5000/api';
   // Example: 'http://192.168.1.100:5000/api'
   ```

3. Start the backend API:
   ```bash
   cd apps/adhd_app/src
   python api_server.py
   ```

**Note**: The app works with mock data even without the backend!

---

## 🖥️ Testing on Emulator/Simulator

### Android Emulator
```bash
# Make sure Android Studio is installed with an emulator
npx expo start
# Press 'a' when Expo starts
```

### iOS Simulator (Mac only)
```bash
# Make sure Xcode is installed
npx expo start
# Press 'i' when Expo starts
```

---

## 🌐 Testing on Web
```bash
npx expo start
# Press 'w' to open in browser
```

---

## 📂 Project Structure

```
rn_app/
├── App.js                 # ✨ Main app (Expo-ready)
├── app.json              # ✨ Expo configuration
├── package.json          # ✨ Expo dependencies
├── babel.config.js       # ✨ Expo Babel preset
│
├── src/
│   ├── screens/          # 4 main screens
│   │   ├── HomeScreen.js
│   │   ├── TasksScreen.js
│   │   ├── BrainDumpScreen.js
│   │   └── PomodoroScreen.js
│   │
│   ├── components/       # Reusable UI
│   │   ├── TaskCard.js
│   │   ├── Button.js
│   │   └── LoadingSpinner.js
│   │
│   └── utils/           # Utilities
│       ├── api.js       # Backend API client
│       ├── storage.js   # Local storage
│       └── notifications.js
│
└── assets/              # Icons, images, splash
```

---

## 🔧 Troubleshooting

### "Unable to resolve module"
```bash
rm -rf node_modules
npm install
npx expo start --clear
```

### Can't see QR code
```bash
# Try tunnel mode if on different networks
npx expo start --tunnel
```

### Backend connection fails
1. Make sure API server is running
2. Use your computer's IP address (not localhost)
3. Check firewall allows port 5000
4. Ensure both devices on same WiFi

### App crashes on startup
```bash
# Clear cache and restart
npx expo start --clear
```

---

## 🎨 Customization

### Change App Colors
Edit the header color in `App.js`:
```javascript
headerStyle: {
  backgroundColor: '#6200ee', // Change this!
}
```

### Change App Name
Edit `app.json`:
```json
{
  "expo": {
    "name": "Your App Name"
  }
}
```

### Add App Icon
1. Create 1024x1024 PNG icon
2. Save as `assets/icon.png`
3. Rebuild app

---

## 📦 Building for Production

When ready to publish:

```bash
# Install EAS CLI
npm install -g eas-cli

# Configure project
eas build:configure

# Build for Android
eas build -p android

# Build for iOS
eas build -p ios
```

---

## 🚀 Next Steps

1. ✅ **Run the app** - `npx expo start`
2. ✅ **Test on your phone** - Use Expo Go
3. ⏳ **Start backend** - Connect to Python API
4. ⏳ **Customize UI** - Make it your own
5. ⏳ **Add features** - Extend functionality
6. ⏳ **Deploy** - Publish to app stores

---

## 📚 Resources

- **Expo Docs**: https://docs.expo.dev/
- **React Native**: https://reactnative.dev/
- **React Navigation**: https://reactnavigation.org/
- **Full Documentation**: See `README_EXPO.md`

---

## ✨ Ready to Go!

Your ADHD Assistant app is ready to run!

```bash
cd apps/adhd_app/rn_app
npm install
npx expo start
```

Then press **`a`** for Android or **`i`** for iOS! 🎉
