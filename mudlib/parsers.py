# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/parsers.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

"""
Decorator functions to parse and error check arguments for player commands.
"""    


#-------------------------------------------------------------------------Blank

def blank(cmd_func):

    """Decorator to enforce zero arguments."""

    def parse_func(client):
        args = client.verb_args
        if len(args):
            client.send('That command should be a single word.\n')
            return
        else:
            cmd_func(client)

    return parse_func


#----------------------------------------------------------------------Singular

def singular(cmd_func):

    """Decorator to enforce single argument commands."""

    def parse_func(client):
        args = client.verb_args
        if len(args) != 1:
            client.send('That command requires a subject.\n')
            return
        else:
            cmd_func(client, args[0])

    return parse_func


#---------------------------------------------------------------------Monologue

def monologue(cmd_func):

    """Decorator to combine verb args into a single string."""

    def parse_func(client):
        args = client.verb_args
        if not len(args):
            client.send('Verb is missing who or what.\n')
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
            client.send('Verb is missing a subject and message.\n')
            return
        elif len(args) == 1:
            client.send('Verb is missing a message.\n')
            return
        else:
            target = args.pop(0)
            msg = ' '.join(args)
            cmd_func(client, target, msg)
        return parse_func 

  

