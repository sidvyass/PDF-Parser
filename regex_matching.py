"""Parser that is used after converting the pdf document -> txt file. 
    This module is entirely regex focused with most regex functions being used to parse
    assembly list breakdowns.

    - We first clean up the data and match regexes to give us the indexes over which we need to iterate
    - Cleaning up involves matching regex to remove reduntant jargon that comes after every assembly list page
    - The parsing_assembly_list function only calls the start_end_indexes_for_assembly function currently. 
    - The list needed to skip over is hard coded as of now but logic can be added easily to parse
"""


import re

def split_header(data: str) -> list:
    """Splits the string into elements, has to have two or more whitespace in between to split"""
    result = re.split(r'\s{2,}', data.strip())
    return result


def start_end_indexes_for_assembly() -> tuple:
    """Start and ending index for iteration -> removes most of the jargon in the document
    Matches the patterns - "Assembly Breakdown List" - start point and "Flag notes general" - end point"""
    # matches "ASSEMBLY BREAKDOWN LIST" and then we use that to start out iteration
    startidx = re.compile(r'\s*\.\s*\.\s*\.\s+ASSEMBLY\s+BREAKDOWN\s+LIST\s+\.\s*\.\s*\.')
    endidx = re.compile(r'\s*\.\s*\.\s*\.\s+FLAGNOTES-GENERAL\s+NOTES\s+\.\s*\.\s*\.')
    with open("document.txt", "r") as file:
        for idx, line in enumerate(file.readlines()):
            if startidx.match(line):
                start = idx
            elif endidx.match(line):
                end = idx
                return start, end
        return 0  # debug this so that it throws an error - DEBUG
    

def remove_jargon_indexes() -> list:
    """Returns a list to let us know how many lines to skip over -> 
    Regex matches pattern "ASSY LIST (CONTINUED ON NEXT PAGE)" - start point
    "ASSY LIST (CONTINUED FROM PRECEDING PAGE)" - end point
    The no. of lines that come in the middle stay consistent so we only need to calculate once"""
    #TODO: add logic to skip - might be different for different documents
    bs_start = re.compile(r'\s*ASSY\s+LIST\s+\(CONTINUED\s+ON\s+NEXT\s+PAGE\)\s*')
    bs_end = re.compile(r'\s*ASSY\s+LIST\s+\(CONTINUED\s+FROM\s+PRECEDING\s+PAGE\)\s*')
    with open("document.txt", "r") as file:
        for idx, line in enumerate(file.readlines()):
            if bs_start.match(line):
                print(idx)
            elif bs_end.match(line):  # this tell us how much to skip over (end - start)
                print(idx, "this is where it stops")
    return bs_index


def parsing_assembly_list():
    """Skips over everything but assembly list breakdown and outputs it to the terminal"""
    bs_skip = [90, 163, 236, 309]  # currently hard coded but will change soon
    skip_count = 0
    with open("document.txt", "r") as file:
        with open("parsed_data.txt", "w") as writefile:
            lines = file.readlines()
            start_index, end_index = start_end_indexes_for_assembly()
            for idx, line in enumerate(lines[start_index:end_index]):
                idx += start_index
                if idx in bs_skip:
                    skip_count = 24
                # the startswith line removes all the headers
                elif skip_count == 0 and not (line.strip().startswith("QTY") or line.strip().startswith("REQD")):
                    print(line)
                    writefile.write(line)
                    # print(line.strip())
                elif skip_count > 0:
                    skip_count -= 1  # decreament to only print when skip count is zero


bs_index = [90, 114, 163, 187, 236, 260, 309, 333]  # logic to calculate how many lines we need to step over        
if __name__ == "__main__":
    parsing_assembly_list()
