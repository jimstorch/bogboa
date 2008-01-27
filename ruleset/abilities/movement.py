#------------------------------------------------------------------------------
#   File:       movement.py
#   Purpose:    movement based abilities
#   Author:     Jim Storch
#------------------------------------------------------------------------------


#---[ North ]------------------------------------------------------------------

def north(client):
    """Move north, if able."""

    if 'north' in client.room.exits:
        leaving = client.room
        entering = leaving.exits['north']
        leaving.remove_player(client, 'to the north')
        entering.add_player(client, 'from the south')
    
    else:
        client.send('^yThe way North is obstructed.')

north.parser = None


#---[ North East]--------------------------------------------------------------

def north_east(client):
    pass

north_east.parser = None 


#---[ East ]-------------------------------------------------------------------

def east(client):
    pass

east.parser = None


#---[ South East ]-------------------------------------------------------------

def south_east(client):
    pass

south_east.parser = None


#---[ South ]------------------------------------------------------------------

def south(client):
    pass

south.parser = None


#---[ South West ]-------------------------------------------------------------

def south_west(client):
    pass

south_west.parser = None


#---[ West ]-------------------------------------------------------------------

def west(client):
    pass
    
west.parser = None


#---[ North West ]-------------------------------------------------------------

def north_west(client):
    pass

north_west.parser = None


#---[ Up ]---------------------------------------------------------------------

def up(client):
    pass

up.parser = None

#---[ Down ]-------------------------------------------------------------------

def down(client):
    pass

down.parser = None


#---[ Enter ]------------------------------------------------------------------

def enter(client):
    pass

enter.parser = None


#---[ Exit ]-------------------------------------------------------------------

def exit(client):
    pass

exit.parser = None
 

#---[ Recall ]-----------------------------------------------------------------

def recall(client):
    pass

recall.parser = None


