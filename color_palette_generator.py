import colorsys
import webcolors

def rgb_to_hsl(rgb):
    return colorsys.rgb_to_hls(rgb[0] / 255.0, rgb[1] / 255.0, rgb[2] / 255.0)

def hsl_to_rgb(hsl):
    rgb = colorsys.hls_to_rgb(hsl[0], hsl[1], hsl[2])
    return (int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255))

def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])

def complementary_color(rgb):
    return (255 - rgb[0], 255 - rgb[1], 255 - rgb[2])

def triadic_colors(rgb):
    h, l, s = rgb_to_hsl(rgb)
    return [hsl_to_rgb(((h + 1 / 3) % 1.0, l, s)), hsl_to_rgb(((h + 2 / 3) % 1.0, l, s))]

def analogous_colors(rgb):
    h, l, s = rgb_to_hsl(rgb)
    return [hsl_to_rgb(((h + 1 / 12) % 1.0, l, s)), hsl_to_rgb(((h - 1 / 12) % 1.0, l, s))]

def adjust_brightness(rgb, factor):
    h, l, s = rgb_to_hsl(rgb)
    new_lightness = max(0, min(1, l * factor))
    return hsl_to_rgb((h, new_lightness, s))

def generate_dark_palette_from_light(light_palette):
    dark_palette = {}
    for key, color in light_palette.items():
        rgb = webcolors.hex_to_rgb(color)
        if key in ["Primary", "Success"]:
            dark_palette[key] = rgb_to_hex(adjust_brightness(rgb, 0.7))
        elif key in ["Primary Text", "Secondary Text"]:
            dark_palette[key] = rgb_to_hex(adjust_brightness(rgb, 1.5))
        elif key in ["Primary Background", "Secondary Background"]:
            dark_palette[key] = rgb_to_hex(adjust_brightness(rgb, 0.3))
        else:
            dark_palette[key] = rgb_to_hex(adjust_brightness(rgb, 0.8))
    return dark_palette

def generate_color_palette(base_rgb):
    comp_color = complementary_color(base_rgb)
    triad = triadic_colors(base_rgb)
    analog = analogous_colors(base_rgb)

    light_palette = {
        "Primary": rgb_to_hex(base_rgb),
        "Secondary": rgb_to_hex(adjust_brightness(base_rgb, 1.3)),
        "Tertiary": rgb_to_hex(adjust_brightness(base_rgb, 1.6)),
        "Alternate": rgb_to_hex(triad[0]),
        "Primary Text": rgb_to_hex(adjust_brightness((0, 0, 0), 0.2)),
        "Secondary Text": rgb_to_hex(adjust_brightness((128, 128, 128), 1.1)),
        "Primary Background": rgb_to_hex(adjust_brightness((240, 240, 240), 1.0)),
        "Secondary Background": rgb_to_hex(adjust_brightness((220, 220, 220), 1.0)),
        "Accent 1": rgb_to_hex(analog[0]),
        "Accent 2": rgb_to_hex(triad[1]),
        "Accent 3": rgb_to_hex(adjust_brightness(base_rgb, 0.9)),
        "Accent 4": rgb_to_hex(comp_color),
        "Success": rgb_to_hex(base_rgb),
        "Error": rgb_to_hex((255, 51, 51)),
        "Warning": rgb_to_hex((255, 153, 51)),
        "Info": rgb_to_hex((51, 204, 255))
    }

    dark_palette = generate_dark_palette_from_light(light_palette)

    custom_colors = {
        "Shadow": rgb_to_hex(adjust_brightness(base_rgb, 0.4)),
        "Highlight": rgb_to_hex(adjust_brightness(base_rgb, 1.5)),
        "Disabled": rgb_to_hex(adjust_brightness(base_rgb, 0.3)),
        "Border": rgb_to_hex(adjust_brightness(base_rgb, 0.6)),
        "Gradient Start": rgb_to_hex(base_rgb)
    }

    return light_palette, dark_palette, custom_colors

def print_palette(title, palette):
    print(f"=== {title} ===")
    for name, color in palette.items():
        print(f"{name}: {color}")

# Base Color Input
base_color_hex = input("Enter the primary color in HEX format (e.g., #53B175): ").strip()
base_color_rgb = webcolors.hex_to_rgb(base_color_hex)

# Generate and Print Palettes
light_palette, dark_palette, custom_colors = generate_color_palette(base_color_rgb)
print_palette("Light Theme Palette", light_palette)
print_palette("Dark Theme Palette", dark_palette)
print_palette("Custom Colors for Mobile App", custom_colors)
