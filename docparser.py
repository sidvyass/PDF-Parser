import xml.etree.ElementTree as ET
import pandas as pd
from pdfminer.high_level import extract_text


# NOT IN USE
# def extract_text_from_pdf(file_path) -> str:
#     """CURRENTLY NOT IN USE - NEW FUNCTION ON LINE 19"""
#     text = ''
#     with open(file_path, 'rb') as file:
#         pdf_reader = PyPDF2.PdfReader(file)  # PdfFileReader does not work
#         num_pages = len(pdf_reader.pages)

#         for page_num in range(num_pages):
#             page = pdf_reader.pages[page_num]
#             text += page.extract_text()
#     return text


# NEW FUNCTION
def pdf_parse(filepath) -> str:
    """Uses pdfminer.six API to extract text from pdf"""
    text = extract_text(filepath)
    return text


def extract_text_from_xml(file_path) -> str:
    """Parser for xml file uses trees to iterate and crawl through the text. (Final text is not returned through this function)"""
    text = ''
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        # Iterate through XML elements to extract text
        for element in root.iter():
            if element.text:
                text += element.text.strip() + ' '
    except ET.ParseError as e:
        print(f"Error parsing XML file: {e}")
    return text


def extract_text_from_excel(file_path) -> str:
    text = ''
    try:
        df = pd.read_excel(file_path)
        # Iterate through each cell in the dataframe to extract text
        for column in df.columns:
            for value in df[column].values:
                if pd.notna(value):
                    text += str(value) + ' '

    except pd.errors.ParserError as e:
        print(f"Error parsing Excel file: {e}")

    return text


def useful_text_extraction(text: str) -> dict:
    """Text -> formatting and extraction of useful information"""
    # here we will use the NER model - currently not used
    extracted_data = {}
    lines = text.split('\n')

    for line in lines:
        if ':' in line:
            label, value = line.split(':', 1)
            label = label.strip()
            value = value.strip()
            print(label, value, sep=" --- ")  # TODO: testing remove
            print("*"*10)
            extracted_data[label] = value

    return extracted_data

