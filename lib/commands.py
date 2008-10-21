##-----------------------------------------------------------------------------
##  File:       lib/commands.py
##  Author:     Jim Storch
##-----------------------------------------------------------------------------


ALIAS = {}

## Don't forget to enter single item tuples with a comma inside: (foo,)
alias_list = (

    ## Movement
    ('north', 'nor', 'n'),
    ('east', 'eas', 'e'),
    ('south', 'sou', 's'),
    ('west', 'wes', 'w'),
    ('up', 'u', 'climb'),
    ('down', 'dn', 'd'),
    ('recall', 'home'),
    ('enter',)

    ## Communication
    ('say', '/s'),
    ('shout', 'yell', '/y'),
    ('tell', 'whisper', '/t', '/w'),
    ('reply', '/r'),
    ('emote', '/em', ':'),

    ## Information
    ('help', '?'),
    ('score', 'played', 'info'),
    ('time', 'date', 'clock'),
    ('inventory', 'i', 'inven'),

    ## Interaction
    ('do', 'cast', 'doability', 'spell'),
    ('look', 'l'),
    ('attack', 'kill', 'atk', 'slay', 'att'),
    ('target', 'tar'),
    ('search',),

    ## System
    ('quit', 'exit', 'logoff'),

    ## Wizardry
    ('ban',),
    ('kick', 'punt'),
    ('summon',)
    ('teleport', 'port'),
    ('zap',)

    )
    
## Map every alias to the first command in each line.
## Saves me typing a dictionary by hand.
for commands in alias_list:
    for command in commands:
        ALIAS[command] = commands[0]

