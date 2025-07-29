"""
Mathematical utilities for the chart generator.
Handles calculations, statistics, and data processing.
"""

import math
from typing import List





def calculate_total_values(values: List[List[float]]) -> List[float]:
    """Calculate total values for each period from stacked data."""
    return [sum(year_data) for year_data in values]


def normalize_values(values: List[float]) -> List[float]:
    """Normalize values to 0-1 range for percentage calculations."""
    if not values:
        return []
    
    max_val = max(values)
    if max_val == 0:
        return [0.0] * len(values)
    
    return [v / max_val for v in values]


def round_to_decimal(value: float, decimal_places: int = 2) -> float:
    """Round a value to specified decimal places."""
    return round(value, decimal_places) 