/**
 * TaskCard Component - Reusable task card
 */

import React from 'react';
import { View, Text, StyleSheet, TouchableOpacity } from 'react-native';

const TaskCard = ({ task, onPress, onLongPress }) => {
  return (
    <TouchableOpacity
      style={[
        styles.card,
        task.status === 'completed' && styles.cardCompleted,
      ]}
      onPress={onPress}
      onLongPress={onLongPress}>
      <View style={styles.header}>
        <Text
          style={[
            styles.title,
            task.status === 'completed' && styles.titleCompleted,
          ]}>
          {task.title}
        </Text>
        <Text style={styles.status}>
          {task.status === 'completed' ? '✅' : '⏳'}
        </Text>
      </View>
      {task.description && (
        <Text style={styles.description}>{task.description}</Text>
      )}
      {task.created_at && (
        <Text style={styles.date}>
          {new Date(task.created_at).toLocaleDateString()}
        </Text>
      )}
    </TouchableOpacity>
  );
};

const styles = StyleSheet.create({
  card: {
    backgroundColor: '#fff',
    borderRadius: 12,
    padding: 16,
    marginBottom: 12,
    elevation: 2,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 1 },
    shadowOpacity: 0.1,
    shadowRadius: 2,
  },
  cardCompleted: {
    opacity: 0.6,
    backgroundColor: '#e8f5e9',
  },
  header: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 8,
  },
  title: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#333',
    flex: 1,
  },
  titleCompleted: {
    textDecorationLine: 'line-through',
    color: '#666',
  },
  status: {
    fontSize: 20,
  },
  description: {
    fontSize: 14,
    color: '#666',
    marginBottom: 8,
  },
  date: {
    fontSize: 12,
    color: '#999',
  },
});

export default TaskCard;
