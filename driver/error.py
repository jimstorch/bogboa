# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   driver/error.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

class BogError(Exception):

    """Base class for errors in BogBoa."""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class BogCmdError(BogError):

    """Custom exception to notify client of failed commands."""    


class BogScriptError(BogError):

    """Custom exception to raise scripting errors."""    


class BogYAMLError(BogError):

    """Custom exception to raise YAML parsing errors."""    


