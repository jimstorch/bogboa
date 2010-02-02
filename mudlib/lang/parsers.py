# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/lang/parsers.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

"""
Decorator functions to parse and error check arguments for player commands and
general search functions.
"""

from mudlib.sys.error import BogCmdError
from mudlib.lang import create_keyset

def blank(cmd_func):
    """
    Decorator to enforce zero arguments.
    """
    def parse_func(player):
        args = player.verb_args
        if len(args):
            raise BogCmdError('That command does not use parameters.')
        else:
            cmd_func(player)
    return parse_func


def singular(cmd_func):
    """
    Decorator to enforce single parameter commands.
    """
    def parse_func(player):
        args = player.verb_args
        if len(args) == 0:
            raise BogCmdError('That command requires a parameter.')
        elif len(args) > 1:
            raise BogCmdError('Too many parameters -- use one.')
        else:
            cmd_func(player, args[0])
    return parse_func


def none_or_one(cmd_func):
    """
    Decorator that accepts zero or one parameters.
    """
    def parse_func(player):
        args = player.verb_args
        if len(args) > 1:
            raise BogCmdError('Too many parameters -- use one.')
        elif len(args) == 1:
            arg = args[0]
        else:
            arg = None
        cmd_func(player, arg)
    return parse_func


def monologue(cmd_func):
    """
    Decorator to combine all args into a single string.
    """
    def parse_func(player):
        args = player.verb_args
        if not len(args):
            raise BogCmdError('Missing subject.')
        else:
            msg = ' '.join(args)
            cmd_func(player, msg)
    return parse_func


def dialogue(cmd_func):
    """
    Decorator to identify a target and combine remaining arguments.
    """
    def parse_func(player):
        args = player.verb_args
        if len(args) == 0:
            raise BogCmdError('Command is missing a subject and message.')
        elif len(args) == 1:
            raise BogCmdError('Command is missing a message.')
        else:
            name = args.pop(0)
            target = shared.find_player(name)
            if target == None:
                raise BogCmdError('%s is not online.' % name)
            msg = ' '.join(args)
            cmd_func(player, target, msg)
    return parse_func


def set_or_show(cmd_func):
    """
    Set/Unset decorator parser.  Returns:

    None for no args -- display the current setting.
    True for yes-like args -- turn it on.
    False for no-like args -- turn it off.
    """
    def parse_func(player):
        args = player.verb_args
        if len(args) > 1:
            raise BogCmdError('Too many parameters.')
        if len(args) == 0:
            setting = None
        else:
            arg = args[0].lower()

            if arg in ['yes', 'true', '1', 'on']:
                setting = True

            elif arg in ['no', 'false', '0', 'off']:
                setting = False

            else:
                raise BogCmdError('Please use a yes/no or on/off parameter.')
        cmd_func(player, setting)
    return parse_func


def online_player(cmd_func):
    """
    Decorator to target an online player.
    """
    def parse_func(player):
        args = player.verb_args
        if len(args) != 1:
            raise BogCmdError('That command requires a player name.')
        else:
            name = args[0]
            target = shared.find_player(name)
            if target == None:
                raise BogCmdError('Player not found online.')
            cmd_func(player, target)
    return parse_func


def arg_keyset(cmd_func):
    """
    Generate a keyset from the command arguments.
    """

    def parse_func(player):
        args = player.verb_args
        if len(args) == 0:
            raise BogCmdError('Your verb is missing a subject.')
        else:
            name = ' '.join(args)
            ks = create_keyset(name)
            if not ks:
                raise BogCmdError('Entry too ambiguous to match.')
            cmd_func(player, ks)
    return parse_func



#def name_and_qty(cmd_func):
#    ##TODO: this is a mess
#    """
#    Decorator to parse quantity and name of item(s) to select.
#    Qty == -1 for all.
#    """
#    def parse_func(client):
#        args = client.verb_args
#        count = len(args)
#        if count == 0:
#            client.alert('That command needs a subject.')
#            return
#        elif count == 1:
#            arg = args[0].lower()
#            if arg.isdigit():
#                client.alert("%s of what?" % arg)
#                return
#            if arg in ('all', 'everything', 'stuff', 'loot'):
#                args = ['all',]
#                qty = -1
#            else:
#                qty = 1
#        else:
#            arg = args[0].lower()
#            ## Is the first argument a number?
#            if arg.isdigit():
#                if len(arg) > 9:
#                    client.alert("That's a bit much.")
#                    return
#                qty = int(arg)
#                args = args[1:]
#            elif arg in ('a', 'an', 'one'):
#                qty = 1
#                args = args[1:]
#            elif arg in ('all', 'every'):
#                qty = -1
#                args = args[1:]
#            else:
#                qty = 1
#        phrase = ' '.join(args)
#        cmd_func(client, phrase, qty)
#    return parse_func
