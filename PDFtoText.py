##PYTHON SCRIPT TO CONVERT PDF TO TEXT FILE##


#http://stackoverflow.com/questions/5725278/python-help-using-pdfminer-as-a-library
##MAKE SURE YOU HAVE THE PDFMINER CLASS INSTALLED##
import os
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO

 

 ##FUNCTION THAT CONVERTS A SINGLE PDF DOC TO A SINGLE TEXT DOC##
 ##TAKES IN A FILEPATH TO A PDF AND RETURNS A STRING OF TEXT##
def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = file(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)
    fp.close()
    device.close()
    str = retstr.getvalue()
    retstr.close()
    return str

def writePDFToTxt(pdfPath,destPath):
    try:
        pdfToText = convert_pdf_to_txt(pdfPath)
        with open(destPath, "w") as txt_file:
            txt_file.write(pdfToText)
    except Exception, e:
        print "Could not open PDF number "+pdfPath

##CHANGE DIRECTORY TO WHERE THE BITS ARE LOCATED##
wd = "" ##insert working directory
destDir = "" ##insert destination directory
os.chdir(wd)

for pdf in range(3030,3461):
    srcPath = str(pdf)+".pdf"
    destination = destDir+"BIT_"+str(pdf)+".txt"
    writePDFToTxt(srcPath,destination)
