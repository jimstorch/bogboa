# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   driver/error.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------


class BogCmdError(Exception):

    """Custom exception to notify client of failed commands."""    

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class BogScriptError(Exception):

    """Custom exception to raise scripting errors."""    

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class BogYAMLError(Exception):

    """Custom exception to raise YAML parsing errors."""    

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
