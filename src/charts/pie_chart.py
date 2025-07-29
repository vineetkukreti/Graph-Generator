"""
Pie chart implementation.
Creates professional pie charts with labels and percentages.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from typing import Dict, Any
from PIL import Image

from src.charts.base_chart import BaseChart
from src.config.constants import UI_COLORS


class PieChart(BaseChart):
    """Pie chart implementation."""
    
    def create_chart(self) -> Image.Image:
        """Create pie chart."""
        fig, ax = self.create_figure()
        
        # Extract data
        labels = self.data['labels']
        values = self.data['values']
        
        # Convert to numpy arrays
        values_array = np.array(values)
        
        # Get colors
        colors = self.get_color_palette('pastel')
        
        # Calculate percentages
        total = np.sum(values_array)
        percentages = (values_array / total) * 100
        
        # Create pie chart
        wedges, texts, autotexts = ax.pie(values_array, 
                                         labels=labels,
                                         colors=colors[:len(values_array)],
                                         autopct='%1.1f%%',
                                         startangle=90,
                                         pctdistance=0.85,
                                         labeldistance=1.1,
                                         wedgeprops={'edgecolor': 'white', 
                                                    'linewidth': 2,
                                                    'alpha': 0.9})
        
        # Style the pie chart
        self._style_pie_chart(ax, autotexts, texts)
        
        # Add center circle for modern look
        centre_circle = Circle((0, 0), 0.3, fc='white', ec='white', linewidth=2)
        ax.add_patch(centre_circle)
        
        # Add total value in center
        ax.text(0, 0, f'Total\n{total:.1f}', 
               ha='center', va='center', 
               fontsize=12, weight='bold',
               color=UI_COLORS['text_primary'])
        
        # Equal aspect ratio ensures circular pie
        ax.axis('equal')
        
        # Remove axes
        ax.set_xticks([])
        ax.set_yticks([])
        
        # Adjust layout
        plt.tight_layout()
        
        return self.convert_to_pil_image(fig)
    
    def _style_pie_chart(self, ax, autotexts, texts):
        """Apply professional styling to pie chart elements."""
        # Style percentage labels
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontsize(10)
            autotext.set_weight('bold')
        
        # Style category labels
        for text in texts:
            text.set_color(UI_COLORS['text_primary'])
            text.set_fontsize(11)
            text.set_weight('medium') 