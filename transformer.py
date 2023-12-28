import fitz
import pathlib
import os

class PdfExtractor:
    def __init__(self, filepath: str, output_filename: str, start=1, end=None):
        self.filepath = filepath
        self.start = start

        if end is not None:
            self.end = end
        else:
            self.end = self.get_page_count()
            print(self.end)

        if not output_filename.endswith(".txt"):
            output_filename += ".txt"
        if os.path.isfile(output_filename):
            print("File already exists - Select another filename")
            return None
        else:
            self.output_filename = output_filename
        self.convert_to_txt()

    def get_page_count(self) -> int:
        """returns the page count of the pdf"""
        with fitz.open(self.filepath) as doc:
            num_pages = doc.page_count
        return num_pages

    def append_to_outputfile(self, line):
        with open(self.output_filename, "a") as writefile:
            writefile.write(line + "\n")

    def convert_to_txt(self): 
        with fitz.open(self.filepath) as doc:
            for page_no in range(self.start, self.end):
                current_page = doc[page_no]
                lines_current_page = [line for line in current_page.get_text().split("\n") if not line.isspace()]
                for line in lines_current_page:
                    self.append_to_outputfile(line)
