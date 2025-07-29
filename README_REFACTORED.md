# Chart Generator - Refactored Version

A modular, professional chart generation system that creates beautiful branded charts with corporate dashboard styling.

## 🚀 Features

- **5 Chart Types**: Stacked Bar, Line, Pie, Area, and Bar charts
- **Professional Design**: 16:9 aspect ratio, 8px grid system, modern typography
- **Brand Consistency**: Corporate color palettes and styling
- **Performance Optimized**: Cached operations, vectorized calculations
- **Modular Architecture**: Clean separation of concerns, easy to maintain and extend

## 📁 Project Structure

```
svg_grapgh/
├── src/                          # Source code (REFACTORED)
│   ├── config/                   # Configuration and constants
│   │   ├── __init__.py
│   │   └── constants.py          # Design constants, colors, layouts
│   ├── core/                     # Core application logic
│   │   ├── __init__.py
│   │   └── app.py               # Main application class
│   ├── charts/                   # Chart implementations
│   │   ├── __init__.py
│   │   ├── base_chart.py        # Abstract base chart class
│   │   ├── chart_factory.py     # Chart factory for creation
│   │   ├── stacked_bar_chart.py # Stacked bar chart
│   │   ├── line_chart.py        # Line chart
│   │   ├── pie_chart.py         # Pie chart
│   │   ├── area_chart.py        # Area chart
│   │   └── bar_chart.py         # Bar chart
│   ├── ui/                      # UI components
│   │   ├── __init__.py
│   │   └── dashboard_renderer.py # Main dashboard renderer
│   └── utils/                   # Utility functions
│       ├── __init__.py
│       ├── file_utils.py        # File operations
│       ├── layout_utils.py      # Layout calculations
│       ├── math_utils.py        # Mathematical calculations
│       ├── text_utils.py        # Text processing
│       └── ui_utils.py          # UI utilities
├── configs/                     # Configuration files
├── output/                      # Generated charts
├── assets/                      # Assets (logos, etc.)
├── tests/                       # Test files
├── generate_cbd_market_graph.py # ORIGINAL monolithic script (947 lines)
├── generate_chart.py           # NEW refactored script
├── test_refactored.py          # Test suite
└── README_REFACTORED.md        # This file
```

## 🏗️ Architecture Overview

### Core Components

1. **Configuration Management** (`src/config/`)

   - Centralized constants and design values
   - Color palettes, layout configurations
   - Easy to modify and extend

2. **Chart System** (`src/charts/`)

   - Abstract base class for all charts
   - Factory pattern for chart creation
   - Individual implementations for each chart type
   - Consistent styling and behavior

3. **UI System** (`src/ui/`)

   - Dashboard renderer for main layout
   - Professional styling and effects

4. **Utilities** (`src/utils/`)

   - Modular utility functions
   - Separation of concerns
   - Reusable across components

5. **Core Application** (`src/core/`)
   - Main application orchestration
   - Command-line interface
   - Error handling and validation

## 🚀 Quick Start

### Installation

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. **Use the NEW refactored version:**

```bash
python generate_chart.py --config configs/cbd_market_forecast.json
```

3. **Or use the ORIGINAL version (still works):**

```bash
python generate_cbd_market_graph.py --config configs/cbd_market_forecast.json
```

### Usage

Both scripts use the same command-line interface:

```bash
# Basic usage
python generate_chart.py --config <config_file.json>

# Specify output directory
python generate_chart.py --config <config_file.json> --output-dir <output_directory>
```

### Configuration Format

The configuration format remains the same for both versions:

```json
{
  "title": "Chart Title",
  "subtitle": "Chart Subtitle",
  "logo_path": "assets/logo.png",
  "graph": {
    "type": "stacked_bar",
    "data": {
      "years": ["2024", "2025", "2026"],
      "categories": ["Category 1", "Category 2"],
      "values": [
        [1.0, 2.0],
        [1.5, 2.5],
        [2.0, 3.0]
      ]
    }
  },
  "footer": "© 2024 Chart Generator"
}
```

## 🧪 Testing

Run the test suite to verify functionality:

```bash
python test_refactored.py
```

This will:

- Test all chart types with the refactored version
- Compare with original implementation
- Verify output quality

## 🔄 Migration from Original

### What Changed

- **Structure**: Modular architecture instead of monolithic file
- **Maintainability**: Clean separation of concerns
- **Extensibility**: Easy to add new features
- **Testing**: Unit testable components

### What Stayed the Same

- **Functionality**: All original features preserved
- **Output Quality**: Same professional appearance
- **Configuration**: Same JSON format
- **Performance**: All optimizations maintained
- **Command Line**: Same interface

### Migration Steps

1. **Option 1**: Use `generate_chart.py` instead of `generate_cbd_market_graph.py`
2. **Option 2**: Keep using the original script - it still works perfectly
3. **Option 3**: Gradually migrate by testing both versions

## 🎯 Benefits of Refactoring

### For Developers

- **Maintainability**: Easy to understand and modify
- **Testability**: Unit testable components
- **Extensibility**: Simple to add new features
- **Code Reuse**: Shared utilities and base classes

### For Users

- **Same Interface**: No changes to usage
- **Better Performance**: Optimized architecture
- **More Features**: Easier to add new chart types
- **Reliability**: Better error handling and validation

## 🔧 Development

### Adding New Chart Types

1. Create a new chart class in `src/charts/`:

```python
from src.charts.base_chart import BaseChart

class NewChart(BaseChart):
    def create_chart(self) -> Image.Image:
        # Implementation here
        pass
```

2. Add to the factory in `src/charts/chart_factory.py`:

```python
_chart_classes = {
    # ... existing charts
    'new_chart': NewChart
}
```

3. Update constants in `src/config/constants.py`:

```python
SUPPORTED_CHART_TYPES = ['stacked_bar', 'line', 'pie', 'area', 'bar', 'new_chart']
```

### Modifying Styles

Edit `src/config/constants.py` to modify:

- Colors and palettes
- Layout dimensions
- Font configurations
- UI styling

### Adding UI Components

1. Create component in `src/ui/`
2. Integrate into `DashboardRenderer`
3. Follow existing patterns for consistency

## 📊 Performance Optimizations

Both versions maintain all original optimizations:

- **Cached Operations**: Font loading, layout calculations
- **Vectorized Math**: NumPy operations for calculations
- **Efficient Rendering**: Optimized matplotlib configurations
- **Memory Management**: Proper cleanup and resource handling

## 🐛 Troubleshooting

### Common Issues

1. **Import Errors**: Ensure `src/` is in Python path
2. **Missing Dependencies**: Run `pip install -r requirements.txt`
3. **Configuration Errors**: Check JSON format and required fields
4. **Output Issues**: Verify output directory permissions

### Debug Mode

For debugging, you can import and use components directly:

```python
from src.core.app import ChartGeneratorApp
from src.charts.chart_factory import ChartFactory

# Test individual components
app = ChartGeneratorApp()
```

## 📈 Future Enhancements

The modular architecture enables easy addition of:

- New chart types (scatter, heatmap, etc.)
- Custom themes and styling
- Interactive features
- Export to different formats
- Web interface
- Real-time data integration

## 🤝 Contributing

1. Follow the modular architecture
2. Add tests for new features
3. Maintain backward compatibility
4. Update documentation
5. Follow existing code patterns

## 📄 License

Same as original project.

---

## 📋 Current Status

✅ **REFACTORING COMPLETE**

- **Original Script**: `generate_cbd_market_graph.py` (947 lines) - Still works
- **New Script**: `generate_chart.py` - Modular architecture
- **Both scripts produce identical output quality**
- **100% backward compatibility maintained**
- **All 5 chart types supported**
- **Performance optimizations preserved**

**Recommendation**: Use `generate_chart.py` for new development and gradually migrate existing workflows.
