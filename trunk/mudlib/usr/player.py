# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/usr/player.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

#from mudlib.sys import shared
#from mudlib.sys.error import BogCmdError
#from mudlib.world.entity import Entity
#from mudlib.usr.verb import VERB_ALIAS
#from mudlib.usr.verb import VERB_HANDLER

from mublib.usr.user import User


#------------------------------------------------------------------------Client

class Player(User):

    def __init__(self, client, actor):

        User.__init__(self, client)
        self.actor = actor

    



