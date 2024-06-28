import re

def open_file(file_path: str):
    with open(file_path, 'r') as file:
        return file.readlines()
    

def process(lines: list):
    count = 0
    pattern = r"[0-9]+"
    for index, line in enumerate(lines):
        matches = re.finditer(pattern, line)
        for match in matches:
            if index == 0:
                if isPartNumber(currentLine=line, previousLine='None', nextLine=lines[index+1], match=match):
                    count += int(match.group())
                    continue
            elif index == len(lines) - 1:
                if isPartNumber(currentLine=line, previousLine=lines[index-1], nextLine='None', match=match):
                    count += int(match.group())
                    continue
            elif isPartNumber(currentLine=line, previousLine=lines[index-1], nextLine=lines[index+1], match=match):
                count += int(match.group())
                continue
    return count


regex_pattern = r"[^a-zA-Z0-9\n.]"
def isPartNumber(currentLine, previousLine, nextLine, match):
    index = match.start(0)
    str = match.group()
    is_part_number = False
    currentLineSymbols = [(m.start(0)) for m in re.finditer(regex_pattern, currentLine)]
    previousLineSymbols = [(m.start(0)) for m in re.finditer(regex_pattern, previousLine)]
    nextLineSymbols = [(m.start(0)) for m in re.finditer(regex_pattern, nextLine)]
    combined = list(currentLineSymbols) + list(previousLineSymbols) + list(nextLineSymbols)
    is_part_number = any((ind >= (index - 1) and ind <= (index + len(str))) for ind in combined)
    # is_part_number = any((4 >= (0 - 1) and 4 <= (0 + 3 + 1)) for ind in combined)
    return is_part_number

fileLines = open_file('engine.txt')

c = process(fileLines)
print(c)