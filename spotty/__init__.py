"""
Spotty - A terminal application for downloading songs from Exportify CSV files.

This package provides tools to analyze and process Spotify playlist data
exported using Exportify.
"""

from spotty.cli import app, main
from spotty.utils import (
    calculate_statistics,
    format_date,
    format_duration,
    get_top_artists,
    get_unique_values,
    read_csv_file,
    validate_csv_columns,
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
