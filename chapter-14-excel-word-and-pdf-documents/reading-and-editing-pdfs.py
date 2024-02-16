import os
import PyPDF2

cwd = f'{os.getcwd()}/chapter-14-excel-word-and-pdf-documents'
pdfFile = open(f'{cwd}/meetingminutes1.pdf', 'rb')
reader = PyPDF2.PdfReader(pdfFile)
# print(len(reader.pages))
# print(reader.pages[1])
# print(reader.pages[1].extract_text())

for pageNum in range(len(reader.pages)):
	print(reader.pages[pageNum].extract_text())

pdfFile.close()

# ===================

pdfFile1 = open(f'{cwd}/meetingminutes1.pdf', 'rb')
pdfFile2 = open(f'{cwd}/meetingminutes2.pdf', 'rb')
reader1 = PyPDF2.PdfReader(pdfFile1)
reader2 = PyPDF2.PdfReader(pdfFile2)

writer = PyPDF2.PdfWriter()
for pageNum in range(len(reader1.pages)):
	page = reader1.pages[pageNum]
	writer.add_page(page)
for pageNum in range(len(reader2.pages)):
	page = reader2.pages[pageNum]
	writer.add_page(page)

outputFile = open(f'{cwd}/combinedminutes.pdf', 'wb')
writer.write(outputFile)

outputFile.close()
pdfFile1.close()
pdfFile2.close()