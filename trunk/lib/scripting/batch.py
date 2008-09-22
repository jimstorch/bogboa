#------------------------------------------------------------------------------
#   File:       lib/scripting/batch.py
#   Author:     Jim Storch
#------------------------------------------------------------------------------

class Batch(object):

    """
    Represents a series of function calls with an evironmental dictionary.
    """

    def __init__(self):

        self.cmd_list = []

    def add(self, cmd):
        self.cmd_list.append(cmd)


    def execute(self, mob):

        for cmd in self.cmd_list:
            
            
