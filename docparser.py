import fitz, pathlib, sys, logging, re
import regex_matching

logging.basicConfig(level=logging.INFO)

with open("document.txt", "r") as doc:
    data_list = [line for line in doc.readlines()]


final_list = []
FILEPATH = r"Y:\Estimating\Non-restricted\SPIRIT\RFE 141776P\ENGINEERING\313W3153-7.pdf"


def boeing_pdf_parser(filename):  #TODO: args taken from the terminal
    """PDF -> txt file: maintains the correct format of the pdf"""
    with fitz.open(FILEPATH) as doc:
        text = chr(12).join([page.get_text() for page in doc])

    pathlib.Path(filename + ".txt").write_bytes(text.encode())
    logging.info(f"PDF Parsed Successfully - {filename}")


def get_headers():
    """Does not return anything, just added headers on to the final dict. Uses string methods"""
    for line in data_list:
        line.strip()
        if line.startswith("PARTS LIST"):  # this can be done only once using regex matching
                final_list.append([line.split()[2:].pop(2)])
                logging.info("Added headers")
                break
        else:
            logging.debug("No headers found")


# identify the REQD IDENTIFYING NUMBER line and then use the function that comes after this
def pl_data_struct():
    value = ""
    parts_dict = {
        "Reqd": "-",  # only for this pdf
        "Identifying Number": None, 
        "Description": None,
    }
    # index hard coded for parsing purposes
    for idx, line in enumerate(data_list[77:88]):  # code to identify the "Assembly list" goes here
        if idx==0:
            data = regex_matching.split_two_or_more_whitespace(line)
            parts_dict["Identifying Number"] = data[1]
            parts_dict["Description"] = data[2]
            value = "   ".join(data[3:]) + "\n"  # to ensure correct formatting
        else:
            value += line
        
        parts_dict["Description"] = value
    # print(f"THE KEY IS : {parts_dict['Identifying Number']} ")
    # print("THE VALUE IS : ", sep="")
    # print(parts_dict["Description"])
