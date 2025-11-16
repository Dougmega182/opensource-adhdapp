/**
 * Pomodoro Screen - Focus timer with breaks
 */

import React, { useState, useEffect, useRef } from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  Alert,
} from 'react-native';

const PomodoroScreen = () => {
  const [minutes, setMinutes] = useState(25);
  const [seconds, setSeconds] = useState(0);
  const [isActive, setIsActive] = useState(false);
  const [isBreak, setIsBreak] = useState(false);
  const [sessions, setSessions] = useState(0);
  const intervalRef = useRef(null);

  useEffect(() => {
    if (isActive) {
      intervalRef.current = setInterval(() => {
        if (seconds === 0) {
          if (minutes === 0) {
            handleTimerComplete();
          } else {
            setMinutes(minutes - 1);
            setSeconds(59);
          }
        } else {
          setSeconds(seconds - 1);
        }
      }, 1000);
    } else {
      clearInterval(intervalRef.current);
    }

    return () => clearInterval(intervalRef.current);
  }, [isActive, minutes, seconds]);

  const handleTimerComplete = () => {
    setIsActive(false);
    
    if (isBreak) {
      Alert.alert(
        'Break Complete! 🎉',
        'Ready to focus again?',
        [
          {
            text: 'Start Work Session',
            onPress: () => startWorkSession(),
          },
        ]
      );
    } else {
      setSessions(sessions + 1);
      const isLongBreak = (sessions + 1) % 4 === 0;
      const breakMinutes = isLongBreak ? 15 : 5;
      
      Alert.alert(
        'Work Session Complete! 🎉',
        `Great job! Time for a ${isLongBreak ? 'long' : 'short'} break.`,
        [
          {
            text: `Start ${breakMinutes} min Break`,
            onPress: () => startBreak(breakMinutes),
          },
          {
            text: 'Skip Break',
            onPress: () => startWorkSession(),
          },
        ]
      );
    }
  };

  const startWorkSession = () => {
    setMinutes(25);
    setSeconds(0);
    setIsBreak(false);
    setIsActive(true);
  };

  const startBreak = (breakMinutes) => {
    setMinutes(breakMinutes);
    setSeconds(0);
    setIsBreak(true);
    setIsActive(true);
  };

  const handleStartPause = () => {
    setIsActive(!isActive);
  };

  const handleReset = () => {
    Alert.alert(
      'Reset Timer',
      'Are you sure you want to reset?',
      [
        { text: 'Cancel', style: 'cancel' },
        {
          text: 'Reset',
          onPress: () => {
            setIsActive(false);
            setMinutes(25);
            setSeconds(0);
            setIsBreak(false);
          },
          style: 'destructive',
        },
      ]
    );
  };

  const formatTime = (mins, secs) => {
    return `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
  };

  return (
    <View style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.sessionCount}>
          🏆 Sessions Completed: {sessions}
        </Text>
      </View>

      <View style={styles.timerContainer}>
        <Text style={styles.timerLabel}>
          {isBreak ? '☕ Break Time' : '💪 Focus Time'}
        </Text>
        <Text style={styles.timer}>{formatTime(minutes, seconds)}</Text>
      </View>

      <View style={styles.buttonContainer}>
        <TouchableOpacity
          style={[styles.button, styles.primaryButton]}
          onPress={handleStartPause}>
          <Text style={styles.buttonText}>
            {isActive ? '⏸️ Pause' : '▶️ Start'}
          </Text>
        </TouchableOpacity>

        <TouchableOpacity
          style={[styles.button, styles.secondaryButton]}
          onPress={handleReset}>
          <Text style={styles.buttonText}>🔄 Reset</Text>
        </TouchableOpacity>
      </View>

      <View style={styles.infoContainer}>
        <Text style={styles.infoTitle}>How it works:</Text>
        <Text style={styles.infoText}>
          • Work for 25 minutes with full focus{'\n'}
          • Take a 5-minute break{'\n'}
          • After 4 sessions, take a 15-minute break{'\n'}
          • Repeat to stay productive!
        </Text>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f5f5f5',
    padding: 16,
  },
  header: {
    alignItems: 'center',
    marginBottom: 40,
  },
  sessionCount: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#6200ee',
  },
  timerContainer: {
    alignItems: 'center',
    marginBottom: 40,
  },
  timerLabel: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 16,
  },
  timer: {
    fontSize: 72,
    fontWeight: 'bold',
    color: '#6200ee',
    fontFamily: 'monospace',
  },
  buttonContainer: {
    flexDirection: 'row',
    marginBottom: 40,
  },
  button: {
    flex: 1,
    padding: 20,
    borderRadius: 12,
    alignItems: 'center',
    marginHorizontal: 4,
  },
  primaryButton: {
    backgroundColor: '#6200ee',
  },
  secondaryButton: {
    backgroundColor: '#999',
  },
  buttonText: {
    color: '#fff',
    fontSize: 18,
    fontWeight: 'bold',
  },
  infoContainer: {
    backgroundColor: '#fff',
    borderRadius: 12,
    padding: 16,
    borderWidth: 1,
    borderColor: '#ddd',
  },
  infoTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 12,
  },
  infoText: {
    fontSize: 14,
    color: '#666',
    lineHeight: 24,
  },
});

export default PomodoroScreen;
