import re
from regular_expressions import match_footers

class DataCleaner:

    def __init__(self, raw_text_file):
        self.text_filepath = raw_text_file if raw_text_file.endswith(".txt") else raw_text_file + ".txt"
        self.index_skip = []

    def start_end_indexes_for_assembly(self) -> tuple:
        """Start and ending index for iteration -> removes most of the jargon in the document
        Matches the patterns - "Assembly Breakdown List" - start point and "Flag notes general" - end point"""
        startidx = re.compile(r'\s*\.\s*\.\s*\.\s+ASSEMBLY\s+BREAKDOWN\s+LIST\s+\.\s*\.\s*\.')
        endidx = re.compile(r'\s*\.\s*\.\s*\.\s+FLAGNOTES-GENERAL\s+NOTES\s+\.\s*\.\s*\.')
        with open(self.text_filepath, "r") as file:
            self.start, self.end = 0, 0
            for idx, line in enumerate(file.readlines()):
                if startidx.match(line):
                    self.start = idx
                elif endidx.match(line):
                    self.end = idx
                    return self.start, self.end
            assert(self.start != 0 or self.end != 0), "Could not find Assembly Breakdown List in the Document"

    def remove_jargon_indexes(self) -> list:
        """Cleans the data inside the main start and end indexes. We get the main indexes from start_end_indexes_for_assembly"""
        bs_start = re.compile(r'\s*ASSY\s+(?:-?\d+|LIST)?\s*\((CONTINUED\s+ON\s+NEXT\s+PAGE)\)\s*')
        with open(self.text_filepath, "r") as file:
            for idx, line in enumerate(file.readlines()):
                if bs_start.match(line):
                    self.index_skip.append(idx)
                elif line.startswith(" REQD      IDENTIFYING NUMBER") and len(self.index_skip) >= 1:  # to ensure that if gets executed first
                    self.index_skip.append(idx)
        # try and except block here with throwing errors for list being too short
        self.skip_count = self.index_skip[1] - self.index_skip[0]
        self.index_skip = self.index_skip[::2]  # We only need starting points
        print(self.index_skip, self.skip_count)
        

    def parsing_assembly_list(self, output_filename="garb_file1.txt"):
        """iterating over the main start and end indexes, appending lines that are relevant. Finds irrelevant lines from the function above"""
        skip_count = 0
        with open(self.text_filepath, "r") as file:
            with open(output_filename, "w") as writefile:
                lines = file.readlines()
                for idx, line in enumerate(lines[self.start:self.end]):
                    idx += self.start
                    if idx in self.index_skip:
                        skip_count = self.skip_count 
                    elif skip_count == 0:
                        writefile.write(line)
                    elif skip_count > 0:
                        skip_count -= 1  # decreament to only print when skip count is zero

    def remove_footers(self, input_file, output_filename):
        skip_count_list = []
        skip = 0
        with open(input_file, "r") as writtenfile:
            output_filename if output_filename.endswith(".txt") else output_filename + ".txt"
            with open(output_filename, "w") as finalfile:
                lines = writtenfile.readlines()
                for idx, line in enumerate(lines):
                    if match_footers(line):
                        skip_count_list.append(idx)  # we append the idx so that we know when to set skip count to 18
                for idx, line in enumerate(lines):
                    if idx in skip_count_list:
                        skip = 18
                    elif skip > 0:
                        skip -= 1
                    else:
                        finalfile.write(line)

    def parse(self, output_filename):
        self.start_end_indexes_for_assembly()
        self.remove_jargon_indexes()
        self.parsing_assembly_list()
        self.remove_footers("garb_file1.txt", output_filename)

if __name__ == "__main__":
    cleaner = DataCleaner("test_raw_file2.txt")
    cleaner.parse("pased_data_2")
