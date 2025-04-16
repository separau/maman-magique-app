from fpdf import FPDF

def export_pdf(name, letter, photos, cover_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=16)
    pdf.cell(200, 10, txt="Maman Magique", ln=True, align='C')
    pdf.ln(10)
    pdf.multi_cell(0, 10, letter)
    pdf.image(cover_path, x=10, y=100, w=190)
    pdf_path = "/mnt/data/maman_magique_gift.pdf"
    pdf.output(pdf_path)
    return pdf_path