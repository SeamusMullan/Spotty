"""
Spotty utilities - Helper functions for CSV processing and data manipulation.
"""
from pathlib import Path
from typing import Dict, Any

import pandas as pd


def read_csv_file(csv_file: Path) -> pd.DataFrame:
    """
    Read an Exportify CSV file and return a pandas DataFrame.
    
    Args:
        csv_file: Path to the CSV file
        
    Returns:
        pd.DataFrame: The loaded CSV data
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        pd.errors.EmptyDataError: If the CSV is empty
    """
    if not csv_file.exists():
        raise FileNotFoundError(f"CSV file not found: {csv_file}")
    
    return pd.read_csv(csv_file)


def calculate_statistics(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Calculate statistics from a Spotify CSV DataFrame.
    
    Args:
        df: DataFrame containing Spotify playlist data
        
    Returns:
        Dict containing:
            - total_songs: Number of songs
            - total_hours: Total duration in hours
            - unique_artists: Number of unique artists
            - unique_albums: Number of unique albums
    """
    total_songs = len(df)
    total_duration_ms = df['Duration (ms)'].sum() if 'Duration (ms)' in df.columns else 0
    total_hours = total_duration_ms / (1000 * 60 * 60)
    
    unique_artists = df['Artist Name(s)'].nunique() if 'Artist Name(s)' in df.columns else 0
    unique_albums = df['Album Name'].nunique() if 'Album Name' in df.columns else 0
    
    return {
        'total_songs': total_songs,
        'total_hours': total_hours,
        'unique_artists': unique_artists,
        'unique_albums': unique_albums,
    }


def get_top_artists(df: pd.DataFrame, limit: int = 5) -> pd.Series:
    """
    Get the top N artists by song count.
    
    Args:
        df: DataFrame containing Spotify playlist data
        limit: Number of top artists to return
        
    Returns:
        pd.Series: Artist names and their song counts
    """
    if 'Artist Name(s)' not in df.columns:
        return pd.Series(dtype=object)
    
    return df['Artist Name(s)'].value_counts().head(limit)


def format_duration(duration_ms: Any) -> str:
    """
    Format duration from milliseconds to MM:SS format.
    
    Args:
        duration_ms: Duration in milliseconds (or None/NaN)
        
    Returns:
        str: Formatted duration string (e.g., "3:45")
    """
    if pd.isna(duration_ms) or duration_ms is None:
        return "0:00"
    
    try:
        duration_ms = int(duration_ms)
        minutes = duration_ms // 60000
        seconds = (duration_ms % 60000) // 1000
        return f"{minutes}:{seconds:02d}"
    except (ValueError, TypeError):
        return "0:00"


def format_date(date_str: Any) -> str:
    """
    Format date string to YYYY-MM-DD format.
    
    Args:
        date_str: Date string (or None/NaN)
        
    Returns:
        str: Formatted date string or 'N/A'
    """
    if pd.isna(date_str) or date_str is None:
        return 'N/A'
    
    try:
        return str(date_str)[:10]
    except Exception:
        return 'N/A'


def validate_csv_columns(df: pd.DataFrame) -> bool:
    """
    Validate that the DataFrame has the expected Exportify columns.
    
    Args:
        df: DataFrame to validate
        
    Returns:
        bool: True if all required columns are present
    """
    required_columns = {
        'Track Name',
        'Artist Name(s)',
        'Album Name',
        'Duration (ms)',
    }
    
    return required_columns.issubset(df.columns)


def get_unique_values(df: pd.DataFrame, column: str) -> list:
    """
    Get unique values from a DataFrame column.
    
    Args:
        df: DataFrame to query
        column: Column name
        
    Returns:
        list: Unique values from the column
    """
    if column not in df.columns:
        return []
    
    return df[column].dropna().unique().tolist()
