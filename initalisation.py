import tkintermaker
import collections


output = tkintermaker.Output()

def initialisation():

    output.write(tkintermaker.text, """
    Welcome to the desert island game
    Are you ready??
    You slowly awaken to a dazzling bright light.
    It's the sun.
    Aduh!
    Haven't you played these games before?
    Point is you’re stuck on a desert island.
    The smell of salt is on the air.
    Above you, seagulls circle in the sky like vultures,
    looking for their next meal... Yeah, you should
    probably get away from here
    You see a shelf of rock to the east,
    To the west, the beach stretches out of sight.
    The jungle is to the north of you and the ocean the south.
    The sun blazes on above you.

    If you are unsure what to do, type 'help'.""")


    InitTuple = collections.namedtuple('InitTuple', ['character', 'turn_no'])
    character = Character(loc = [1,2], health = 20, inventory = [])
    print('initialisaton is awesome!')
    roomreset()
    global turn_no
    turn_no = 0
    return InitTuple(character, turn_no)