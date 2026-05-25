#!/bin/bash
# Setup script for Unix/Linux/Mac - creates venv and configures Jupyter kernel

cd "$(dirname "$0")"
echo "======================================"
echo "Setting up Jupyter environment..."
echo "======================================"
python3 setup.py "$@"
