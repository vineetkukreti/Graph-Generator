#!/usr/bin/env python3
"""
Test script to verify the refactored chart generator works correctly.
Compares output with the original implementation.
"""

import sys
import os
import subprocess
import json
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.core.app import ChartGeneratorApp


def test_chart_generation():
    """Test chart generation with different chart types."""
    app = ChartGeneratorApp()
    
    # Test configurations
    test_configs = [
        'configs/cbd_market_forecast.json',
        'configs/line_chart.json',
        'configs/pie_chart.json',
        'configs/area_chart.json',
        'configs/bar_chart.json'
    ]
    
    print("Testing refactored chart generator...")
    print("=" * 50)
    
    for config_path in test_configs:
        if os.path.exists(config_path):
            try:
                print(f"Testing {config_path}...")
                output_path = app.generate_chart(config_path, 'output_test')
                print(f"✓ Successfully generated: {output_path}")
                
                # Verify file was created
                if os.path.exists(output_path):
                    file_size = os.path.getsize(output_path)
                    print(f"  File size: {file_size:,} bytes")
                else:
                    print("  ✗ Error: Output file not found")
                    
            except Exception as e:
                print(f"  ✗ Error: {e}")
        else:
            print(f"  ⚠ Skipping {config_path} (file not found)")
        
        print()
    
    print("Test completed!")


def test_original_vs_refactored():
    """Compare original and refactored implementations."""
    print("Comparing original vs refactored implementation...")
    print("=" * 50)
    
    # Test with CBD market forecast
    config_path = 'configs/cbd_market_forecast.json'
    
    if not os.path.exists(config_path):
        print(f"Config file not found: {config_path}")
        return
    
    try:
        # Generate with refactored version
        app = ChartGeneratorApp()
        refactored_output = app.generate_chart(config_path, 'output_refactored')
        print(f"✓ Refactored output: {refactored_output}")
        
        # Check if original script exists and run it
        if os.path.exists('generate_cbd_market_graph.py'):
            print("Running original implementation...")
            result = subprocess.run([
                'python', 'generate_cbd_market_graph.py', 
                '--config', config_path
            ], capture_output=True, text=True)
            
            if result.returncode == 0:
                original_output = result.stdout.strip()
                print(f"✓ Original output: {original_output}")
                
                # Compare file sizes
                if os.path.exists(refactored_output) and os.path.exists(original_output):
                    refactored_size = os.path.getsize(refactored_output)
                    original_size = os.path.getsize(original_output)
                    
                    print(f"  Refactored file size: {refactored_size:,} bytes")
                    print(f"  Original file size: {original_size:,} bytes")
                    
                    if abs(refactored_size - original_size) < 1000:  # Allow small differences
                        print("  ✓ File sizes are similar (within tolerance)")
                    else:
                        print("  ⚠ File sizes differ significantly")
                else:
                    print("  ⚠ Could not compare file sizes")
            else:
                print(f"  ✗ Original implementation failed: {result.stderr}")
        else:
            print("  ⚠ Original implementation not found")
            
    except Exception as e:
        print(f"  ✗ Error during comparison: {e}")


if __name__ == '__main__':
    print("Chart Generator Refactoring Test Suite")
    print("=" * 50)
    
    # Test 1: Basic functionality
    test_chart_generation()
    
    print("\n" + "=" * 50)
    
    # Test 2: Comparison with original
    test_original_vs_refactored()
    
    print("\nTest suite completed!") 