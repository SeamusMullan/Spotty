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

# Install dependencies (requires uv)
uv sync
```

## How to Use

### List Songs

Display songs from your Exportify CSV in a table:

```bash
uv run python main.py list <your_file_name> --limit <max_num_rows>
```

### Show Info

Get statistics about your music library:

```bash
uv run python main.py info <your_file_name>
```

### Show Version

```bash
uv run python main.py version
```

### Get Help

```bash
uv run python main.py --help
```

## Contributing

Just make a PR, I need as much help as I can get!
