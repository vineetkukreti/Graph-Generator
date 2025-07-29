"""
File handling utilities for the chart generator.
Handles file operations, path management, and configuration loading.
"""

import os
import json
from typing import Dict, Any


def load_config(config_path: str) -> Dict[str, Any]:
    """Load and parse JSON configuration file."""
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
        return config
    except FileNotFoundError:
        raise FileNotFoundError(f"Configuration file not found: {config_path}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in configuration file: {e}")


def generate_unique_filename(output_dir: str, base_name: str) -> str:
    """Generate unique filename by appending numbers if needed."""
    filename = f"{base_name}.png"
    filepath = os.path.join(output_dir, filename)
    
    counter = 1
    while os.path.exists(filepath):
        filename = f"{base_name}-{counter}.png"
        filepath = os.path.join(output_dir, filename)
        counter += 1
    
    return filepath


def ensure_output_directory(output_dir: str) -> None:
    """Create output directory if it doesn't exist."""
    os.makedirs(output_dir, exist_ok=True)


def get_relative_path(filepath: str) -> str:
    """Get relative path from current working directory."""
    return os.path.relpath(filepath) 