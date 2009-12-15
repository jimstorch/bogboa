# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/world/entity.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

from mudlib.world.profiler import Profiler


class Entity(Profiler):

    def __init__(self):

        self.profile = {}
        self.skills = {}
        self.target = None


    def
