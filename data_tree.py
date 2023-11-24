import regex_matching, csv

data_dict = {}


def stripline(line: str, search_str: str):
    return line.strip().startswith(search_str)


def headers(header_list):
    """Currently hard coded but can use regex matching later on"""
    try:
        number = int(header_list[1])
        name = header_list[2]
        finish = header_list[3]
        info = header_list[4]
        rev = header_list[5]
        data_dict[number] = {"name":name, 
                            "finish": finish,
                            "info": info, 
                            "rev": rev,
                            "ALL INFO": ""}
        print(number)
        return number
    except (IndexError, ValueError) as e:
        print(f"{e} - This is normal")
        return False


def add_other_info(data_str: str, number: int):
    """If blocks to identify which info goes where"""
    try:
        data_dict[number]["ALL INFO"] += data_str  # all info in case our library misses something
        if stripline(data_str, "FIN"):
            data_dict[number]["Finish name"] = data_str.strip()
        elif stripline(data_str, "STOCK"):
            data_dict[number]["dimensions"] = data_str.strip()
    except KeyError as e:
        print(f"{e} - this is normal")


def separate_parts_main_loop():
    with open("parsed_data.txt", "r") as file:
        file.readline()  # read heading
        lines = file.readlines()
        num = None
        for line in lines:
            data_list = regex_matching.split_header(line) 
            if data_list[0] == "-":  # will execute when new part
                num = headers(data_list)
            else:  # adds everything to the current part
                add_other_info(line, num)


if __name__ == "__main__":
    separate_parts_main_loop()
    for key, value in data_dict.items(): 
        print(key, value)
