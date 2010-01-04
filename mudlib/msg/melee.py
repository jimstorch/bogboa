# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/msg/melee.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

"""
Melee related action messages.
"""

from mudlib.msg.msg_base import BaseMsg


class SlashMsg(BaseMsg):
    source = 'You slash {tname}.\n'
    viewer = '{sname} slashes {tname}.\n'


class BashMsg(BaseMsg):,lp =
    source = 'You bash {tname}.\n'
    viewer = '{sname} bashes {tname}.\n'



