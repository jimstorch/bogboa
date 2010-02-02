# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/action/__init__.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

"""
Action Function Library
-----------------------

Actions are called by Commands, Abilities, and Scripts.  It is assumed that
validation has already occurred above this level, therefore no argument
testing or exception raising will be attempted.

In other words, don't call take_item() without knowing that the actor has it.
"""

from mudlib.action.stat_acts import *
from mudlib.action.move_acts import *
from mudlib.action.speech_acts import *
from mudlib.action.inventory_acts import *
