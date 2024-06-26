def open_file(filePath: str):
    with open(filePath, 'r') as file:
        return file.readlines()

def process(lines: list):
    count = 0
    for line in lines:
        arr = [char for char in line if char.isdigit()]
        if (len(arr) == 1):
            count += int(arr[0] + arr[0])
            continue
        first = arr[0]
        last = arr[-1]
        count += int(first + last)
    return count

fileLines = open_file('lines.txt')

c = process(fileLines)
print(c)