"""
Design constants and configuration values for the chart generator.
Centralized configuration management for maintainability.
"""

# Design constants based on 8px grid system
GRID_UNIT = 8
CANVAS_WIDTH = 1600
CANVAS_HEIGHT = 900
GOLDEN_RATIO = 1.618

# Extended color palette for multiple chart types
CHART_COLORS = {
    'primary': ['#1F3B4D', '#26547C', '#5C88B0', '#A3BFD9', '#D4E4F1'],
    'secondary': ['#10B981', '#F59E0B', '#EF4444', '#8B5CF6', '#06B6D4'],
    'gradient': ['#667EEA', '#764BA2', '#F093FB', '#F5576C', '#4FACFE'],
    'pastel': ['#FFB3BA', '#BAFFC9', '#BAE1FF', '#FFFFBA', '#FFB3F7']
}

# CBD Market specific color palette (for backward compatibility)
CBD_COLORS = {
    'cbd_oil': '#1F3B4D',        # Deep blue-gray
    'cbd_isolates': '#26547C',   # Medium blue
    'cbd_concentrates': '#5C88B0', # Light blue
    'others': '#A3BFD9',         # Very light blue
}

# Professional color palette for UI elements
UI_COLORS = {
    'text_primary': '#111827',   # Almost black
    'text_secondary': '#6B7280', # Medium gray
    'text_light': '#9CA3AF',     # Light gray
    'background': '#FFFFFF',     # Pure white
    'surface': '#F9FAFB',        # Light gray background
    'border': '#E5E7EB',         # Border gray
    'shadow': 'rgba(0, 0, 0, 0.1)'  # Subtle shadow
}



# Supported chart types
SUPPORTED_CHART_TYPES = ['stacked_bar', 'line', 'pie', 'area', 'bar']

# Font configuration
FONT_CONFIG = {
    'title_size': 48,
    'subtitle_size': 24,
    'footer_size': 18
}

# Layout configuration
LAYOUT_CONFIG = {
    'card_margin': GRID_UNIT * 4,  # 32px
    'logo_max_height_ratio': 0.15,  # 15% of canvas height
    'graph_margin': GRID_UNIT * 8,  # 64px
    'border_radius': 16,
    'shadow_blur': 16,
    'shadow_offset': (0, 4)
} 