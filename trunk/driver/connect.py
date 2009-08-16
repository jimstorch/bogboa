# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   File:       driver/connect.py
#   Author:     Jim Storch
#------------------------------------------------------------------------------

from mudlib import shared
from mudlib.client import Client
from driver.config import LOBBY_UUID


#lobby_uuid = "0c9997b9-5068-46d9-a245-12991bdf3f17"


#-----------------------------------------------------------------Lobby Connect

def lobby_connect(conn):

    client = Client()
    client.conn = conn
    client.active = True
    shared.LOBBY.append(client)
    #print client
    ## Fire the on_enter event
    shared.ROOMS[LOBBY_UUID].on_enter(client.body)



