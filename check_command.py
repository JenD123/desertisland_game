from cfunctions import *
from classes import *
import tkintermaker
from tkintermaker import exit
from initialisation import initialisation

global character
character = Character(loc = [1,2], health = 20, status = 'alive', inventory = []) 



def check_command(cmd, item, collection, toolslist, makelist):
    if character.status == 'alive':
        verbiage = False
        if cmd.verb in ['help', 'h']:
            help_command(character)
        elif cmd.verb in ['look', 'l']:
            verbiage = look_command(character)
        elif cmd.verb == '_items':
            verbiage = items_command(character.room)
        elif cmd.verb in ['get']:
            get_command(cmd, character, item)
        elif cmd.verb in ['use', 'u']:
            use_command(character, item, toolslist)
        elif cmd.verb in ['inventory', 'i']:
            inventory_command(character)
        elif cmd.verb in ['eat']:
            eat_command(cmd, character, item)
        elif cmd.verb == 'health':
            health_command(character)
        elif cmd.verb in ['west','w']:
            west_command(character)
        elif cmd.verb in ['east','e']:
            east_command(character)
        elif cmd.verb in ['north','n']:
            north_command(character)
        elif cmd.verb in ['south','s']:
            south_command(character)
        elif cmd.verb in ['examine', 'ex']:
            examine_command(item)
        elif cmd.verb in ['enter']:
            enter_command(character)
        elif cmd.verb in ['exit']:
            exit_command(character)
        elif cmd.verb in ['rest', 'r']:
            rest_command(character)
        elif cmd.verb == '_teleport':
            teleport_command(character, cmd)
        elif cmd.verb == 'make':
            make_command(item, character, makelist)
        elif cmd.verb == '_get':
            cget_command(character, item, collection)
        elif cmd.verb == '_die':
            die_command(character)
        elif cmd.verb == '_five':
            five_command(character)
        elif cmd.verb == 'drop':
            drop_command(character, item)
        else:
            error_command()
            
        if verbiage:
            write(tkintermaker.text, verbiage)
    elif character.status == 'help':
        if cmd.verb == 'leave':
            leave_command(character)
        elif cmd.verb in ['topics']:
            topics_command()
        elif cmd.verb == 'game':
            game_command()
        elif cmd.verb == 'food':
            food_command()
        elif cmd.verb == 'crafting':
            crafting_command()
        elif cmd.verb in ['HP', 'hp', 'health']:
            hpinfo_command()
        else:
            help_error()
    elif character.status == 'end1':
        if cmd.verb in ['yes', 'y']:
            character.status = 'alive'
            continue_command(character)
        
    else:
        if cmd.verb in ['yes', 'y']:
            initialisation()
            character.status = 'alive'
            character.health = 20
        else:
            exit()



def chealth_check(turn_no):
    health_check(turn_no, character)
def chealth_warning():
    health_warning(character)
def cstarvation_check():
    starvation_check(character)

def mini(entry, program):
    entry.bind('<Return>', program)