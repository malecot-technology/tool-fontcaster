# Fontcaster

**Fontcaster** is a command-line tool that renders a sample text across multiple font weights and
outputs the result as a PNG image. It's a simple and effective way to preview how a typeface looks
from Thin to Black.

Ideal for typographers, designers, and frontend developers who want to quickly audit font weight
ranges.

## Features

- Renders text across 9 font weights (Thin to Black).
- Customizable text string, font size, text color, and background color.
- Outputs to a PNG image.
- Uses Pango + Cairo for accurate font rendering.

## Requirements

- Python 3.9+
- [pycairo](https://pycairo.readthedocs.io/en/latest/)
- PyGObject bindings (`gi`, with Pango and PangoCairo)

## Usage

```bash
./fontcaster.py <font> [--text TEXT] [--font-size SIZE] [--text-color HEX] [--bg-color HEX] [-o OUTPUT]
```

### Arguments

- `<font>`: Font family name (e.g. `Roboto`, `Fira Sans`, `Arial`).
- `--text`: Text to render (optional; defaults to weight name like "Thin", "Bold", etc.).
- `--font-size`: Font size in points (default: `36.0`).
- `--text-color`: Hexadecimal text color (default: `#000000`).
- `--bg-color`: Hexadecimal background color (default: `#FFFFFF`).
- `-o`, `--output`: Output PNG file name (default: `output.png`).

### Example

```bash
./fontcaster.py "Roboto" --text "The quick brown fox" --font-size 32 --text-color "#222222" --bg-color "#FAFAFA" -o roboto.png
```

## Notes

- The specified font must be installed and accessible via Pango (check with `fc-list` on Linux).
- Color codes must be valid 6-digit hexadecimal strings starting with `#`.
- Each weight is rendered on a separate line, evenly spaced.

## License

This project is licensed under either of:

* [Apache License, Version 2.0](LICENSE-APACHE)
* [MIT license](LICENSE-MIT)
