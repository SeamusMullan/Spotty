import typer
from pathlib import Path
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.panel import Panel
from rich import print as rprint
import pandas as pd
import time

app = typer.Typer(help="Spotty - Download your Spotify music from Exportify CSV files")
console = Console()

def main():
    app()


if __name__ == "__main__":
    main()
