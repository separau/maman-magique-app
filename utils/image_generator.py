from PIL import Image, ImageDraw, ImageFont
import os

def generate_cover_image(name="Mom", style="watercolor", output_path="output/cover.jpg"):
    """
    Generates a simple artistic-style cover image for the souvenir book.

    :param name: Name to display on the cover.
    :param style: Style of the cover (placeholder for now).
    :param output_path: Output path for the image.
    :return: Path to the saved cover image.
    """
    width, height = 800, 1200
    img = Image.new('RGB', (width, height), color=(255, 230, 240))

    draw = ImageDraw.Draw(img)

    # Load a font
    try:
        font = ImageFont.truetype("arial.ttf", 60)
    except:
        font = ImageFont.load_default()

    text = f"For {name}"
    text_width, text_height = draw.textsize(text, font=font)
    draw.text(
        ((width - text_width) / 2, height / 2 - text_height),
        text,
        fill=(120, 30, 50),
        font=font
    )

    subtitle = "A Magical Mother's Day Book"
    sub_width, sub_height = draw.textsize(subtitle, font=font)
    draw.text(
        ((width - sub_width) / 2, height / 2 + 50),
        subtitle,
        fill=(100, 20, 40),
        font=font
    )

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path)
    return output_path

# Example usage:
# generate_cover_image(name="Sophie", style="watercolor", output_path="output/cover.jpg")

