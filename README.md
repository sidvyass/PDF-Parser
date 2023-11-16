Document Parser -> inject into SQL
    Input -> FILE PATH - this only has one input
    Output -> 


Code changes - 


Testing Documentation -> 
    PDF miner works the best for aviation documents - Focuses only on text based extraction

Dev updates -> 
11/15 - First inital commit, pushing to github URL - https://github.com/etezazicorps
        - Made a local and private git repo to control the versions of the code - making gitignore files, branching and locally committing
        - PDF parsing function does not work the library is too old to work - reworked to working condition
        - Parsed data is not correct - fixing will take time as I dont understand what to extract
        - The PDF library used is not correct to the parse the data - trying to use pdfminer
        - Main PDF parsing library changed to pdfminer - high level API
        