from rooms import *
import items
import collections



        
def parsecommand(userinput):
    '''This is where i separates the command into the 'verb' (e.g. get), and the 'item' (e.g. coconut)'''
    ParsedCommand = collections.namedtuple('ParsedCommand', ['verb', 'item'])
    tokens = userinput.split(' ')
    verb = tokens.pop(0)
    if len(tokens) > 0:
        return ParsedCommand(verb, ' '.join(tokens))
    else:
        return ParsedCommand(verb, '')

def finditem(itemname, container):
    for i in container:
        if i['name'] == itemname:
            return i

def death():
    respawn = input('You died! Would you like to respawn? ')
    if respawn == 'yes':
        it = initialisation()
        global character
        character = it.character
        turn_no = it.turn_no
    else:
        exit()

def chooseroom(character):
    """This is where it decides where the character is."""
    if character.loc == [1,2]:
        character.room = beach
    elif character.loc == [1,1]:
        character.room = rocks
    elif character.loc == [2,2]:
        character.room = jungle
    elif character.loc == [2.5,2]:
        character.room = clearing
    elif character.loc == [3,2]:
        character.room = mountains
    elif character.loc == [2,1]:
        character.room = village
    elif character.loc == [2.5,1]:
        character.room = house
    elif character.loc == [3,3]:
        character.room = waterfall
    elif character.loc == [2,3]:
        character.room = hill
    elif character.loc == [1,3]:
        character.room = cliff
    else:
        print('I can\'t choose a room!!!')

def roomreset():
    beach['items'] = [coconut, rope, seagull]
    rocks['items'] = [rock, starfish, shellfish]


def get(item, character):
    if item not in character.inventory:
        character.inventory.append(item)
        item['inv'] = item['inv'] + 1
    else:
        item['inv'] = item['inv'] + 1

def invcheck(character, item):
    for item in character.inventory:
        if item['inv'] < 1:
            character.inventory.remove(item)

def clone(item):
    index = 1
    newitem = item.copy()
    write(text, newitem)
    return newitem
