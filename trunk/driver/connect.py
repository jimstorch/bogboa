##-----------------------------------------------------------------------------
##  File:       driver/connect.py
##  Author:     Jim Storch
##-----------------------------------------------------------------------------

from lib import shared
from lib.player import Player

lobby_uuid = "0c9997b9-5068-46d9-a245-12991bdf3f17"
anonymous_uuid = "2d9817b7-48e2-45a7-9fb7-606bdb4acdac"
guest_uuid = "f2f8003b-2097-45e7-b869-eba0bfd8c891"


def lobby_connect(conn):

    player = Player()
    player.conn = conn
    player.active = True
    player.name = 'Anonymous'
    player.room = shared.ROOM[lobby_uuid]
    player.sect = shared.SECT[guest_uuid]

    shared.LOBBY_LIST.append(player)


def game_connect(conn):
    pass   
