/**
 * Brain Dump Screen - Quick capture of thoughts and ideas
 */

import React, { useState } from 'react';
import {
  View,
  Text,
  StyleSheet,
  TextInput,
  TouchableOpacity,
  Alert,
} from 'react-native';
import { saveBrainDump } from '../utils/api';

const BrainDumpScreen = ({ navigation }) => {
  const [text, setText] = useState('');
  const [isProcessing, setIsProcessing] = useState(false);

  const handleSave = async () => {
    if (!text.trim()) {
      Alert.alert('Empty Brain Dump', 'Please enter some text before saving.');
      return;
    }

    setIsProcessing(true);
    try {
      const result = await saveBrainDump(text);
      Alert.alert(
        'Success!',
        `Saved ${result.tasks_saved || 0} tasks from your brain dump.`,
        [
          {
            text: 'OK',
            onPress: () => {
              setText('');
              navigation.navigate('Tasks');
            },
          },
        ]
      );
    } catch (error) {
      Alert.alert('Error', 'Failed to save brain dump. Please try again.');
      console.error('Error saving brain dump:', error);
    } finally {
      setIsProcessing(false);
    }
  };

  const handleClear = () => {
    Alert.alert(
      'Clear Brain Dump',
      'Are you sure you want to clear all text?',
      [
        { text: 'Cancel', style: 'cancel' },
        { text: 'Clear', onPress: () => setText(''), style: 'destructive' },
      ]
    );
  };

  return (
    <View style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.headerText}>🧠 Brain Dump</Text>
        <Text style={styles.subHeaderText}>
          Write down everything on your mind. We'll organize it for you!
        </Text>
      </View>

      <TextInput
        style={styles.textInput}
        multiline
        placeholder="Just start typing everything that's on your mind...&#10;&#10;- Things you need to do&#10;- Ideas you have&#10;- Worries or concerns&#10;- Anything at all!"
        value={text}
        onChangeText={setText}
        textAlignVertical="top"
      />

      <View style={styles.buttonContainer}>
        <TouchableOpacity
          style={[styles.button, styles.clearButton]}
          onPress={handleClear}
          disabled={isProcessing}>
          <Text style={styles.buttonText}>Clear</Text>
        </TouchableOpacity>

        <TouchableOpacity
          style={[styles.button, styles.saveButton]}
          onPress={handleSave}
          disabled={isProcessing}>
          <Text style={styles.buttonText}>
            {isProcessing ? 'Processing...' : 'Save & Organize'}
          </Text>
        </TouchableOpacity>
      </View>

      <View style={styles.tipContainer}>
        <Text style={styles.tipTitle}>💡 Tips:</Text>
        <Text style={styles.tipText}>
          • Don't worry about formatting{'\n'}
          • Write one idea per line for best results{'\n'}
          • Include as much or as little detail as you want{'\n'}
          • We'll automatically break it into actionable tasks
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
    marginBottom: 16,
  },
  headerText: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 8,
  },
  subHeaderText: {
    fontSize: 16,
    color: '#666',
  },
  textInput: {
    flex: 1,
    backgroundColor: '#fff',
    borderRadius: 12,
    padding: 16,
    fontSize: 16,
    borderWidth: 1,
    borderColor: '#ddd',
    marginBottom: 16,
  },
  buttonContainer: {
    flexDirection: 'row',
    marginBottom: 16,
  },
  button: {
    flex: 1,
    padding: 16,
    borderRadius: 12,
    alignItems: 'center',
    marginHorizontal: 4,
  },
  clearButton: {
    backgroundColor: '#999',
  },
  saveButton: {
    backgroundColor: '#6200ee',
  },
  buttonText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: 'bold',
  },
  tipContainer: {
    backgroundColor: '#fff',
    borderRadius: 12,
    padding: 16,
    borderWidth: 1,
    borderColor: '#ddd',
  },
  tipTitle: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 8,
  },
  tipText: {
    fontSize: 14,
    color: '#666',
    lineHeight: 20,
  },
});

export default BrainDumpScreen;
