"""
Stacked bar chart implementation.
Creates professional stacked bar charts with multiple categories.
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, Any
from PIL import Image
import matplotlib.patches as mpatches

from src.charts.base_chart import BaseChart
from src.config.constants import CBD_COLORS, UI_COLORS


class StackedBarChart(BaseChart):
    """Stacked bar chart implementation."""
    
    def create_chart(self) -> Image.Image:
        """Create stacked bar chart."""
        fig, ax = self.create_figure()
        
        # Extract data
        years = self.data['years']
        categories = self.data['categories']
        values = self.data['values']
        
        # Convert to numpy arrays for easier manipulation
        values_array = np.array(values)
        
        # Create x positions for bars
        x_positions = np.arange(len(years))
        
        # Get colors for categories
        colors = self._get_category_colors(categories)
        
        # Create stacked bars
        bottom = np.zeros(len(years))
        bars = []
        
        for i, category in enumerate(categories):
            bar = ax.bar(x_positions, values_array[:, i], bottom=bottom, 
                        color=colors[i], alpha=0.9, edgecolor='white', 
                        linewidth=0.5, width=0.7)
            bars.append(bar)
            bottom += values_array[:, i]
        
        # Apply professional styling
        self.apply_professional_styling(ax)
        
        # Set labels and title
        ax.set_xlabel('Year', fontsize=11, color=UI_COLORS['text_primary'])
        ax.set_ylabel('Market Size (USD Billion)', fontsize=11, color=UI_COLORS['text_primary'])
        
        # Set x-axis ticks
        ax.set_xticks(x_positions)
        ax.set_xticklabels(years, rotation=0)
        
        # Add value labels on bars
        self._add_value_labels(ax, bars, values_array)
        
        # Add legend
        legend_elements = [mpatches.Patch(color=colors[i], label=category) 
                          for i, category in enumerate(categories)]
        ax.legend(handles=legend_elements, loc='upper left', 
                 frameon=True, fancybox=True, shadow=True, 
                 fontsize=9, framealpha=0.9)
        
        # Adjust layout
        plt.tight_layout()
        
        return self.convert_to_pil_image(fig)
    
    def _get_category_colors(self, categories: list) -> list:
        """Get colors for categories, using CBD colors if available."""
        colors = []
        for category in categories:
            # Try to match with CBD colors first
            category_lower = category.lower().replace(' ', '_')
            if category_lower in CBD_COLORS:
                colors.append(CBD_COLORS[category_lower])
            else:
                # Use default palette
                colors.append(self.get_color_palette()[len(colors) % len(self.get_color_palette())])
        return colors
    
    def _add_value_labels(self, ax, bars, values_array):
        """Add value labels on top of bars."""
        for i, bar_group in enumerate(bars):
            for j, bar in enumerate(bar_group):
                height = bar.get_height()
                if height > 0:
                    # Calculate total height for this bar
                    total_height = sum(values_array[j])
                    # Position label at the top of this segment
                    bottom_height = sum(values_array[j][:i])
                    label_y = bottom_height + height / 2
                    
                    # Only show label if segment is large enough
                    if height / total_height > 0.1:  # 10% threshold
                        ax.text(bar.get_x() + bar.get_width()/2, label_y,
                               f'{height:.1f}', ha='center', va='center',
                               fontsize=8, color='white', weight='bold') 