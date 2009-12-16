# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/actor/actor.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

"""
Base Class for PCs and NPCs.
"""

class Actor(object):

    def __init__(self):

        self.profile = {}
        self.resources = {}
        self.stats = {}
        self.worn = {}
        self.carried = {}
        self.target = None
