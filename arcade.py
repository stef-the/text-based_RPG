# Text Based Game

### Standard  Classes ###
# Warrior               #   - Melee/Damage
# Ranger                #   - Bows/Range
# Scout                 #   - Knives/Speed
# Wizard                #   - Spells/Support
#### Special Classes ####
# Knight                #   - Warrior Derivative
# Paladin               #   - Knight/Samurai Derivative
# Samurai               #   - Warrior/Scout Derivative
# Sharpshooter          #   - Hunter Derivative
# Hunter                #   - Ranger/Scout Derivative
# Assasin               #   - Scout Derivative
# Cleric                #   - Wizard Derivative
#########################

from time import sleep as t_slp
from time import asctime as cur_t
from time import gmtime, strftime
from sys import stdout as sys_stdout
from sys import version_info
from json import loads as jsonloads

class text:
    class box:
        cross = '┼'
        horizontal = '─'
        vertical = '│'

        class t:
            right = '├'
            left = '┤'
            down = '┬'
            up = '┴'
        
        class angle:
            left_down = '╮'
            left_up = '╯'
            
            right_down = '╭'
            right_up = '╰'
        
        class end:
            right = '╶'
            left = '╴'
            down = '╵'
            up = '╷'

    class color:
        purple = '\033[95m'
        blue = '\033[94m'
        cyan = '\033[96m'
        green = '\033[92m'
        yellow = '\033[93m'
        red = '\033[91m'
        stop = '\033[0m'
        bold = '\033[1m'
        underline = '\033[4m'

    
    class print:
        def bold(text_input):
            print(text.color.bold + str(text_input) + text.color.stop)
        def under(text_input):
            print(text.color.under + str(text_input) + text.color.stop)
    
    def up(amount: int = 1):
        for i in range(0, amount):
            sys_stdout.write("\033[F")
    
    input = (color.bold + '> ' + color.stop)

class game:
    username = None

    class version:
        major = 0
        minor = 0
        micro = 1
    
    class info:
        name = 'Stef\'s Text-Based Dungeon Crawler'
        author = 'stef#6470'
        creation_date = 'Jun 7 2021'
    class startup():
        def text():
            text.print.bold(f'\nWelcome to {game.info.name}')
            print(text.color.cyan + f'''Built by {game.info.author}
Project Started on {game.info.creation_date}
''' + text.color.stop)

        def login():
            print('\nWelcome!')
            for i in range(0, 3):
                print('.' * i)
                sys_stdout.write("\033[F")
                t_slp(0.2)
            
            save = False

            print('Do you have a save code? (Y/N)')
            save_input = input(text.input)

            if 'y' in save_input:
                save = True
            else:
                pass

            text.up(3)

            if save:
                print('\nDo you have a save code? ' + text.color.green + 'Yes  ' + text.color.stop)
            
            else:
                print('\nDo you have a save code? ' + text.color.red + 'No   ' + text.color.stop)
                text.up()
                print('\nWhat would you like your username to be?')
                game.username = input(text.input)
                text.up()

                if len(game.username) > 1:
                    print('Your Username: ' + text.color.purple + game.username + text.color.stop + (' ' * (25 - len(game.username))))
                
                else:
                    print('Your chosen username is too short! The game will close, start it again!\n')
                    exit()

class debug:
    def info():
        print(text.color.blue + f'''[DEBUGGER INFORMATION]
Current Time: {cur_t()}, {strftime("%z", gmtime())}
Python Version: {version_info.major}.{version_info.minor}.{version_info.micro} - {version_info.releaselevel}
Game Verison: {game.version.major}.{game.version.minor}.{game.version.micro}''' + text.color.stop)

print(text.color.stop)


game.startup.text() # Game name,e author
debug.info() # Display debugging information

game.startup.login() # Get save code/create username + class

class_tree = jsonloads(open('classes.json', 'r').read())
print('\n')
print(class_tree)

b = text.box

for i in class_tree:
    if i['upgrades'] != []:
        if len(i['upgrades']) > 1:

            for j in class_tree:
                if j['id'] == i['upgrades'][0]:
                    aa = j
            
            print(i['name'] + b.end.right + b.t.down + b.end.left + aa['name'])

    else:
        print(i['name'])