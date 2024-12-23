from PyPDF2 import PdfWriter, PdfReader
from reportlab.pdfgen import canvas
from reportlab.lib.colors import orange
from reportlab.lib.pagesizes import A4
from io import BytesIO
import os

def modify_pdf(filename, cpf, position,color,upload_folder, Nome):
    packet = BytesIO()
    can = canvas.Canvas(packet, pagesize=A4)

    if position == 'top-left':
        x= 20
        y = 800
    elif position == 'top-right':
        x = 350
        y = 800
    elif position == 'bottom-left':
        x = 50
        y = 50
    elif position == 'bottom-right':
        x = 350
        y = 50
    else:
        raise ValueError("posição inválida")

    print(f"Desenho do CPF na posição: {x}, {y}")

    can.setFillColor(color)
    can.setFont("Helvetica", 10)
    name = f"{Nome} do CPF {cpf}"
    can.drawString(x,y,name) 
    can.save()     

    try:
        packet.seek(0)
        new_pdf = PdfReader(packet)
        print("PDF foi criado com sucesso")
    except Exception as e:
        print("Erro ao criar o PDF" + str(e))

    try:
        existing_pdf = PdfReader(open(os.path.join(upload_folder,filename), "rb"))
        print("sucesso ao abrir o PDF")
        output = PdfWriter()
        print(f"Números de páginas no PDF é:{len(existing_pdf.pages)}")    
        for i in range(len(existing_pdf.pages)):
            page = existing_pdf.pages[i]
            page.merge_page(new_pdf.pages[0])
            output.add_page(page)

        with open(os.path.join(upload_folder,filename),"wb") as outputStream:
            output.write(outputStream)
        print(f"pdf foi modificado com sucesso: {os.path.join(upload_folder,filename)}")
    except Exception as e:
        print("Erro ao abrir o PDF Gerado" + str(e))    
