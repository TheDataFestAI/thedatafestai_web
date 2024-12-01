# import os
# from pathlib import Path
from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import letter

a4_page_size = (595.27, 841.89)

def generate_pdf(file_name, content):
    file_name = "./assets/temp_dumps/" + file_name
    c = canvas.Canvas(file_name, pagesize=a4_page_size)
    c.drawString(50, 780, content)
    c.showPage()
    c.save()
    # out_file_path = os.path.abspath(file_name)
    return file_name
    
if __name__ == "__main__":
    generate_pdf(file_name="sample.pdf", content="Sample Word")