#!/usr/bin/env python3
import argparse
import cairo
import gi
import re

gi.require_version("Pango", "1.0")
gi.require_version("PangoCairo", "1.0")

from gi.repository import Pango, PangoCairo

WEIGHTS = [
    (100, "Thin"),
    (200, "Extra Light"),
    (300, "Light"),
    (400, "Regular"),
    (500, "Medium"),
    (600, "Semi Bold"),
    (700, "Bold"),
    (800, "Extra Bold"),
    (900, "Black"),
]


def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    if len(hex_color) != 6 or not re.fullmatch(r"[0-9a-fA-F]{6}", hex_color):
        raise ValueError(f"Invalid color code: {hex_color}")
    r, g, b = tuple(int(hex_color[i : i + 2], 16) / 255.0 for i in (0, 2, 4))
    return r, g, b


def render_variants_to_png(
    font_family, text, font_size, output_file, text_color, bg_color
):
    padding = 10
    line_spacing = int(font_size * 1.5)
    max_text_width = 0
    height_needed = padding * 2 + line_spacing * len(WEIGHTS)
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 0, height_needed)
    ctx = cairo.Context(surface)
    layout = PangoCairo.create_layout(ctx)
    for weight, name in WEIGHTS:
        desc = Pango.FontDescription(f"{font_family} {int(font_size)}")
        desc.set_weight(weight)
        layout.set_font_description(desc)
        if text:
            layout.set_text(text, -1)
        else:
            layout.set_text(name, -1)
        ink_rect, logical_rect = layout.get_pixel_extents()
        max_text_width = max(max_text_width, logical_rect.width)
    width = max_text_width + padding * 2
    height = height_needed
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    ctx = cairo.Context(surface)
    ctx.set_source_rgb(*bg_color)
    ctx.paint()
    layout = PangoCairo.create_layout(ctx)
    for index, (weight, name) in enumerate(WEIGHTS):
        desc = Pango.FontDescription(f"{font_family} {int(font_size)}")
        desc.set_weight(weight)
        layout.set_font_description(desc)
        if text:
            layout.set_text(text, -1)
        else:
            layout.set_text(name, -1)
        x = padding
        y = padding + index * line_spacing
        ctx.move_to(x, y)
        ctx.set_source_rgb(*text_color)
        PangoCairo.show_layout(ctx, layout)
    surface.write_to_png(output_file)


def main():
    parser = argparse.ArgumentParser(
        description="Render text at multiple font weights."
    )
    parser.add_argument("font", help="Font family name (e.g., 'Roboto')")
    parser.add_argument("--text", help="Text to render")
    parser.add_argument(
        "--font-size", type=float, default=36.0, help="Font size in points"
    )
    parser.add_argument(
        "-o", "--output", default="output.png", help="Output PNG file name"
    )
    parser.add_argument(
        "--text-color",
        default="#000000",
        help="Text color in hex format (e.g., #000000)",
    )
    parser.add_argument(
        "--bg-color",
        default="#FFFFFF",
        help="Background color in hex format (e.g., #FFFFFF)",
    )
    args = parser.parse_args()
    try:
        text_color = hex_to_rgb(args.text_color)
        bg_color = hex_to_rgb(args.bg_color)
    except ValueError as err:
        parser.error(str(err))
    render_variants_to_png(
        args.font, args.text, args.font_size, args.output, text_color, bg_color
    )


if __name__ == "__main__":
    main()
