#! python3
# combinePdfs.py - Combinese all the PDFs in the current working directory
# into a single PDF.

import PyPDF2, os
from tkinter import filedialog
from tkinter import *

root = Tk()
root.withdraw
root.directory =  filedialog.askdirectory()
print (root.directory)
os.chdir(root.directory)

# Get all the PDF filenames.
pdfFiles = []
for filename in os.listdir(root.directory):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key=str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

# Loop through all the PDF files.
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    # Loop through all pages (except the first) and add them.
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

# Save the resulting PDF to a file.
pdfOutput = open('Combined.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()