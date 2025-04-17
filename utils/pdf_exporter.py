from fpdf import FPDF
import os
from PIL import Image

class PDFExporter:
    def __init__(self, output_path="output/memory_book.pdf"):
        self.output_path = output_path
        self.pdf = FPDF()
        self.pdf.set_auto_page_break(auto=True, margin=15)

    def add_cover(self, image_path):
        self.pdf.add_page()
        self.pdf.image(image_path, x=0, y=0, w=210, h=297)

    def add_letter(self, letter_text):
        self.pdf.add_page()
        self.pdf.set_font("Arial", size=12)
        self.pdf.multi_cell(0, 10, letter_text)

    def add_photos(self, photo_paths, captions=None):
        for i, photo_path in enumerate(photo_paths):
            self.pdf.add_page()
            self.pdf.image(photo_path, x=30, y=40, w=150)

            if captions and i < len(captions):
                self.pdf.set_y(200)
                self.pdf.set_font("Arial", size=11)
                self.pdf.multi_cell(0, 10, captions[i])

    def save(self):
        os.makedirs(os.path.dirname(self.output_path), exist_ok=True)
        self.pdf.output(self.output_path)
        return self.output_path

# Exemple d’utilisation :
# pdf = PDFExporter()
# pdf.add_cover("output/cover.jpg")
# pdf.add_letter("Dear Mom, thank you for everything...")
# pdf.add_photos(["photo1.jpg", "photo2.jpg"], ["Caption 1", "Caption 2"])
# pdf.save()

