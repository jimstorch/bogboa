# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/sys/log.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

"""
File and TTY logging.
"""

import time


class Log(object):
    """
    A very simple logging system for screen and file.
    """

    def __init__(self, filename, append = True):
        if append:
            mode = 'a'
        else:
            mode = 'w'
        self.file = open(filename, mode)

    def add(self, string):
        """
        Add the given string to the log and echo to the screen.
        """
        now = time.strftime('%Y-%m-%d %H:%M:%S ')
        self.file.write('\n' + now + string)
        self.file.flush()
        print now, string


