import re;

def open_file(file_path: str):
    with open(file_path, 'r') as file:
        return file.readlines()
    
def process(games: list):
    count = 0
    for game in games:
        fewest = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        parsed = re.sub(r'(Game )(\d+:)', '', game)
        turns = parsed.split(';')
        for turn in turns:
            matches = re.findall(r'(\d+) (red|green|blue)', turn)
            for match in matches:
                quantity, colour = int(match[0]), match[1]
                fewest[colour] = max([quantity, fewest[colour]])
            game_power = fewest['red'] * fewest['green'] * fewest['blue']
        count += game_power
    return count

games = open_file('games.txt')

print(process(games))
