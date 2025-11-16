/**
 * Storage Utility - Local storage helpers
 */

import AsyncStorage from '@react-native-async-storage/async-storage';

/**
 * Save data to local storage
 */
export const saveData = async (key, value) => {
  try {
    const jsonValue = JSON.stringify(value);
    await AsyncStorage.setItem(key, jsonValue);
  } catch (error) {
    console.error('Error saving data:', error);
    throw error;
  }
};

/**
 * Get data from local storage
 */
export const getData = async (key) => {
  try {
    const jsonValue = await AsyncStorage.getItem(key);
    return jsonValue != null ? JSON.parse(jsonValue) : null;
  } catch (error) {
    console.error('Error getting data:', error);
    throw error;
  }
};

/**
 * Remove data from local storage
 */
export const removeData = async (key) => {
  try {
    await AsyncStorage.removeItem(key);
  } catch (error) {
    console.error('Error removing data:', error);
    throw error;
  }
};

/**
 * Clear all local storage
 */
export const clearAll = async () => {
  try {
    await AsyncStorage.clear();
  } catch (error) {
    console.error('Error clearing storage:', error);
    throw error;
  }
};

// Storage keys
export const STORAGE_KEYS = {
  USER_SETTINGS: 'user_settings',
  TASKS_CACHE: 'tasks_cache',
  POMODORO_SESSIONS: 'pomodoro_sessions',
};
