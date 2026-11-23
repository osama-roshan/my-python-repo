# PDF Merge project in python 


# This python code will merge pdf files in eachother

from pypdf import PdfWriter
import os

merger = PdfWriter()
files = [file for file in os.listdir() if file.endswith(" .pdf")]

for pdf in files:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()