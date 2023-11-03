import PyPDF2
import pdfReader
from pypdf import PdfReader

if __name__ =='__main__':
    pdfFileObj = open('../python-by-vilar.pdf')
    dfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pdfReader.numPages
    pageObj = pdfReader.getPage(0)
    pageObj.extractText()

