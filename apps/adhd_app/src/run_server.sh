#!/bin/bash
# Run ADHD Assistant API Server

echo "🚀 Starting ADHD Assistant API Server..."

# Set PYTHONPATH to workspace root
export PYTHONPATH="$(cd ../../.. && pwd)"

# Run the Flask server
python api_server.py
