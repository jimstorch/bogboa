# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   driver/bogscript.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

import sys

from driver.dsl import lexer
from driver.dsl import pygen
from driver.dsl import bytegen
from driver.error import BogScriptError


#----------------------------------------------------------------Compile Script

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


#---------------------------------------------------------------Process Scripts

def process_scripts(cfg, obj):

    """
    Given a cfg dictionary and a game object, compiles event snippets into
    Python bytecode and puts them into the object's event dictionary.
    """

    keys = cfg.keys()
    for key in keys:

        ## Look for script snippets that begin with 'on_'
        if key.startswith('on_'):
            event_name = key

            ## Issue warnings for events that don't match class methods
            if event_name not in obj.__class__.__dict__:
                THE_LOG.add("??  Warning unknown event '%s' in file %s." %
                    (event_name, obj.filename))

            else:
                script = cfg.pop(event_name)

                try:
                    code = compile_script(script)

                except BogScriptError, error:
                    THE_LOG.add('!! Script error in file %s' % obj.filename)
                    THE_LOG.add("!!   for event '%s'" % key)
                    THE_LOG.add('!!   %s' % error)
                    sys.exit(1)

                ## Map the event name to the compiled bytecode
                obj.scripts[event_name] = code

    return cfg
