"""
Layout utilities for the chart generator.
Handles positioning, layout calculations, and grid system.
"""

from functools import lru_cache
from typing import Dict
from src.config.constants import (
    GRID_UNIT, CANVAS_WIDTH, CANVAS_HEIGHT, LAYOUT_CONFIG
)


@lru_cache(maxsize=1)
def calculate_layout_positions() -> Dict[str, int]:
    """Calculate positions based on 8px grid system and 16:9 layout. Cached."""
    return {
        # Header section
        'title_x': GRID_UNIT * 8,  # 64px from left
        'title_y': GRID_UNIT * 8,  # 64px from top
        'subtitle_x': GRID_UNIT * 8,
        'subtitle_y': GRID_UNIT * 16,  # 128px from top
        
        # Logo section (top right, 15% height)
        'logo_x': CANVAS_WIDTH - (GRID_UNIT * 8) - 200,  # 200px width, 64px margin
        'logo_y': GRID_UNIT * 8,  # 64px from top
        
        # Graph area (full width)
        'graph_x': GRID_UNIT * 8,   # 64px margin
        'graph_y': GRID_UNIT * 32,  # 256px from top
        'graph_width': CANVAS_WIDTH - (GRID_UNIT * 16),  # Full width minus margins
        'graph_height': CANVAS_HEIGHT - (GRID_UNIT * 64), # Space for header and footer
        
        # Footer
        'footer_y': CANVAS_HEIGHT - (GRID_UNIT * 12)  # 96px from bottom
    }


def calculate_card_dimensions() -> Dict[str, int]:
    """Calculate main content card dimensions."""
    card_margin = LAYOUT_CONFIG['card_margin']
    card_width = CANVAS_WIDTH - (card_margin * 2)
    card_height = CANVAS_HEIGHT - (card_margin * 2)
    
    return {
        'width': card_width,
        'height': card_height,
        'margin': card_margin,
        'x': card_margin,
        'y': card_margin
    }


def calculate_graph_container_dimensions(graph_width: int, graph_height: int) -> Dict[str, int]:
    """Calculate graph container dimensions with padding."""
    padding = 16
    container_width = graph_width + (padding * 2)
    container_height = graph_height + (padding * 2)
    
    return {
        'width': container_width,
        'height': container_height,
        'padding': padding,
        'offset_x': -padding,
        'offset_y': -padding
    }


def center_text_horizontally(text: str, font, canvas_width: int) -> int:
    """Calculate x position to center text horizontally."""
    # This is a placeholder - actual implementation would need PIL ImageDraw
    # to calculate text bounding box
    return (canvas_width - len(text) * 10) // 2  # Rough approximation 