/**
 * API Utility - Handles communication with Python backend
 */

import axios from 'axios';

// Configure your backend URL here
const API_BASE_URL = 'http://localhost:5000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
});

/**
 * Fetch all tasks
 */
export const fetchTasks = async () => {
  try {
    const response = await api.get('/tasks');
    return response.data.tasks || [];
  } catch (error) {
    console.error('Error fetching tasks:', error);
    // Return mock data for development
    return [
      {
        id: 1,
        title: 'Sample Task 1',
        description: 'This is a sample task',
        status: 'pending',
        created_at: new Date().toISOString(),
      },
      {
        id: 2,
        title: 'Sample Task 2',
        description: 'Another sample task',
        status: 'completed',
        created_at: new Date().toISOString(),
      },
    ];
  }
};

/**
 * Create a new task
 */
export const createTask = async (title, description = '') => {
  try {
    const response = await api.post('/tasks', {
      title,
      description,
      status: 'pending',
    });
    return response.data;
  } catch (error) {
    console.error('Error creating task:', error);
    throw error;
  }
};

/**
 * Update task status
 */
export const updateTaskStatus = async (taskId, status) => {
  try {
    const response = await api.put(`/tasks/${taskId}`, { status });
    return response.data;
  } catch (error) {
    console.error('Error updating task:', error);
    throw error;
  }
};

/**
 * Delete a task
 */
export const deleteTask = async (taskId) => {
  try {
    const response = await api.delete(`/tasks/${taskId}`);
    return response.data;
  } catch (error) {
    console.error('Error deleting task:', error);
    throw error;
  }
};

/**
 * Save brain dump and process it
 */
export const saveBrainDump = async (text) => {
  try {
    const response = await api.post('/brain-dump', { text });
    return response.data;
  } catch (error) {
    console.error('Error saving brain dump:', error);
    // Mock response for development
    return { tasks_saved: text.split('\n').filter(line => line.trim()).length };
  }
};

/**
 * AI Task Breakdown
 */
export const aiTaskBreakdown = async (text) => {
  try {
    const response = await api.post('/ai/task-breakdown', { text });
    return response.data;
  } catch (error) {
    console.error('Error with AI task breakdown:', error);
    throw error;
  }
};

export default api;
