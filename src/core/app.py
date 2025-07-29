"""
Main application class for the chart generator.
Orchestrates the entire chart generation process.
"""

import argparse
from typing import Dict, Any

from src.utils.text_utils import validate_config, slugify
from src.utils.file_utils import load_config, generate_unique_filename, ensure_output_directory, get_relative_path
from src.ui.dashboard_renderer import DashboardRenderer


class ChartGeneratorApp:
    """Main application class for generating professional charts."""
    
    def __init__(self):
        """Initialize the chart generator application."""
        self.renderer = DashboardRenderer()
    
    def generate_chart(self, config_path: str, output_dir: str = 'output') -> str:
        """Generate a chart from configuration file."""
        try:
            # Load and validate configuration
            config = load_config(config_path)
            validate_config(config)
            
            # Ensure output directory exists
            ensure_output_directory(output_dir)
            
            # Render dashboard
            canvas = self.renderer.render_dashboard(config)
            
            # Generate output filename
            slug = slugify(config['title'])
            output_path = generate_unique_filename(output_dir, slug)
            
            # Save the image with high quality
            canvas = canvas.convert('RGB')  # Convert back to RGB for final save
            canvas.save(output_path, 'PNG', quality=100, optimize=True)
            
            # Return relative path for downstream scripts
            return get_relative_path(output_path)
            
        except Exception as e:
            raise RuntimeError(f"Error generating chart: {e}")
    
    def run_from_command_line(self):
        """Run the application from command line arguments."""
        parser = argparse.ArgumentParser(description='Generate professional branded charts (Refactored)')
        parser.add_argument('--config', required=True, help='Path to JSON configuration file')
        parser.add_argument('--output-dir', default='output', help='Output directory for generated charts')
        args = parser.parse_args()
        
        try:
            output_path = self.generate_chart(args.config, args.output_dir)
            print(output_path)
        except Exception as e:
            print(f"Error: {e}")
            return 1
        
        return 0


def main():
    """Main entry point for the application."""
    app = ChartGeneratorApp()
    return app.run_from_command_line()


if __name__ == '__main__':
    exit(main()) 