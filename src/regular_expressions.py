import re

pattern_set_0 = [
    "   -      -1                     SHIM                 - OP   -2 OPPOSITE -1                                                     B", 
    "   -      -6                     RADIUS FILLER        - OP   -6 OPPOSITE -5", 
    "   -      -3                     SHIM                 - MF   MAKE FROM BACS40R014C018F", 
    "   -      -7                     SHIM LAMINATED       - MD   PT MK M     FIN F-17.07                                            C",
    "   -      -13                    SPLICE, S-27L        - MD   ZONE 13B4      PT MK M                                             A",
    "   -      -2                     SPLICE, S-8L         - MD   ZONE 2B4       PT MK M",
    "   -      -1                     SHEAR TIES INSTL     - MD   ZONE 4C8",
    "   -      -157                   EXTENSION INSTL-     - EN   (VARIABLE).                                                        P", 
    "   -      -185                   EXTENSION INSTL      - EN   (VARIABLE)                                                        AD",
    "   -      -2                     FINISH INSTL         - EN   (PRE-MODULE) PROTECTIVE                                           CC",
    "   -      -202                   EXTENSION INSTL-     - EN   VARIABLE                                                          AH",
    "   -      -214                   INTEGRATION INSTL    - EN   INCLUDES PROVISIONS FOR NEW ELEVATOR TENSION                      BC",
    "   -      -222                   INTEGRATION INSTL    - EN   INCLUDES PROVISIONS FOR NEW ELEVATOR TENSION                      BK",
    "   -      -223                   SUPPORT INSTL        - EN   FLOOR (PRE-MODULE)                                                BG",
    "   -      -245                   CLOSEOUT INSTL       - EN   (PREMODULE)                                                       CD",
    "   -      -3                     CANTED BHD TIE INSTL - EN   (PRE-MODULE) LH                                                   CC",
]

pattern_set_3 = [
    "   1      -29                    STRINGER SPLICE      - MD   ZONE 3A10      PT MK M                                             K", 
    "   2      141T0113-1             FITTING              - MD   ZONE 1B10                                                          A", 
    "   1      -7                     STRINGER SPLICE      - OP   -8 OPPOSITE -7                                                     U",
    "   2      141T0113-1             FITTING              - MD   ZONE 1B10                                                          D",
]

# this is the pattern to match the first set of spaces + dashes AND matches the last letters (capital only).
pattern = r"^\s*-\s*-\d+\s+.*\s+([A-Z]+)\s*$"
re_string = re.compile(pattern)

# same as the pattern above but this has optional matching of the last characters (REVS).
pattern_1 = r"^\s*-\s*-\d+\s+.*(?:\s+([A-Z]+))?\s*$"
re_string_1 = re.compile(pattern_1)

for i in pattern_set_0:
    match = re.match(re_string, i)
    if match:
        print(i)
    elif re.match(re_string_1, i):
        match = re.match(re_string_1, i)
        print(match)
    else:
        print("pass")
