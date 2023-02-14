from pikepdf import Pdf, PdfImage

file = Pdf.open("Image_Extractor/spdf.pdf")

page = file.pages[0]
print(list(page.Images.keys()))

# raw = page.images['/Images']
# pdf_image = PdfImage(raw)
# pdf_image.extract_to(fileprefix = "t1")