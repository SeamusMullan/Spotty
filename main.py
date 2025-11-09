"""
Spotty - A terminal application for downloading songs from Exportify CSV files.
"""
import time
from pathlib import Path

import pandas as pd
import typer
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table

app = typer.Typer(
    help="Spotty - Download your Spotify music from Exportify CSV files"
)
console = Console()


@app.command()
def list_songs(
    csv_file: Path = typer.Argument(..., help="Path to Exportify CSV file"),
    limit: int = typer.Option(
        20, "--limit", "-l", help="Number of songs to display"
    ),
):
    """
    Display songs from an Exportify CSV file in a beautiful table.
    """
    if not csv_file.exists():
        console.print(
            f"[bold red]Error:[/bold red] File '{csv_file}' not found!"
        )
        raise typer.Exit(1)

    try:
        console.print(
            f"\n[bold cyan]Reading:[/bold cyan] {csv_file.name}\n"
        )
        df = pd.read_csv(csv_file)

        # Show file stats
        stats_panel = Panel(
            f"[bold]Total Songs:[/bold] {len(df)}\n"
            f"[bold]Displaying:[/bold] {min(limit, len(df))} songs",
            title="Statistics",
            border_style="cyan"
        )
        console.print(stats_panel)
        console.print()

        # Create table
        table = Table(
            title=f"Songs from {csv_file.name}", show_lines=False
        )
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
            duration_col = 'Duration (ms)'
            duration_ms = row[duration_col] if (
                duration_col in row and pd.notna(row[duration_col])
            ) else 0
            minutes = int(duration_ms / 60000)
            seconds = int((duration_ms % 60000) / 1000)
            duration_str = f"{minutes}:{seconds:02d}"

            added_at_col = 'Added At'
            added_at = row[added_at_col] if (
                added_at_col in row and pd.notna(row[added_at_col])
            ) else None
            added_date = str(added_at)[:10] if added_at else 'N/A'

            track_col = 'Track Name'
            track_name = row[track_col] if (
                track_col in row and pd.notna(row[track_col])
            ) else 'Unknown'

            artist_col = 'Artist Name(s)'
            artist_name = row[artist_col] if (
                artist_col in row and pd.notna(row[artist_col])
            ) else 'Unknown'

            album_col = 'Album Name'
            album_name = row[album_col] if (
                album_col in row and pd.notna(row[album_col])
            ) else 'Unknown'

            table.add_row(
                str(idx + 1),
                str(track_name)[:40],
                str(artist_name)[:30],
                str(album_name)[:30],
                duration_str,
                added_date
            )

        console.print(table)
        console.print()

    except Exception as e:
        console.print(f"[bold red]Error reading CSV:[/bold red] {e}")
        raise typer.Exit(1) from e


@app.command()
def info(
    csv_file: Path = typer.Argument(..., help="Path to Exportify CSV file")
):
    """
    Show detailed information about the CSV file.
    """
    if not csv_file.exists():
        console.print(
            f"[bold red]Error:[/bold red] File '{csv_file}' not found!"
        )
        raise typer.Exit(1)

    try:
        df = pd.read_csv(csv_file)

        # Calculate statistics
        total_songs = len(df)
        total_duration_ms = df['Duration (ms)'].sum()
        total_hours = total_duration_ms / (1000 * 60 * 60)

        # Get unique values
        unique_artists = df['Artist Name(s)'].nunique()
        unique_albums = df['Album Name'].nunique()

        # Get top artists
        top_artists = df['Artist Name(s)'].value_counts().head(5)

        # Display info
        info_text = (
            f"[bold]File:[/bold] {csv_file.name}\n"
            f"[bold]Total Songs:[/bold] {total_songs}\n"
            f"[bold]Total Duration:[/bold] {total_hours:.1f} hours\n"
            f"[bold]Unique Artists:[/bold] {unique_artists}\n"
            f"[bold]Unique Albums:[/bold] {unique_albums}\n"
        )

        panel = Panel(
            info_text, title=" File Information", border_style="green"
        )
        console.print(panel)
        console.print()

        # Top artists table
        artists_table = Table(title=" Top 5 Artists", show_lines=False)
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
        "./downloads", "--output", "-o",
        help="Output directory for downloads"
    ),
):
    """
    Download songs from the CSV file (placeholder - not yet implemented).
    """
    if not csv_file.exists():
        console.print(
            f"[bold red]Error:[/bold red] File '{csv_file}' not found!"
        )
        raise typer.Exit(1)

    try:
        df = pd.read_csv(csv_file)
        total_songs = len(df)

        console.print(
            "\n[bold yellow]  Download functionality coming soon!"
            "[/bold yellow]\n"
        )
        console.print(
            f"Would download {total_songs} songs to: "
            f"{output_dir.absolute()}\n"
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

        console.print("\n[green][/green] Demo complete!\n")

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
