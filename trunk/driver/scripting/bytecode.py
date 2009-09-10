# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   driver/scripting/bytecode.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

from driver.error import BogScriptError

class ByteCompiler(object):

    """
    Attempts to compile a snippet of auto-generated code into Python bytecode. 
    """

    def __init__(self, pycode=''):
      
        self.pycode = pycode
        self.bytecode = None
        self._encode()

    def dump(self):
        
        lst = ''
        lines = self.pycode.split('\n')
        for number, line in enumerate(lines):
            lst += '|%.2d|%s\n' % (number + 1, line) 
        return lst

    def _encode(self):

        try:
            self.bytecode = compile(self.pycode, 'parsed_script', 'exec')

        except SyntaxError, error:
            raise BogScriptError("Bytecode Compile Error: %s\n" % error)




