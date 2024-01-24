from docparser import boeing_pdf_converter
import os

# TODO: add a walk function to walk all the pdfs and generate all text files
directory = r"test_cases_boeing\pdfs"
# boeing_pdf_converter(r"M:\docparser\test_cases_boeing\pdfs\test_case1.pdf", r"M:\docparser\test_cases_boeing\textfiles\test_case1.txt")

x = 1
for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)
    boeing_pdf_converter(filepath, fr"test_cases_boeing\textfiles\test_case_{x}.txt")
    x += 1