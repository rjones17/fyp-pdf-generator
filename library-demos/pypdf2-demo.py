from PyPDF2 import PdfFileReader, PdfFileWriter

# with open('Google.html', 'r') as file:    # Cannot pass in a string to the Reader
#     data = file.read()

# input = PdfFileReader(open('Google.html', 'rb')) # Will not work, cannot read html stream

input = PdfFileReader(open("pypdf2-test.pdf", 'rb'))
output = PdfFileWriter()

print("input has %d pages" % input.getNumPages())
