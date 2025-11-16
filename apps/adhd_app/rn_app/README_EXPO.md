# ADHD Assistant - Expo React Native App

Quick start guide for running the ADHD Assistant mobile app with Expo.

## Prerequisites

- Node.js 16+ installed
- Expo CLI (will be installed with `npm install`)
- For testing:
  - **Android**: Android Studio with emulator OR physical Android device
  - **iOS**: Xcode with simulator (Mac only) OR physical iOS device
  - **Both**: Expo Go app on your phone

## Quick Start

### 1. Install Dependencies

```bash
cd apps/adhd_app/rn_app
npm install
```

### 2. Start Expo

```bash
npx expo start
```

or simply:

```bash
npm start
```

### 3. Run on Device

After starting Expo, you'll see a QR code and options:

- **Press `a`** - Run on Android emulator
- **Press `i`** - Run on iOS simulator (Mac only)
- **Press `w`** - Run in web browser
- **Scan QR code** - Run on your physical phone using Expo Go app

## Running on Physical Device

### Option 1: Expo Go App (Easiest)

1. Install **Expo Go** app from App Store (iOS) or Play Store (Android)
2. Run `npx expo start` on your computer
3. Scan the QR code with:
   - **iOS**: Camera app
   - **Android**: Expo Go app
4. App will load on your device

### Option 2: Development Build

For advanced features, build a development client:

```bash
npx expo run:android
# or
npx expo run:ios
```

## Backend Connection

The app connects to the Python backend API at `http://localhost:5000/api` by default.

### For Physical Devices

Edit `src/utils/api.js` and change the API URL to your computer's IP:

```javascript
const API_BASE_URL = 'http://YOUR_COMPUTER_IP:5000/api';
// Example: 'http://192.168.1.100:5000/api'
```

To find your computer's IP:
- **Windows**: `ipconfig` (look for IPv4 Address)
- **Mac/Linux**: `ifconfig` or `ip addr` (look for inet)

Make sure both devices are on the same WiFi network!

## Features

- ✅ **Cross-platform**: Runs on iOS, Android, and Web
- ✅ **Hot Reload**: Changes appear instantly
- ✅ **Easy Testing**: Use Expo Go app without building
- ✅ **Mock Data**: Works without backend for UI testing

## Project Structure

```
rn_app/
├── App.js              # Main app entry
├── app.json            # Expo configuration
├── package.json        # Dependencies
├── assets/             # Images, icons, splash
└── src/
    ├── screens/        # App screens
    ├── components/     # Reusable UI
    └── utils/          # API client, storage
```

## Available Scripts

- `npm start` - Start Expo development server
- `npm run android` - Run on Android
- `npm run ios` - Run on iOS
- `npm run web` - Run in web browser

## Troubleshooting

### "Unable to resolve module"
```bash
rm -rf node_modules
npm install
npx expo start --clear
```

### Can't connect to backend
1. Make sure backend is running: `python src/api_server.py`
2. Check the API URL in `src/utils/api.js`
3. For physical devices, use your computer's IP address
4. Ensure firewall allows port 5000

### Android emulator not starting
```bash
# List available emulators
emulator -list-avds

# Start specific emulator
emulator -avd <device_name>
```

### iOS simulator not found (Mac)
```bash
# List available simulators
xcrun simctl list devices

# Open simulator
open -a Simulator
```

## Building for Production

### Android APK
```bash
eas build -p android --profile preview
```

### iOS IPA
```bash
eas build -p ios --profile preview
```

### App Stores
```bash
# Android (Google Play)
eas build -p android --profile production
eas submit -p android

# iOS (App Store)
eas build -p ios --profile production
eas submit -p ios
```

Note: Requires Expo EAS account (free tier available)

## Tips

1. **Use Expo Go** for quick testing - no build required
2. **Enable Fast Refresh** - Changes apply without full reload
3. **Use React DevTools** - Press `m` in terminal to open menu
4. **Check logs** - Press `Shift+m` to open Chrome DevTools
5. **Mock API data** - The app works offline with fallback data

## Documentation

- Main README: `../README_FULL.md`
- Expo Docs: https://docs.expo.dev/
- React Native: https://reactnative.dev/
- React Navigation: https://reactnavigation.org/

## Support

For issues:
1. Check this README
2. Review `../README_FULL.md`
3. Check Expo documentation
4. Open an issue on GitHub

Happy coding! 🚀
