"""
Chart factory for creating different chart types.
Provides a clean interface for chart creation.
"""

from typing import Dict, Any
from PIL import Image

from src.charts.base_chart import BaseChart
from src.charts.stacked_bar_chart import StackedBarChart
from src.charts.line_chart import LineChart
from src.charts.pie_chart import PieChart
from src.charts.area_chart import AreaChart
from src.charts.bar_chart import BarChart
from src.config.constants import SUPPORTED_CHART_TYPES


class ChartFactory:
    """Factory class for creating different chart types."""
    
    _chart_classes = {
        'stacked_bar': StackedBarChart,
        'line': LineChart,
        'pie': PieChart,
        'area': AreaChart,
        'bar': BarChart
    }
    
    @classmethod
    def create_chart(cls, config: Dict[str, Any], width: int, height: int) -> BaseChart:
        """Create a chart instance based on the configuration."""
        chart_type = config.get('type')
        
        if chart_type not in SUPPORTED_CHART_TYPES:
            raise ValueError(f"Unsupported chart type: {chart_type}. "
                           f"Supported types: {SUPPORTED_CHART_TYPES}")
        
        chart_class = cls._chart_classes.get(chart_type)
        if not chart_class:
            raise ValueError(f"Chart type '{chart_type}' not implemented")
        
        return chart_class(config, width, height)
    
    @classmethod
    def render_chart(cls, config: Dict[str, Any], width: int, height: int) -> Image.Image:
        """Create and render a chart based on the configuration."""
        chart = cls.create_chart(config, width, height)
        return chart.render()
    
    @classmethod
    def get_supported_types(cls) -> list:
        """Get list of supported chart types."""
        return SUPPORTED_CHART_TYPES.copy() 