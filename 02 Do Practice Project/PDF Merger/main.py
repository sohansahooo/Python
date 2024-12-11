import PyPDF2 as pdf
from PyPDF2 import PdfMerger

# Create a PdfMerger object
merger = PdfMerger()

# List of PDF files to merge
pdf_files = ["file1.pdf", "file2.pdf", "file3.pdf"]

# Iterate through the PDF files and append them
for file in pdf_files:
    merger.append(file)

# Write the merged PDF to a new file
merger.write("merged-pdf.pdf")
merger.close()

print("PDF files merged successfully into merged-pdf.pdf")
