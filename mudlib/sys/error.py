# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/sys/error.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

class BogError(Exception):
    """
    Base class for errors in BogBoa.
    """
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


class BogCmdError(BogError):
    """
    Exception to notify client of failed commands.
    """
    pass

class BogClientError(BogError):
    """
    Exception to signal lost connection.
    """
    pass


class BogDepleteCond(BogError):
    """
    Exception to signal a depleted resource.
    """
    pass

class BogExceedCond(BogError):
    """
    Exception to signal a depleted resource.
    """
    pass

class BogScriptError(BogError):
    """
    Exception to raise scripting errors.
    """
    pass

class BogYAMLError(BogError):
    """
    Exception to raise YAML parsing errors.
    """
    pass
