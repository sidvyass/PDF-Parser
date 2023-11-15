import tkinter as tk
from tkinter import filedialog
import pystray
from PIL import Image
import spacy
import xml.etree.ElementTree as ET
import pandas as pd
from docparser import *
from sql_inputs import *

# CHECK README.md BEFORE RUNNING!

ML_TEXT_PROCESSING = spacy.load('en_core_web_sm')  # TODO: instance of the NER model but this is currently not used anywhere. 


def open_file_dialog(icon, item):
    """Opens a window where one can select files for input"""
    file_paths = filedialog.askopenfilenames()
    print("Selected files:")
    for file_path in file_paths:
        print(file_path)
        extracted_data = extract_information(file_path)
        upload_data_to_table(extracted_data)


def direct_parser(file_path):
    """Directs the file to the correct parser"""
    # Extract text from the document based on the file format
    text = ''

    if file_path.endswith('.pdf'):
        text = extract_text_from_pdf(file_path)

    elif file_path.endswith('.xml'):
        text = extract_text_from_xml(file_path)

    elif file_path.endswith('.xlsx') or file_path.endswith('.xls'):
        text = extract_text_from_excel(file_path)

    else:
        print("Unsupported file format.")
        return 0
    return text


def useful_text_extraction(text):
    """Text -> proper formatting extraction of useful information"""
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


# TODO: we will create this at the very end if everything runs properly
# def create_desktop_application():
#     window = tk.Tk()
#     window.withdraw()

#     # Create the system tray icon
#     icon_path = "M:/cloud-upload.ico"
#     icon = pystray.Icon("Desktop App", Image.open(icon_path))
#     menu = (pystray.MenuItem("Open File", lambda item, icon: open_file_dialog(icon, item)),)
#     icon.menu = pystray.Menu(*menu)

#     # Run the system tray icon loop
#     icon.run()

#if_name_ == __main__ 
# Start the desktop application
# create_desktop_application()


if __name__ == "__main__":
    open_file_dialog()
