# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/usr/entant.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

#import shared
from mudlib.sys.error import BogCmdError
from mudlib.usr.user import User
from mudlib.usr.verb import VERB_ALIAS
from mudlib.usr.verb import VERB_HANDLER

#from driver.decorate import word_wrap


#------------------------------------------------------------------------Client

class Entrant(User):

    def __init__(self, client):

        User.__init__(self, client)

        self.login_attempts = 0
        self.name = 'Anonymous'         ## Changed to body name later


    #----------------------------------------------------------------Deactivate

    def deactivate(self):
        """Client disconnected or was kicked."""
        ## Unlink the player's body for garbage collecting

        if self.body and self.body.room:
            self.body.room.on_exit(self.body)

        if self.body and self.body.mind:
            self.body.mind = None
        self.body = None
        ## Remove from the name lookup
        if self.name.lower() in shared.BY_NAME:
            del shared.BY_NAME[self.name.lower()]
        ## Schedule for cleanup via driver.monitor.test_connections()
        self.active = False
        self.client.active = False
