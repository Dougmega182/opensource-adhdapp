/**
 * ADHD Assistant - React Native App with Expo
 * Main application entry point
 */

import React from 'react';
import { StatusBar } from 'expo-status-bar';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import { GestureHandlerRootView } from 'react-native-gesture-handler';

// Import screens
import HomeScreen from './src/screens/HomeScreen';
import TasksScreen from './src/screens/TasksScreen';
import BrainDumpScreen from './src/screens/BrainDumpScreen';
import PomodoroScreen from './src/screens/PomodoroScreen';

const Stack = createStackNavigator();

export default function App() {
  return (
    <GestureHandlerRootView style={{ flex: 1 }}>
      <NavigationContainer>
        <StatusBar style="light" />
        <Stack.Navigator
          initialRouteName="Home"
          screenOptions={{
            headerStyle: {
              backgroundColor: '#6200ee',
            },
            headerTintColor: '#fff',
            headerTitleStyle: {
              fontWeight: 'bold',
            },
          }}>
          <Stack.Screen
            name="Home"
            component={HomeScreen}
            options={{ title: 'ADHD Assistant' }}
          />
          <Stack.Screen
            name="Tasks"
            component={TasksScreen}
            options={{ title: 'My Tasks' }}
          />
          <Stack.Screen
            name="BrainDump"
            component={BrainDumpScreen}
            options={{ title: 'Brain Dump' }}
          />
          <Stack.Screen
            name="Pomodoro"
            component={PomodoroScreen}
            options={{ title: 'Pomodoro Timer' }}
          />
        </Stack.Navigator>
      </NavigationContainer>
    </GestureHandlerRootView>
  );
}
