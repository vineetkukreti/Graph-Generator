"""
Area chart implementation.
Creates professional area charts with gradient fills.
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, Any
from PIL import Image

from src.charts.base_chart import BaseChart
from src.config.constants import UI_COLORS


class AreaChart(BaseChart):
    """Area chart implementation."""
    
    def create_chart(self) -> Image.Image:
        """Create area chart."""
        fig, ax = self.create_figure()
        
        # Extract data
        labels = self.data['labels']
        values = self.data['values']
        
        # Convert to numpy arrays
        x_positions = np.arange(len(labels))
        values_array = np.array(values)
        
        # Get colors
        colors = self.get_color_palette('gradient')
        
        # Create area plot
        ax.fill_between(x_positions, values_array, 
                       color=colors[0], alpha=0.7,
                       edgecolor=colors[0], linewidth=2)
        
        # Add line on top
        ax.plot(x_positions, values_array, 
               color=colors[0], linewidth=3,
               marker='o', markersize=8,
               markerfacecolor=colors[0],
               markeredgecolor='white',
               markeredgewidth=2)
        
        # Apply professional styling
        self.apply_professional_styling(ax)
        
        # Set labels and title
        ax.set_xlabel('Period', fontsize=11, color=UI_COLORS['text_primary'])
        ax.set_ylabel('Value', fontsize=11, color=UI_COLORS['text_primary'])
        
        # Set x-axis ticks
        ax.set_xticks(x_positions)
        ax.set_xticklabels(labels, rotation=0)
        
        # Add value labels on points
        self._add_value_labels(ax, x_positions, values_array)
        
        # Add trend line if multiple points
        if len(values_array) > 1:
            self._add_trend_line(ax, x_positions, values_array, colors[1])
        
        # Adjust layout
        plt.tight_layout()
        
        return self.convert_to_pil_image(fig)
    
    def _add_value_labels(self, ax, x_positions, values_array):
        """Add value labels above data points."""
        for i, (x, y) in enumerate(zip(x_positions, values_array)):
            ax.text(x, y + (max(values_array) - min(values_array)) * 0.05,
                   f'{y:.1f}', ha='center', va='bottom',
                   fontsize=9, color=UI_COLORS['text_secondary'],
                   weight='bold')
    
    def _add_trend_line(self, ax, x_positions, values_array, color):
        """Add trend line to show overall direction."""
        # Calculate trend line
        z = np.polyfit(x_positions, values_array, 1)
        p = np.poly1d(z)
        
        # Plot trend line
        ax.plot(x_positions, p(x_positions), 
               color=color, linewidth=2, 
               linestyle='--', alpha=0.7,
               label='Trend')
        
        # Add legend
        ax.legend(loc='upper left', frameon=True, 
                 fancybox=True, shadow=True, fontsize=9) 