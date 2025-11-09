"""
Spotty - A terminal application for downloading songs from Exportify CSV files.

This package provides tools to analyze and process Spotify playlist data
exported using Exportify.
"""

from spotty.cli import main, app
from spotty.utils import (
    read_csv_file,
    calculate_statistics,
    get_top_artists,
    format_duration,
    format_date,
    validate_csv_columns,
    get_unique_values,
)

__version__ = "0.1.0"

__all__ = [
    # CLI
    "main",
    "app",
    # Utilities
    "read_csv_file",
    "calculate_statistics",
    "get_top_artists",
    "format_duration",
    "format_date",
    "validate_csv_columns",
    "get_unique_values",
    # Version
    "__version__",
]
