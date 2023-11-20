import re

testcases = []


def check_re(line):
    pattern = re.compile(r'^PARTS LIST\s+(\d+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s*')
    matches = pattern.match(line)


def split_two_or_more_whitespace(data: str) -> list:
    result = re.split(r'\s{2,}', data.strip())
    return result


for case in testcases:
    check_re(case)
