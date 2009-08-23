# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   driver/connect.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

import random

from mudlib import shared
from mudlib.client import Client
from driver.config import LOBBY_UUID


#lobby_uuid = "0c9997b9-5068-46d9-a245-12991bdf3f17"

greeting = """^kb%s^s
     ____              ____              
    |  _ \            |  _ \             
    | |_) | ___   __ _| |_) | ___   __ _ 
    |  _ < / _ \ / _` |  _ < / _ \ / _` |
    | |_) | (_) | (_| | |_) | (_) | (_| |
    |____/ \___/ \__, |____/ \___/ \__,_|
                  __/ |                  
    Test Server  |___/  Horribly Unstable^w""" 
                   


BCOLORS = ['^R', '^B', '^C', '^M', '^W', '^G'] 

#-----------------------------------------------------------------Lobby Connect





def lobby_connect(conn):

    client = Client()
    client.conn = conn
    client.send_nowrap(greeting % random.choice(BCOLORS))
    conn.request_terminal_type()
    conn.request_naws()
    client.active = True
    shared.LOBBY.append(client)
    #print client
    ## Fire the on_enter event
    shared.ROOMS[LOBBY_UUID].on_enter(client.body)



