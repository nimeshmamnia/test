import os
from PyPDF2 import PdfMerger

os.chdir("C:\\Dropbox\\Python")
merger = PdfMerger()

for files in os.listdir("C:\\Dropbox\\Python"):
    if files.endswith('.pdf'):
        merger.append(files)

merger.write("combined2.pdf")
merger.close()