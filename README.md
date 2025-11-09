# Spotty

A terminal application for downloading songs from Exportify.

(In early development, don't expect everything to work)

## Features

- **Clean TUI**: Built with Rich for a pretty damn cool terminal experience
- **Tables n' stuff**: Displays songs in formatted tables
- **Statistics**: See how cooked you are (show who you listen to the most)

## Coming Soon (hopefully)

- **Music Downloading**: Download your songs for listening offline
- **Desktop App**: No promises, but wouldn't it be awesome, wouldn't it be so cool
- **FastAPI Integration**: So you cracked programmers can implement this in a site or app

## Installation

```bash
# Clone the repository
git clone https://github.com/SeamusMullan/Spotty.git
cd Spotty

# Install the package
make install

# Or install with development dependencies
make dev-install
```

## How to Use

Once installed, you can use `spotty` from anywhere in your terminal:

### List Songs

Display songs from your Exportify CSV in a table:

```bash
spotty list <your_file_name.csv> --limit <max_num_rows>

# Example
spotty list exportify-csv-files/Liked_Songs.csv --limit 50
```

### Show Info

Get statistics about your music library:

```bash
spotty info <your_file_name.csv>

# Example
spotty info exportify-csv-files/muzak.csv
```

### Download (Coming Soon)

```bash
spotty download <your_file_name.csv> --output ./downloads
```

### Show Version

```bash
spotty version
```

### Get Help

```bash
spotty --help
```

## Using as a Python Package

You can also import and use Spotty's functionality in your own Python code:

```python
from spotty import read_csv_file, calculate_statistics, get_top_artists

# Read a CSV file
df = read_csv_file("path/to/your/file.csv")

# Get statistics
stats = calculate_statistics(df)
print(f"Total songs: {stats['total_songs']}")
print(f"Total hours: {stats['total_hours']:.1f}")

# Get top artists
top_artists = get_top_artists(df, limit=10)
print(top_artists)
```

## Project Structure

```text
Spotty/
├── spotty/              # Main package directory
│   ├── __init__.py      # Package initialization and exports
│   ├── cli.py           # CLI commands and interface
│   └── utils.py         # Utility functions for data processing
├── main.py              # Entry point for direct execution
├── pyproject.toml       # Package configuration and dependencies
└── README.md            # This file
```

## Contributing

Just make a PR, I need as much help as I can get!

### Development Workflow

1. **Install development dependencies:**

   ```bash
   make dev-install
   ```

2. **Auto-fix code before committing:**

   ```bash
   make format
   ```

   This runs Black and Ruff to automatically format and fix common issues.

3. **Check for remaining issues:**

   ```bash
   make lint
   ```

4. **Optional: Set up pre-commit hooks** (auto-fixes on every commit):

   ```bash
   make pre-commit-install
   ```

5. **See all available commands:**

   ```bash
   make help
   ```

See [CODE_QUALITY.md](CODE_QUALITY.md) for detailed information about code quality tools.

## License

MIT
