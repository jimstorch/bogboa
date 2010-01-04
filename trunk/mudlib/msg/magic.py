# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/msg/magic.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

"""
Magic related action messages.
"""

from mudlib.msg.msg_base import BaseMsg


#--------------------------------------------------------Begin Casting Messages

class BeginHealSpell(BaseMsg):
    source = 'You begin chanting {val} for {tname}.\n'
    viewer = '{sname} looks at {tname} and begins to chant.\n'


class BeginDmgSpell(BaseMsg):
    source = 'You begin invoking {val} at {tname}.\n'
    viewer = '{sname} traces arcane gestures towards {tname}.\n'


#---------------------------------------------------------Casting Fail Messages

class SpellFizzle(BaseMsg):
    source = 'Your {val} spell directed at {tname} fizzles.\n'
    viewer = "{sname}'s magic towards {tname} fizzles.\n" 


#-------------------------------------------------------Casting Resist Messages



#------------------------------------------------------Casting Success Messages

