from docparser import *

# CHECK README.md BEFORE RUNNING!
FILEPATH = r"Y:\Estimating\Non-restricted\SPIRIT\RFE 141776P\ENGINEERING\313W3153-7.pdf"


if __name__ == "__main__":
    txt = read_convert_pdf(FILEPATH)
    final_data = parse_data_boeing(txt)
