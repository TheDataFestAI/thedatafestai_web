from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.colors import black, blue, red, darkgrey
from reportlab.lib.pagesizes import letter, A4


a4_page_size = (595.27, 841.89)

def generate_pdf_content_from_list(content, file_name):
    file_path = "./assets/temp_dumps/" + file_name
    c = canvas.Canvas(file_path, pagesize=a4_page_size)
    
    if type(content) == list:
        for i in content:
            c.drawString(50, 780, i)
    else:
         c.drawString(50, 780, content)
    c.showPage()
    c.save()
    
def generate_pdf_content_from_dict(content_dict, file_name):
    file_path = "assets/temp_dumps/" + file_name
    c = canvas.Canvas(file_path, pagesize=A4)
    full_name = content_dict['personal_details']['cv_first_name'] + " " + content_dict['personal_details']['cv_middle_name'] + " " + content_dict['personal_details']['cv_last_name']
    
    # x = 1.8*inch
    # y = 2.7*inch
    x = 1.5*inch
    y = 11*inch
    # c.setFont("Symbol", 10)
    # c.drawString(x,y,"-----------------------------")
    
    for key, val in content_dict['personal_details'].items():
        # print(x,y, key, val)
        if (key == "cv_first_name"):
            c.setFont("Times-Roman", 20)
            c.setFillColor(blue)
            c.drawCentredString(x-10, y, full_name)
        elif (key == "cv_middle_name") or (key == "cv_last_name"):
            continue
        else:   
            c.setFont("Helvetica", 10)
            c.setFillColor(black)
            c.drawString(x,y,val)
            c.drawRightString(x-10,y, key+":")
        y = y-13
    c.showPage()
    c.save()
    # print(f"{file_path} has been created")
    return file_path
    
def hello():
    c = canvas.Canvas("hello.pdf")
    c.drawString(100,100,"Hello World")
    c.showPage()
    c.save()

