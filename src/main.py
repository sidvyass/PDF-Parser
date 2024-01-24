import sys
from docparser import boeing_pdf_converter, get_headers


# CHECK README.md BEFORE RUNNING!
FILEPATH = r"Y:\Estimating\Non-restricted\SPIRIT\RFE141776P\ENGINEERING\313W3153-7.pdf"


parsed_filename = "file"
parsed_filename = parsed_filename if parsed_filename.endswith(".txt") else parsed_filename + ".txt"
print(parsed_filename)