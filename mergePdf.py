
    ##################################################
    #                                                #
    # This code is based on the instagram            #
    # post: https://www.instagram.com/p/CKBjz19gOZC/ #
    #                                                #
    ##################################################

from PyPDF2 import PdfFileReader, PdfFileMerger
OUTPUT_DIR = "/Users/bencarpenter/Documents"


def combinePDF(path1, path2, mergeName):
    """
    Combine the two files into one PDF with PyPDF.
    """

    file1 = PdfFileReader(path1.replace("\\", ""))
    file2 = PdfFileReader(path2.replace("\\", ""))

    output = PdfFileMerger()
    output.append(file1)
    output.append(file2)

    output.write(f'{OUTPUT_DIR}/{mergeName}.pdf')
    return output


def main():
    """
    Main function
    """
    print("PDF File Merger | Combine two files!\n------------------------------------")
    path1 = input("Path of first file: ")
    path2 = input("Path of second file: ")
    outName = input("Merged name: (With out '.pdf'!) ")

    combined = combinePDF(path1, path2, outName)

    if combined:
        print(
            f"Combined file path: {OUTPUT_DIR}/{outName}.pdf\n------------------------------------")

    else:
        print("error!")


main()
