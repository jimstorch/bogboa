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



