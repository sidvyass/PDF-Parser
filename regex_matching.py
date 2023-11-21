import re


def check_re(line):
    """checks for the parts list line"""
    matches = re.compile(r'^PARTS LIST\s+(\d+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s*').match(line)


def split_two_or_more_whitespace(data: str) -> list:
    """Splits the string into elements, has to have two or more whitespace in between to split"""
    result = re.split(r'\s{2,}', data.strip())
    return result


def matching_part():
    # we might not need this anymore
    patternstart = re.compile(r"^ REQD      IDENTIFYING NUMBER     DESCRIPTION            CODE                                                                  SYM$", re.IGNORECASE)
    patternend = re.compile(r"")
    with open("document.txt", "r") as file:
        for idx, line in enumerate(file.readlines()):
            if patternstart.match(line): 
                print(f"found - index is: {idx}")
            elif patternend.match(line): 
                print("s")
            else: 
                print("xy")


def start_end_indexes_for_assembly():
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
    

def assy_list_indexes():
    # this gives us the indexes to skip over
    #TODO: add logic to skip - might be different for different documents
    bs_start = re.compile(r'\s*ASSY\s+LIST\s+\(CONTINUED\s+ON\s+NEXT\s+PAGE\)\s*')
    bs_end = re.compile(r'\s*ASSY\s+LIST\s+\(CONTINUED\s+FROM\s+PRECEDING\s+PAGE\)\s*')
    with open("document.txt", "r") as file:
        for idx, line in enumerate(file.readlines()):
            if bs_start.match(line):
                print(idx)
            elif bs_end.match(line):
                print(idx, "this is where it stops")
    print(bs_index)


def parsing_assembly_list():
    bs_skip = [90, 163, 236, 309]
    skip_count = 0
    with open("document.txt", "r") as file:
        lines = file.readlines()
        start_index, end_index = start_end_indexes_for_assembly()
        for idx, line in enumerate(lines[start_index:end_index]):
            idx += start_index
            if idx in bs_skip:
                skip_count = 24
            elif skip_count == 0:
                print(line)
            elif skip_count > 0:
                skip_count -= 1  # decreament to only print when skip count is zero


bs_index = [90, 114, 163, 187, 236, 260, 309, 333]
# need to skip over the 24 lines starting at 90, 163 and so on
if __name__ == "__main__":
    parsing_assembly_list()
    # assy_list_indexes()
