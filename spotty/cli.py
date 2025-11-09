"""
Spotty CLI - Command-line interface for Spotty.
"""

import time
from pathlib import Path

import typer
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table

from spotty.utils import (
    read_csv_file,
    calculate_statistics,
    get_top_artists,
    format_duration,
    format_date,
)

app = typer.Typer(help="Spotty - Download your Spotify music from Exportify CSV files")
console = Console()


@app.command()
def list_songs(
    csv_file: Path = typer.Argument(..., help="Path to Exportify CSV file"),
    limit: int = typer.Option(20, "--limit", "-l", help="Number of songs to display"),
):
    """
    Display songs from an Exportify CSV file in a beautiful table.
    """
    if not csv_file.exists():
        console.print(f"[bold red]Error:[/bold red] File '{csv_file}' not found!")
        raise typer.Exit(1)

    try:
        console.print(f"\n[bold cyan]Reading:[/bold cyan] {csv_file.name}\n")
        df = read_csv_file(csv_file)

        # Show file stats
        stats_panel = Panel(
            f"[bold]Total Songs:[/bold] {len(df)}\n"
            f"[bold]Displaying:[/bold] {min(limit, len(df))} songs",
            title="Statistics",
            border_style="cyan",
        )
        console.print(stats_panel)
        console.print()

        # Create table
        table = Table(title=f"Songs from {csv_file.name}", show_lines=False)
        table.add_column("#", style="dim", width=4)
        table.add_column("Track", style="cyan", no_wrap=True)
        table.add_column("Artist", style="magenta")
        table.add_column("Album", style="green")
        table.add_column("Duration", style="yellow", justify="right")
        table.add_column("Added", style="blue")

        # Add rows
        df_display = df.head(limit)
        for idx in range(len(df_display)):
            row = df_display.iloc[idx]

            duration_str = format_duration(row.get("Duration (ms)"))
            added_date = format_date(row.get("Added At"))

            track_name = row.get("Track Name", "Unknown")
            artist_name = row.get("Artist Name(s)", "Unknown")
            album_name = row.get("Album Name", "Unknown")

            table.add_row(
                str(idx + 1),
                str(track_name)[:40],
                str(artist_name)[:30],
                str(album_name)[:30],
                duration_str,
                added_date,
            )

        console.print(table)
        console.print()

    except Exception as e:
        console.print(f"[bold red]Error reading CSV:[/bold red] {e}")
        raise typer.Exit(1) from e


@app.command()
def info(csv_file: Path = typer.Argument(..., help="Path to Exportify CSV file")):
    """
    Show detailed information about the CSV file.
    """
    if not csv_file.exists():
        console.print(f"[bold red]Error:[/bold red] File '{csv_file}' not found!")
        raise typer.Exit(1)

    try:
        df = read_csv_file(csv_file)
        stats = calculate_statistics(df)
        top_artists = get_top_artists(df, limit=5)

        # Display info
        info_text = (
            f"[bold]File:[/bold] {csv_file.name}\n"
            f"[bold]Total Songs:[/bold] {stats['total_songs']}\n"
            f"[bold]Total Duration:[/bold] {stats['total_hours']:.1f} hours\n"
            f"[bold]Unique Artists:[/bold] {stats['unique_artists']}\n"
            f"[bold]Unique Albums:[/bold] {stats['unique_albums']}\n"
        )

        panel = Panel(info_text, title="📊 File Information", border_style="green")
        console.print(panel)
        console.print()

        # Top artists table
        artists_table = Table(title="🎵 Top 5 Artists", show_lines=False)
        artists_table.add_column("Rank", style="cyan", width=6)
        artists_table.add_column("Artist", style="magenta")
        artists_table.add_column("Songs", style="green", justify="right")

        for idx, (artist, count) in enumerate(top_artists.items(), 1):
            artists_table.add_row(str(idx), str(artist)[:50], str(count))

        console.print(artists_table)
        console.print()

    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        raise typer.Exit(1) from e


@app.command()
def download(
    csv_file: Path = typer.Argument(..., help="Path to Exportify CSV file"),
    output_dir: Path = typer.Option(
        "./downloads", "--output", "-o", help="Output directory for downloads"
    ),
):
    """
    Download songs from the CSV file (placeholder - not yet implemented).
    """
    if not csv_file.exists():
        console.print(f"[bold red]Error:[/bold red] File '{csv_file}' not found!")
        raise typer.Exit(1)

    try:
        df = read_csv_file(csv_file)
        total_songs = len(df)

        console.print(
            "\n[bold yellow]⚠️  Download functionality coming soon!" "[/bold yellow]\n"
        )
        console.print(
            f"Would download {total_songs} songs to: " f"{output_dir.absolute()}\n"
        )

        # Demo progress bar
        console.print("[dim]Demo of future download progress:[/dim]\n")

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            task = progress.add_task("[cyan]Downloading songs...", total=5)

            for _ in range(5):
                time.sleep(0.3)
                progress.update(task, advance=1)

        console.print("\n[green]✓[/green] Demo complete!\n")

    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        raise typer.Exit(1) from e


@app.command()
def version():
    """
    Show the version of Spotty.
    """
    version_text = (
        "[bold cyan]Spotty[/bold cyan] [dim]v0.1.0[/dim]\n"
        "A terminal app for downloading songs from Exportify CSV files.\n"
        "\n"
        "[dim]Made with <3 and Python[/dim]"
    )
    panel = Panel(version_text, border_style="cyan")
    console.print(panel)


def main():
    """Run the Spotty CLI application."""
    app()


if __name__ == "__main__":
    main()
