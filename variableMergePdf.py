
    ##################################################
    #                                                #
    # This code is based on the instagram            #
    # post: https://www.instagram.com/p/CKBjz19gOZC/ #
    #                                                #
    ##################################################

from PyPDF2 import PdfFileReader, PdfFileMerger
OUTPUT_DIR = "/Users/bencarpenter/Documents"

# Welcome:
print("PDF File Merger | Combine many files!\n-------------------------------------")

numOfFiles = int(input("How many files would you like to combine? "))
i = 1
PDFfiles = []
while i < numOfFiles + 1:
    path = input(f"Path of #{i}: ").replace("\\", "").strip()
    PDFfiles.append(PdfFileReader(path))
    i += 1

outFileName = input("Merged File Name (w/o '.pdf'!): ")#.replace(" ", "\\ ").strip()

output = PdfFileMerger()
for file in PDFfiles:
    output.append(file)

output.write(f"{OUTPUT_DIR}/{outFileName}.pdf")

print(f"Megred File: {OUTPUT_DIR}/{outFileName}.pdf\n-------------------------------------")
