Document Parser -> inject into SQL
    Input -> dir where the files are (aiming to parse all these at once)
    Output -> a searchable data struct that we can use to input "PL no" and "dash(-)" numbers so that we can find what we need on the fly. \
    in short the output is the part specification requested. 

Testing Documentation -> 
    - fitz is used to parse pdf documents and maintain their format. In this case we pdf -> txt and then parse it into a data structure - dict
