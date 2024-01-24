# PDF Parser

This PDF parser was developed for Etezazi Industries to parse technical airplane part pdfs and extrat the information related to outside processing. The parser first converts the pdf file into text, while still keeping relatively the same format and then data cleaning methods (w\ Regex and Fuzzy) are applied to the .txt files.

## How to use

The heart of this project is in docparser.py. This docparser's function `boeing_pdf_converter()` can be used by specifying input and output file paths, the function will return a .txt file that keeps the same format as the pdf. This is very important as most regular expressions would not work if the format was changed. 

### Disclaimer

This software, developed by Etezazi Industries, is intended for internal use only and is not designed for or intended for use by the general public. The software is provided 'as is' without warranty of any kind, either expressed or implied. Etezazi Industries disclaims all liability for any damage or issues that may result from using this software.

The software may use open-source libraries or frameworks; their use does not imply endorsement by the original creators. Etezazi Industries offers no support or maintenance services for this software. Users are responsible for ensuring that their use of the software complies with all applicable company policies and laws.

Modification, redistribution, or use of this software outside of Etezazi Industries is not permitted without express written consent. Users are also responsible for managing and protecting any sensitive or personal data handled by the software in accordance with data privacy laws and company policies.