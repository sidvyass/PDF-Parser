import fitz, pathlib, logging
import regex_matching

#TODO : add flag notes func - map to the part number
#TODO : map the opp vars

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


# WE DONT NEED THIS AS OF NOW


def pl_data_struct() -> dict:
    """Organises the data into a dict - Key is the -1 numbers and value is whatever comes after it"""
    value = ""
    parts_dict = {}
    # index hard coded for parsing purposes
    with open("parsed_data.txt", "r") as file:
        lines = file.readlines()
        for line in lines:  # code to identify the "Assembly list" goes here
            try: 
                if line.strip().startswith("-"):
                    dict.clear(parts_dict)
                    value = ""
                    data = regex_matching.split_two_or_more_whitespace(line)
                    # print(data)
                    # print(data[1], data[2])
                    parts_dict["Identifying Number"] = data[1]
                    parts_dict["Description"] = data[2]
                    value = "   ".join(data[3:]) + "\n"  # to ensure correct formatting
                else:
                    value += line
                    parts_dict["Description"] = value
                    print(parts_dict)
            except IndexError:
                continue


if __name__ == "__main__":
    # needs to make sure that the parts that are related go together
    # the doc for finishes does not change - parse it into the django container

#   -      -1                     SKATE ANGLE-FWD      - OP   -2 OPPOSITE -1.                                                    A
#                                                         MD   ZONE 1A8       PT MK M
#                                                              FIN F-21.18.
#                                                              STOCK 4.2 X 4.6 X 70.3
#                                                              2219-T851 PLATE PER QQ-A-250/30.  ULTRASONIC INSPECT
#                                                              PER BAC 5439, CLASS A.
#                                                         AV   ADVANCE ORDER REQUIRED CONTACT MATL - D. KRENKE
#                                                              529-6735, A. BURKLE 529-6732
#                                                         DP   DRAWING PICTURE SHEET 1.
#                                                         EA   EAMR NUMBER 313W3153-1 PROC CODE - W3002 END ROUTE -
#                                                               LT, 773/IN CDS PAGE - 27, LINE - G DATE DUE ON DOCK
#                                                              - WORKING SIZE INCLUDING MFG EXCESS - 6.0 X 8.0 X
#                                                              75.0
#                                                         GA   PENETRANT INSPECT PER BAC 5423.
#    -      -10                    SKATE ANGLE-AFT UPR  - OP   -10 OPPOSITE -9.                  

    pl_data_struct()