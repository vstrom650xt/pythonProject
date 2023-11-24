import PyPDF2
from PyPDF2 import PdfReader

if __name__ =='__main__':
    reader = PyPDF2.PdfReader('../python-by-vilar.pdf')
    print(len(reader.pages))
    print(reader.pages[0].extract_text())
    #
    # pdfFileObj = open('../python-by-vilar.pdf')
    # dfReader = PdfReader(pdfFileObj)
    # print(dfReader)
    #

