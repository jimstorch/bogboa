# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/scripting/__init__.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

from mudlib.scripting import of_effects
from mudlib.scripting import of_items
from mudlib.scripting import of_mobs
from mudlib.scripting import of_players
from mudlib.scripting import of_rooms


"""
Build a script environment where all script functions are local.
"""


SCRIPT_ENV = {}

SCRIPT_ENV.update(of_effects.__dict__)
SCRIPT_ENV.update(of_items.__dict__)
SCRIPT_ENV.update(of_mobs.__dict__)
SCRIPT_ENV.update(of_players.__dict__)
SCRIPT_ENV.update(of_rooms.__dict__)
