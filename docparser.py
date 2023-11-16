from pdfminer.high_level import extract_text
import re


def read_convert_pdf(filepath) -> str:
    """Uses pdfminer.six API to extract text from pdf"""
    text = extract_text(filepath)
    return text


def parse_data_boeing(text: str) -> dict:
    """Text -> dict using manual parsing methods of string indexing etc"""
    extracted_data = {}
    lines = text.split('\n')  # TODO: try another way
    pattern = re.compile(r'\s+')
    data_list_strings = [re.sub(pattern, ' ', line) for line in lines if line.startswith("    PARTS LIST")]  # removes white spaces - only parts list
    
    # from here we start parsing the data into their respective categories - data is now free of all jargon
    
