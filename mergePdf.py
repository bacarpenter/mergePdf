#!/usr/local/bin/python3

    ##################################################
    #                                                #
    # This code is based on the instagram            #
    # post: https://www.instagram.com/p/CKBjz19gOZC/ #
    #                                                #
    ##################################################

from PyPDF2 import PdfFileReader, PdfFileMerger
from rich import print
OUTPUT_DIR = "/Users/bencarpenter/Documents"

# Welcome:
print("[bold green]PDF File Merger[/bold green] | Ben Carpenter, 2021\n-------------------------------------")

numOfFiles = int(input("How many files would you like to combine? "))
i = 1
PDFfiles = []
while i < numOfFiles + 1:
    path = input(f"Path of #{i}: ").replace("\\", "").strip()
    try:
        PDFfiles.append(PdfFileReader(path))
    except FileNotFoundError:
        print("[bold red]Error. File not found. Is the path correct?[/bold red]")
        i -= 1

    i += 1

outFileName = input("Merged File Name (w/o '.pdf'!): ")#.replace(" ", "\\ ").strip()

output = PdfFileMerger()
for file in PDFfiles:
    output.append(file)

output.write(f"{OUTPUT_DIR}/{outFileName}.pdf")

print(f"Megred File: [magenta]{OUTPUT_DIR}/{outFileName}.pdf[/magenta]\n-------------------------------------")
