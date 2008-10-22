##-----------------------------------------------------------------------------
##  File:       lib/commands.py
##  Author:     Jim Storch
##-----------------------------------------------------------------------------


ALIAS = {}

## Don't forget to enter single item tuples with a comma inside: (foo,)
alias_list = (

    ## Movement
    ('north', 'nor', 'n', '8'),
    ('east', 'eas', 'e', '6'),
    ('south', 'sou', 's', '2'),
    ('west', 'wes', 'w', '4'),
    ('up', 'u', 'climb', '9'),
    ('down', 'dn', 'dwn', 'd', '3'),
    ('recall', 'home'),
    ('enter',)

    ## Communication
    ('say', '/s'),
    ('shout', 'yell', '/y'),
    ('ooc',),
    ('tell', 'whisper', '/t', '/w'),
    ('reply', 'r', '/r'),
    ('emote', '/em', ':'),

    ## Information
    ('help', '?', 'info'),
    ('score', 'played','stats'),
    ('time', 'date', 'clock'),
    ('inventory', 'i', 'inven'),

    ## Interaction
    ('don', 'wear', 'eqip'),
    ('remove', 'unequip'),
    ('take', 'get', 'pickup', 'grab'),
    ('drop', 'discard', 'toss', 'throw')
    ('do', 'cast', 'doability', 'spell'),
    ('look', 'l', '5'),
    ('attack', 'kill', 'atk', 'slay', 'att'),
    ('target', 'tar'),
    ('search',),

    ## System
    ('quit', 'exit', 'logoff'),
    ('yes',),
    ('no',)

    ## Wizardry
    ('ban',),
    ('kick', 'punt'),
    ('summon',)
    ('teleport', 'port'),
    ('zap',)

    ## Silly
    ('verbose',),
    ('plugh', 'xyzzy'),
    ('pizza',),
    ('iddqd', 'idkfa'),
    )
    
## Map every alias to the first command in each line.
## Saves me typing a dictionary by hand.
for commands in alias_list:
    for command in commands:
        ALIAS[command] = commands[0]

