import re

def openFile(filePath: str):
    with open(filePath, 'r') as file:
        return file.readlines()
    
map = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9'
}

def process(lines: list):
    count = 0
    for line in lines:
        myDict = {}
        for key in map:
            match = re.finditer(key, line)
            for m in match:
                myDict[m.start()] = m.group()
        sortedDict = dict(sorted(myDict.items()))
        matches = list(sortedDict.values())
        first = matches[0]
        last = matches[-1]
        count += int(map[first] + map[last])
    return count

fileLines = openFile('lines.txt')

c = process(fileLines)
print(c)