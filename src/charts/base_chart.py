"""
Base chart class for the chart generator.
Provides common functionality and interface for all chart types.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, List
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import font_manager
import numpy as np
from PIL import Image
import io

from src.config.constants import CHART_COLORS, UI_COLORS


class BaseChart(ABC):
    """Abstract base class for all chart types."""
    
    def __init__(self, config: Dict[str, Any], width: int, height: int):
        """Initialize chart with configuration and dimensions."""
        self.config = config
        self.width = width
        self.height = height
        self.data = config['data']
        self.setup_matplotlib_style()
    
    def setup_matplotlib_style(self):
        """Setup matplotlib style for professional appearance."""
        plt.style.use('default')
        
        # Configure matplotlib for high-quality output
        plt.rcParams['figure.dpi'] = 300
        plt.rcParams['savefig.dpi'] = 300
        plt.rcParams['font.size'] = 10
        plt.rcParams['axes.linewidth'] = 0.8
        plt.rcParams['axes.edgecolor'] = UI_COLORS['border']
        plt.rcParams['axes.facecolor'] = 'white'
        plt.rcParams['figure.facecolor'] = 'white'
        plt.rcParams['grid.color'] = UI_COLORS['border']
        plt.rcParams['grid.linestyle'] = '-'
        plt.rcParams['grid.linewidth'] = 0.5
        plt.rcParams['grid.alpha'] = 0.3
    
    def get_color_palette(self, palette_name: str = 'primary') -> List[str]:
        """Get color palette for the chart."""
        return CHART_COLORS.get(palette_name, CHART_COLORS['primary'])
    
    def create_figure(self) -> plt.Figure:
        """Create matplotlib figure with specified dimensions."""
        fig, ax = plt.subplots(figsize=(self.width/100, self.height/100), dpi=100)
        return fig, ax
    
    def apply_professional_styling(self, ax: plt.Axes):
        """Apply professional styling to the chart axes."""
        # Remove top and right spines
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        
        # Style left and bottom spines
        ax.spines['left'].set_color(UI_COLORS['border'])
        ax.spines['bottom'].set_color(UI_COLORS['border'])
        ax.spines['left'].set_linewidth(0.8)
        ax.spines['bottom'].set_linewidth(0.8)
        
        # Set background color
        ax.set_facecolor('white')
        
        # Style grid
        ax.grid(True, alpha=0.3, linestyle='-', linewidth=0.5, color=UI_COLORS['border'])
        ax.set_axisbelow(True)
        
        # Style tick labels
        ax.tick_params(colors=UI_COLORS['text_secondary'], labelsize=9)
        ax.tick_params(axis='x', rotation=0)
    
    def convert_to_pil_image(self, fig: plt.Figure) -> Image.Image:
        """Convert matplotlib figure to PIL Image."""
        buffer = io.BytesIO()
        fig.savefig(buffer, format='png', bbox_inches='tight', 
                   facecolor='white', edgecolor='none', dpi=300)
        buffer.seek(0)
        
        # Convert to PIL Image
        graph_image = Image.open(buffer)
        plt.close(fig)
        
        return graph_image
    
    @abstractmethod
    def create_chart(self) -> Image.Image:
        """Create the specific chart type. Must be implemented by subclasses."""
        pass
    
    def render(self) -> Image.Image:
        """Main method to render the chart."""
        return self.create_chart() 