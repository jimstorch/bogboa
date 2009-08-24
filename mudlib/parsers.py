# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/parsers.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

from mudlib import shared


"""
Decorator functions to parse and error check arguments for player commands and
general search functions.
"""    


#-------------------------------------------------------------------------Blank

def blank(cmd_func):

    """Decorator to enforce zero arguments."""

    def parse_func(client):
        args = client.verb_args
        if len(args):
            client.alert('That command does not use parameters.')
            return
        else:
            cmd_func(client)

    return parse_func


#----------------------------------------------------------------------Singular

def singular(cmd_func):

    """Decorator to enforce single parameter commands."""

    def parse_func(client):
        args = client.verb_args
        if len(args) == 0:
            client.alert('That command requires a parameter.')
            return
        elif len(args) > 1:
            client.alert('Too many parameters -- use one.')
            return                
        else:
            cmd_func(client, args[0])

    return parse_func



#-------------------------------------------------------------------None or One

def none_or_one(cmd_func):

    """Decorator that accepts zero or one parameters."""

    def parse_func(client):
        args = client.verb_args
        if len(args) > 1:
            client.alert('Too many parameters -- use one.')
            return
        elif len(args) == 1:
            arg = args[0]
        else:
            arg = None
     
        cmd_func(client, arg)

    return parse_func


#---------------------------------------------------------------------Monologue

def monologue(cmd_func):

    """Decorator to combine all args into a single string."""

    def parse_func(client):
        args = client.verb_args
        if not len(args):
            client.alert('Missing parameters.')
            return
        else:
            msg = ' '.join(args)
            cmd_func(client, msg)
    return parse_func        
    


#----------------------------------------------------------------------Dialogue

def dialogue(cmd_func):

    """Decorator to identify a target and combine remaining arguments."""

    def parse_func(client):
        args = client.verb_args
        if len(args) == 0:
            client.alert('Command is missing a subject and message.')
            return
        elif len(args) == 1:
            client.alert('Command is missing a message.')
            return
        else:
            name = args.pop(0)
            target = shared.find_player(name)
            if target == None:
                client.alert('%s is not online.' % name)
                return
            msg = ' '.join(args)
            cmd_func(client, target, msg)
    return parse_func 



#-------------------------------------------------------------------Set or Show

def set_or_show(cmd_func):

    """
    Set/Unset decorator parser.  Returns:

    None for no args -- display the current setting.
    True for yes-like args -- turn it on.
    False for no-like args -- turn it off.
    """
    
    def parse_func(client):
        args = client.verb_args
        if len(args) > 1:
            client.alert('Too many parameters.')
            return        
 
        if len(args) == 0:
            setting = None

        else:
            arg = args[0].lower()

            if arg in ['yes', 'true', '1', 'on']:
                setting = True
            
            elif arg in ['no', 'false', '0', 'off']:
                setting = False

            else:
                client.alert('Please use a yes/no or on/off parameter.')
                return

        cmd_func(client, setting)

    return parse_func


#-----------------------------------------------------------------Online Player

def online_player(cmd_func):

    """Decorator to target an online player."""

    def parse_func(client):
        args = client.verb_args
        if len(args) != 1:
            client.alert('That command requires a player name.')
            return
        else:

            name = args[0]
            target = shared.find_player(name)
            if target == None:
                client.alert('Player not found online.')
                return

            cmd_func(client, target)

    return parse_func             


#------------------------------------------------------------------Item in Room

def item_in_room(cmd_func):

    def parse_func(client):
        args = client.verb_args
        if len(args) == 1:
            pass
    

    pass


#-------------------------------------------------------------Item in Inventory

def item_in_inventory(cmd_func):

    pass

#------------------------------------------------------------------Body in Room

def body_in_room(cmd_func):
    pass


