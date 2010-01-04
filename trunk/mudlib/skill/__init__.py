# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/skill/__init__.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

"""
Skills
------

Skills are numeric values that represent the Actor's measure of talent when
it comes to performing acts in given categories.

Potentially, Actor's get 10 points of skill per character level, but these are
capped by skill modifiers of the Actor's Guild.  For example, the Fighters'
Guild might have a "healing_magic" skill modifier of 0.00, which caps members
of that guild at zero forever.

Skills may recieve a bonus or penalty based on character stats. The combination
of current skill + stat bonus is called the Rating.  Ratings are the values
used when testing for success/failure of an action or a magnitude of effect. 
"""

from mudlib.skill.skill_math import *
from mudlib.skill.passive import *
from mudlib.skill.defense import *
from mudlib.skill.melee import *
from mudlib.skill.ranged import *
from mudlib.skill.magic import *
from mudlib.skill.crafting import *




