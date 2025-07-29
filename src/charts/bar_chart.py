"""
Bar chart implementation.
Creates professional bar charts with value labels.
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, Any
from PIL import Image

from src.charts.base_chart import BaseChart
from src.config.constants import UI_COLORS


class BarChart(BaseChart):
    """Bar chart implementation."""
    
    def create_chart(self) -> Image.Image:
        """Create bar chart."""
        fig, ax = self.create_figure()
        
        # Extract data
        labels = self.data['labels']
        values = self.data['values']
        
        # Convert to numpy arrays
        x_positions = np.arange(len(labels))
        values_array = np.array(values)
        
        # Get colors
        colors = self.get_color_palette('secondary')
        
        # Create bars
        bars = ax.bar(x_positions, values_array, 
                     color=colors[0], alpha=0.9,
                     edgecolor='white', linewidth=1,
                     width=0.7)
        
        # Apply professional styling
        self.apply_professional_styling(ax)
        
        # Set labels and title
        ax.set_xlabel('Category', fontsize=11, color=UI_COLORS['text_primary'])
        ax.set_ylabel('Value', fontsize=11, color=UI_COLORS['text_primary'])
        
        # Set x-axis ticks
        ax.set_xticks(x_positions)
        ax.set_xticklabels(labels, rotation=45, ha='right')
        
        # Add value labels on bars
        self._add_value_labels(ax, bars, values_array)
        
        # Adjust layout
        plt.tight_layout()
        
        return self.convert_to_pil_image(fig)
    
    def _add_value_labels(self, ax, bars, values_array):
        """Add value labels on top of bars."""
        for bar, value in zip(bars, values_array):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, height + (max(values_array) - min(values_array)) * 0.02,
                   f'{value:.1f}', ha='center', va='bottom',
                   fontsize=9, color=UI_COLORS['text_secondary'],
                   weight='bold') 