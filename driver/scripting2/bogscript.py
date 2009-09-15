# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   driver/scripting2/bogscript.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

from driver.log import THE_LOG
from driver.scripting2.dsl import lexer
from driver.scripting2.dsl import pygen
from driver.scripting2.dsl import bytegen


#---------------------------------------------------------------Compile Script

def compile_script(bogscript):
    
    """
    Take a snippet of bogscript and compile it into python bytecode.
    """

    ## Step 1: Convert source script into tokens
    tokens = lexer(bogscript)
    #print tokens

    ## Step 2: Convert tokens into Python Source
    pycode = pygen(tokens)
    #print '\n' + pycode + '\n'

    ## Step 3: Compile Python Source into bytecode
    bytecode = bytegen(pycode)

    return bytecode


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

