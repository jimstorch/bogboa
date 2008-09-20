#------------------------------------------------------------------------------
#   File:       driver/scripting/batch.py
#   Author:     Jim Storch
#------------------------------------------------------------------------------

#from driver.clock.scheduler import THE_SCHEDULER


class Batch(object):

    """
    Represents a series of function calls with an evironmental dictionary.
    """

    def __init__(self, env, cmds):

        self.env = env
        self.cmds = cmds

    
