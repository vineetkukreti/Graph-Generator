"""
Text processing utilities for the chart generator.
Handles text formatting, validation, and transformation.
"""

import re
from typing import Dict, Any


def slugify(text: str) -> str:
    """Convert text to slug format: lowercase, a-z0-9 and hyphens only."""
    slug = re.sub(r'[^a-zA-Z0-9\s-]', '', text)
    slug = re.sub(r'\s+', '-', slug.strip())
    return slug.lower()


def validate_config(config: Dict[str, Any]) -> None:
    """Validate the input configuration for different chart types."""
    required_fields = ['title', 'graph']
    for field in required_fields:
        if field not in config:
            raise ValueError(f"Missing required field: {field}")
    
    if 'type' not in config['graph']:
        raise ValueError("Missing required field: graph.type")
    
    if 'data' not in config['graph']:
        raise ValueError("Missing required field: graph.data")
    
    graph_type = config['graph']['type']
    graph_data = config['graph']['data']
    
    # Validate based on chart type
    if graph_type == 'stacked_bar':
        _validate_stacked_bar_data(graph_data)
    elif graph_type in ['line', 'area', 'bar']:
        _validate_linear_data(graph_data)
    elif graph_type == 'pie':
        _validate_pie_data(graph_data)
    else:
        raise ValueError(f"Unsupported chart type: {graph_type}. Supported types: stacked_bar, line, area, bar, pie")


def _validate_stacked_bar_data(graph_data: Dict[str, Any]) -> None:
    """Validate stacked bar chart data structure."""
    required_fields = ['years', 'categories', 'values']
    for field in required_fields:
        if field not in graph_data:
            raise ValueError(f"Missing required field: graph.data.{field}")
    
    years = graph_data['years']
    categories = graph_data['categories']
    values = graph_data['values']
    
    if len(values) != len(years):
        raise ValueError("graph.data.values must have same length as graph.data.years")
    
    for year_data in values:
        if len(year_data) != len(categories):
            raise ValueError("Each year's data must have same length as categories")


def _validate_linear_data(graph_data: Dict[str, Any]) -> None:
    """Validate line, area, and bar chart data structure."""
    required_fields = ['labels', 'values']
    for field in required_fields:
        if field not in graph_data:
            raise ValueError(f"Missing required field: graph.data.{field}")
    
    labels = graph_data['labels']
    values = graph_data['values']
    
    if len(labels) != len(values):
        raise ValueError("graph.data.labels and graph.data.values must have same length")


def _validate_pie_data(graph_data: Dict[str, Any]) -> None:
    """Validate pie chart data structure."""
    required_fields = ['labels', 'values']
    for field in required_fields:
        if field not in graph_data:
            raise ValueError(f"Missing required field: graph.data.{field}")
    
    labels = graph_data['labels']
    values = graph_data['values']
    
    if len(labels) != len(values):
        raise ValueError("graph.data.labels and graph.data.values must have same length") 