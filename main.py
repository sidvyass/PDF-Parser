import tkinter as tk
from tkinter import filedialog
import xml.etree.ElementTree as ET
from docparser import *

# CHECK README.md BEFORE RUNNING!


FILEPATH = r"Y:\Estimating\Non-restricted\SPIRIT\RFE 141776P\ENGINEERING\313W3153-7.pdf"
if __name__ == "__main__":
    txt = pdf_parse(FILEPATH)
    final_data = useful_text_extraction(txt)
    print(final_data)
