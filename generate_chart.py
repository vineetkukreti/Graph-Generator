
#!/usr/bin/env python3
"""
Multi-Chart Graph Generator (Refactored)
Creates professional branded charts with corporate dashboard styling.
Features: 16:9 aspect ratio, 8px grid system, modern typography, and brand-consistent colors.
Supports: Stacked Bar, Line, Pie, Area, and Bar charts.

This is the refactored version with modular architecture for better maintainability.
"""

import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.core.app import main

if __name__ == '__main__':
    exit(main()) 