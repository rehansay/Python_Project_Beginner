import PyPDF2
import os


current_dir = os.path.dirname(__file__)


pdfiles = [
    os.path.join(current_dir, "sample1.pdf"),
    os.path.join(current_dir, "sample2.pdf"),
    os.path.join(current_dir, "sample3.pdf")
]

merger=PyPDF2.PdfMerger()

for filename in pdfiles:
    pdfFile=open(filename, 'rb')

    pdfReader=PyPDF2.PdfReader(pdfFile)

    merger.append(pdfReader)

pdfFile.close()
merger.write('merged.pdf')



