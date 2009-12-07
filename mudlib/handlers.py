# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   driver/connect.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

import random

from mudlib import shared
from mudlib.player import Player
from driver.config import LOBBY_UUID


greeting = """^kb%s^s
     ____              ____
    |  _ \  Amazingly |  _ \   Incomplete
    | |_) | ___   __ _| |_) | ___   __ _
    |  _ < / _ \ / _` |  _ < / _ \ / _` |
    | |_) | (_) | (_| | |_) | (_) | (_| |
    |____/ \___/ \__, |____/ \___/ \__,_|
                  __/ |
    Test Server  |___/  Horribly Unstable^w"""



BCOLORS = ['^R', '^B', '^C', '^M', '^G', '^Y',
    '^r', '^b', '^c', '^m', '^g', '^y', ]

#--------------------------------------------------------------------On Connect

def on_connect(client):

    player = Player()
    player.client = client
    client.send_nowrap(greeting % random.choice(BCOLORS))
    client.request_terminal_type()
    client.request_naws()
    player.active = True
    shared.LOBBY.append(player)
    ## Fire the on_enter event
    shared.ROOMS[LOBBY_UUID].on_enter(player.body)


#-----------------------------------------------------------------On Disconnect

def on_disconnect(client):
    pass
