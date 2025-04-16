from PIL import Image, ImageDraw, ImageFont

def generate_cover_image(name):
    img = Image.new('RGB', (600, 800), color = (255, 230, 240))
    d = ImageDraw.Draw(img)
    d.text((100, 350), f"Maman Magique\n{name}", fill=(120, 0, 60))
    path = "/mnt/data/cover_image.png"
    img.save(path)
    return path