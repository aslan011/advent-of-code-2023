import re;

def open_file(file_path: str):
    with open(file_path, 'r') as file:
        return file.readlines()
    
def process(games: list):
    count = 0
    actual = {
        'red': 12,
        'green': 13,
        'blue': 14
    }
    count = 0
    for game in games:
        game_possible = True
        parsed = re.sub(r'(Game )(\d+:)', '', game)
        ID = re.search(r'(Game )(\d+)', game).groups()[1]
        turns = parsed.split(';')
        for turn in turns:
            matches = re.findall(r'(\d+) (red|green|blue)', turn)
            for match in matches:
                quantity, color = int(match[0]), match[1]
                if quantity > actual[color]: 
                    game_possible = False
                    break
        if game_possible == True: count += int(ID)
    return count

games = open_file('games.txt')

print(process(games))

