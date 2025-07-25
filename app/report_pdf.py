from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4


def generate_pdf(text_boxes, output_path):
    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4
    for item in text_boxes:
        text = item.get("text")
        x, y, w, h = item.get("bbox", [0, 0, 0, 0])
        c.setFont("Helvetica", 12)
        c.drawString(x, height - y, text)
    c.save()
