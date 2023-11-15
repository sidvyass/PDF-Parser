import PyPDF2
import xml.etree.ElementTree as ET
import pandas as pd


def extract_text_from_pdf(file_path):
    text = ''
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)  # PdfFileReader does not work
        num_pages = len(pdf_reader.pages)

        for page_num in range(num_pages):
            page = pdf_reader.getPage(page_num)
            text += page.extractText()
    return text


def extract_text_from_xml(file_path):
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


def extract_text_from_excel(file_path):
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


def useful_text_extraction(text):
    """Text -> formatting and extraction of useful information"""
    # here we will use the NER model - currently not used
    extracted_data = {}
    lines = text.split('\n')

    for line in lines:
        if ':' in line:
            label, value = line.split(':', 1)
            label = label.strip()
            value = value.strip()
            extracted_data[label] = value

    return extracted_data


# module testing
FILEPATH = r"Y:\Estimating\Non-restricted\SPIRIT\RFE 141776P\ENGINEERING\313W3153-7.pdf"
if __name__ == "__main__":
    txt = extract_text_from_pdf(FILEPATH)
    print(txt)
    # final_data = useful_text_extraction(txt)
    # print(final_data)
