# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   driver/bogscript.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

"""
The Problem
===========

Python was not designed to be a sandbox.  Any python program has access to
file and network operations, so giving builders the ability to directly write
python code is just too risky.  The danger ranges from elaborate in-game 
cheats to malicious attacks against the host server itself.    

Besides that, we want scripted events to stay dead simple for the sake of
speed.  You don't want builders trying to code blackjack tables in scripts.
Add gambling code to the API and then whitelist the function calls for
scripting (See driver.scripting.whitelist).  


BogScript
=========

Bogscript is a simple, psuedo-language used to define custom event actions. 
For the sake of clarity, when I say 'scripting' I mean psuedo-code written in
BogScript, not Python (even though Python is a scripting language).  

The task here to take a snippet of BogScript from a YAML config file and 
convert it into Python bytecode for fast processing. The snippets can be
defined for any event such as 'on_equip' for a helmet -- where we might want
to add to the player's armor and maybe boost a stat.  The effects would be
reversed in the helmet's 'on_remove' event.

BogScript snippets should be short and simple with minimal conditionals.  All
heavy lifting should occur in API calls (mud.functions).

Once converted into Python bytecode, scripts can be marshalled for storage
as binary which would let us avoid have to re-parse every YAML file each time
the server is re-started. 


Restrictions
============     

No looping -- you do NOT want 'while(True):' in a event script.
No imports -- for obvious reasons. 
No creating objects, functions, or variables (may revisit that last one).
Scripts may only call whitelisted function and methods.


Permissions
===========

Whitelisted API calls:

    adj_gold(-20)
    set_flag('funny_smelling')

Conditionals:

    if, elif, else    

Keywords:

    and, or, not

Blocks:

    {}

Math:

    * /  -  +


Remember
========

Even with careful sanitation of scripts, there's nothing to prevent a builder
from writing a NPC script that gives the player 100 gold anytime they utter
the word 'plugh' or creating an item that gives stats when you equip it but 
does not reverse them when you remove it, thus creating a stat inflation
handpump.  

Audit scripts and only work with builders you trust.
"""

from driver.scripting.token import Tokenizer
from driver.scripting.pygen import PyGen
from driver.scripting.bytecode import ByteCompiler
from driver.log import THE_LOG

#----------------------------------------------------------------Compile Script

def compile_script(bogscript, event_name, source_obj):
    
    """
    Take a snippet of bogscript and compile it into python bytecode.
    """

    #print bogscript

    ## Step 1: Convert source script into tokens
    tk = Tokenizer(bogscript)
    msg = tk.tokenize()
    if msg != '':
        return (msg, None)

    #for token in tk.tokens:
    #    print token

    ## Step 2: Convert tokens into Python Source
    pg = PyGen(tk.tokens)
    msg = pg.generate()
    if msg != '':
        return (msg, None)

    #print pg.pycode

    ## Step 3: Compile Python Source into bytecode
    bc = ByteCompiler(pg.pycode)
    msg = bc.encode()
    if msg != '':
        return (msg, None)

    ## Return 
    return ('', bc.bytecode)


#--------------------------------------------------------------Check Event Name

def check_event_name(event_name, source_obj):

    """
    Check a script's event name against the class methods of the target class.
    """
    ## Does the event name match a class method?
    if event_name not in source_obj.__class__.__dict__:
        THE_LOG.add ( "WARNING! Unknown event '%s' given for "
            "room '%s' in module '%s'." % 
            (event_name, source_obj.name, source_obj.module) )


