import PyPDF2

with open('pdf/dummy.pdf','rb') as f:
    reader = PyPDF2.PdfFileReader(f)
    page = reader.getPage(0)
    # print(reader.numPages)
    page.rotateClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    
    with open('pdf/tilt.pdf', 'wb') as file:
        writer.write(file)
