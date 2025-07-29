"""
UI utilities for the chart generator.
Handles fonts, images, shadows, and visual effects.
"""

import os
from functools import lru_cache
from typing import Optional, Tuple
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from src.config.constants import CANVAS_HEIGHT, UI_COLORS

# Global font cache
_FONT_CACHE = {}


@lru_cache(maxsize=32)
def load_and_resize_logo(logo_path: str, max_height: Optional[int] = None) -> Optional[Image.Image]:
    """Load and resize logo while preserving aspect ratio. Cached for performance."""
    if not logo_path or not os.path.exists(logo_path):
        return None
    
    if max_height is None:
        # Logo should be 15% of canvas height as specified
        max_height = int(CANVAS_HEIGHT * 0.15)
    
    try:
        logo = Image.open(logo_path)
        if logo.mode != 'RGBA':
            logo = logo.convert('RGBA')
        
        # Resize preserving aspect ratio
        width, height = logo.size
        if height > max_height:
            ratio = max_height / height
            new_width = int(width * ratio)
            logo = logo.resize((new_width, max_height), Image.Resampling.LANCZOS)
        
        return logo
    except Exception as e:
        print(f"Warning: Could not load logo from {logo_path}: {e}")
        return None


@lru_cache(maxsize=128)
def get_font(size: int, weight: str = 'regular'):
    """Get font with modern typography and proper fallbacks. Cached for performance."""
    cache_key = f"{size}_{weight}"
    if cache_key in _FONT_CACHE:
        return _FONT_CACHE[cache_key]
    
    fonts_to_try = []
    
    if weight == 'bold':
        fonts_to_try = [
            # Modern system fonts
            "/System/Library/Fonts/SF-Pro-Display-Bold.otf",
            "/System/Library/Fonts/Helvetica-Bold.ttc",
            "arial-bold.ttf",
            "Arial-Bold.ttf",
            # Linux fonts
            "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        ]
    elif weight == 'medium':
        fonts_to_try = [
            "/System/Library/Fonts/SF-Pro-Display-Medium.otf",
            "/System/Library/Fonts/Helvetica.ttc",
            "arial.ttf",
            "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        ]
    else:  # regular
        fonts_to_try = [
            "/System/Library/Fonts/SF-Pro-Text-Regular.otf",
            "/System/Library/Fonts/Helvetica.ttc",
            "arial.ttf",
            "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        ]
    
    font = None
    for font_path in fonts_to_try:
        try:
            font = ImageFont.truetype(font_path, size)
            break
        except OSError:
            continue
    
    if font is None:
        font = ImageFont.load_default()
    
    _FONT_CACHE[cache_key] = font
    return font


def add_shadow(image: Image.Image, offset: Tuple[int, int] = (4, 4), 
               blur_radius: int = 8, shadow_opacity: int = 38) -> Image.Image:
    """Add subtle drop shadow to an image. Optimized for performance."""
    # Pre-calculate dimensions
    shadow_width = image.width + offset[0] + blur_radius * 2
    shadow_height = image.height + offset[1] + blur_radius * 2
    
    # Create shadow layer
    shadow = Image.new('RGBA', (shadow_width, shadow_height), (0, 0, 0, 0))
    
    # Create shadow shape
    shadow_draw = ImageDraw.Draw(shadow)
    shadow_draw.rectangle([blur_radius, blur_radius, 
                          shadow_width - blur_radius - offset[0], 
                          shadow_height - blur_radius - offset[1]], 
                         fill=(0, 0, 0, shadow_opacity))
    
    # Blur the shadow
    shadow = shadow.filter(ImageFilter.GaussianBlur(blur_radius))
    
    # Create result image
    result = Image.new('RGBA', (shadow_width, shadow_height), (0, 0, 0, 0))
    result.paste(shadow, (0, 0), shadow)
    result.paste(image, (blur_radius, blur_radius), image)
    
    return result


@lru_cache(maxsize=32)
def create_rounded_rectangle(width: int, height: int, radius: int, 
                           fill_color: Optional[str] = None) -> Image.Image:
    """Create rounded rectangle with specified dimensions and radius. Cached for performance."""
    if fill_color is None:
        fill_color = UI_COLORS['background']
    
    # Create image with transparency
    image = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    
    # Draw rounded rectangle
    draw.rounded_rectangle([0, 0, width - 1, height - 1], 
                          radius=radius, fill=fill_color)
    
    return image


def create_gradient_background() -> Image.Image:
    """Create modern gradient background with subtle color transitions."""
    width, height = 1600, 900
    
    # Create gradient image
    image = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(image)
    
    # Create subtle gradient from top to bottom
    for y in range(height):
        # Calculate gradient color (very subtle)
        ratio = y / height
        r = int(248 + (ratio * 7))  # 248 to 255
        g = int(250 + (ratio * 5))  # 250 to 255
        b = int(252 + (ratio * 3))  # 252 to 255
        
        color = (r, g, b)
        draw.line([(0, y), (width, y)], fill=color)
    
    return image 