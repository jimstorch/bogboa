# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   File:       driver/log.py
#   Author:     Jim Storch
#------------------------------------------------------------------------------

"""Module contains the Log() class."""

import time
       

#---------------------------------------------------------------------------Log

class Log(object):

    """A very simple logging system for screen and file."""

    def __init__(self, filename, append = True):
        
        if append:
            mode = 'a'
        else:
            mode = 'w'
   
        self.file = open(filename, mode)

    def add(self, string):
        
        """Add the given string to the log and echo to the screen."""
        
        now = time.strftime('%Y-%m-%d %H:%M:%S ')
        self.file.write('\n' + now + string)
        self.file.flush()
        print now, string
       
    
#--[ Global Instance ]---------------------------------------------------------

THE_LOG = Log('server.log', append=True)
#BUG_LOG = Log('bugs.log', append=True)    
