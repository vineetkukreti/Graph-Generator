"""
Dashboard renderer for creating the main chart dashboard.
Handles layout, composition, and rendering of all UI components.
"""

from typing import Dict, Any, List
from PIL import Image, ImageDraw

from src.charts.chart_factory import ChartFactory
from src.utils.ui_utils import (
    load_and_resize_logo, get_font, create_gradient_background,
    create_rounded_rectangle, add_shadow
)
from src.utils.layout_utils import calculate_layout_positions, calculate_card_dimensions
from src.config.constants import (
    CANVAS_WIDTH, CANVAS_HEIGHT, UI_COLORS, FONT_CONFIG, LAYOUT_CONFIG
)


class DashboardRenderer:
    """Main dashboard renderer for creating professional chart dashboards."""
    
    def __init__(self):
        """Initialize the dashboard renderer."""
        self.positions = calculate_layout_positions()
        self.card_dims = calculate_card_dimensions()
    
    def render_dashboard(self, config: Dict[str, Any]) -> Image.Image:
        """Render the complete dashboard with all components."""
        # Create canvas with gradient background
        canvas = create_gradient_background()
        canvas = canvas.convert('RGBA')
        
        # Create main content card
        canvas = self._add_main_card(canvas)
        
        # Add UI components
        canvas = self._add_logo(canvas, config)
        canvas = self._add_title_and_subtitle(canvas, config)
        canvas = self._add_chart(canvas, config)
        canvas = self._add_footer(canvas, config)
        
        return canvas
    
    def _add_main_card(self, canvas: Image.Image) -> Image.Image:
        """Add main content card with shadow."""
        # Create card background
        card = create_rounded_rectangle(
            self.card_dims['width'], 
            self.card_dims['height'], 
            LAYOUT_CONFIG['border_radius'], 
            UI_COLORS['background']
        )
        
        # Add shadow to card
        card_with_shadow = add_shadow(
            card, 
            offset=LAYOUT_CONFIG['shadow_offset'],
            blur_radius=LAYOUT_CONFIG['shadow_blur']
        )
        
        # Paste card onto canvas
        canvas.paste(
            card_with_shadow, 
            (self.card_dims['x'] - 16, self.card_dims['y'] - 16), 
            card_with_shadow
        )
        
        return canvas
    
    def _add_logo(self, canvas: Image.Image, config: Dict[str, Any]) -> Image.Image:
        """Add logo to the dashboard."""
        logo_path = config.get('logo_path')
        if logo_path:
            logo = load_and_resize_logo(logo_path)
            if logo:
                canvas.paste(
                    logo, 
                    (self.positions['logo_x'], self.positions['logo_y']), 
                    logo
                )
        return canvas
    
    def _add_title_and_subtitle(self, canvas: Image.Image, config: Dict[str, Any]) -> Image.Image:
        """Add title and subtitle to the dashboard."""
        draw = ImageDraw.Draw(canvas)
        
        # Draw title
        title = config['title']
        title_font = get_font(FONT_CONFIG['title_size'], 'bold')
        draw.text(
            (self.positions['title_x'], self.positions['title_y']), 
            title, 
            fill=UI_COLORS['text_primary'], 
            font=title_font
        )
        
        # Draw subtitle
        subtitle = config.get('subtitle', '')
        if subtitle:
            subtitle_font = get_font(FONT_CONFIG['subtitle_size'], 'medium')
            draw.text(
                (self.positions['subtitle_x'], self.positions['subtitle_y']), 
                subtitle, 
                fill=UI_COLORS['text_secondary'], 
                font=subtitle_font
            )
        
        return canvas
    

    
    def _add_chart(self, canvas: Image.Image, config: Dict[str, Any]) -> Image.Image:
        """Add chart to the dashboard."""
        # Generate chart
        graph_image = ChartFactory.render_chart(
            config['graph'], 
            self.positions['graph_width'], 
            self.positions['graph_height']
        )
        
        # Resize graph to exact dimensions if needed
        if graph_image.size != (self.positions['graph_width'], self.positions['graph_height']):
            graph_image = graph_image.resize(
                (self.positions['graph_width'], self.positions['graph_height']), 
                Image.Resampling.LANCZOS
            )
        
        # Create graph container
        container_dims = calculate_graph_container_dimensions(
            self.positions['graph_width'], 
            self.positions['graph_height']
        )
        graph_container = create_rounded_rectangle(
            container_dims['width'], 
            container_dims['height'], 
            12, 
            UI_COLORS['surface']
        )
        
        # Paste graph container
        canvas.paste(
            graph_container, 
            (self.positions['graph_x'] + container_dims['offset_x'], 
             self.positions['graph_y'] + container_dims['offset_y']), 
            graph_container
        )
        
        # Paste graph
        canvas.paste(
            graph_image, 
            (self.positions['graph_x'], self.positions['graph_y']), 
            graph_image
        )
        
        return canvas
    
    def _add_footer(self, canvas: Image.Image, config: Dict[str, Any]) -> Image.Image:
        """Add footer to the dashboard."""
        footer = config.get('footer', '')
        if footer:
            draw = ImageDraw.Draw(canvas)
            footer_font = get_font(FONT_CONFIG['footer_size'], 'regular')
            
            # Calculate text width for centering
            bbox = draw.textbbox((0, 0), footer, font=footer_font)
            text_width = bbox[2] - bbox[0]
            x_position = (CANVAS_WIDTH - text_width) // 2
            
            draw.text(
                (x_position, self.positions['footer_y']), 
                footer, 
                fill=UI_COLORS['text_light'], 
                font=footer_font
            )
        
        return canvas


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