
from fpdf import FPDF
from PIL import Image
import os

class MemoryBookPDF(FPDF):
    def __init__(self, title="Maman Magique"):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=15)
        self.add_font("Arial", "", "arial.ttf", uni=True)
        self.set_title(title)

    def add_cover(self, cover_image_path, title):
        self.add_page()
        if os.path.exists(cover_image_path):
            self.image(cover_image_path, x=10, y=20, w=190)
        self.set_font("Arial", "B", 24)
        self.set_text_color(255, 105, 180)
        self.cell(0, 200, title, align="C")

    def add_letter(self, letter_text):
        self.add_page()
        self.set_font("Arial", "", 14)
        self.set_text_color(50, 50, 50)
        self.multi_cell(0, 10, letter_text)

    def add_photo_page(self, image_path, caption=""):
        self.add_page()
        if os.path.exists(image_path):
            self.image(image_path, x=15, y=30, w=180)
        if caption:
            self.set_xy(10, 250)
            self.set_font("Arial", "I", 12)
            self.multi_cell(0, 10, caption)

    def export(self, output_path):
        self.output(output_path)

# Example usage:
# pdf = MemoryBookPDF()
# pdf.add_cover("cover.jpg", "To Mom, with Love")
# pdf.add_letter("Dear Mom, ...")
# pdf.add_photo_page("photo1.jpg", "A special moment")
# pdf.export("mom_book.pdf")
