#------------------------------------------------------------------------------
#   File:       speech.py
#   Purpose:    communication based abilities
#   Author:     Jim Storch
#------------------------------------------------------------------------------

from server import shared

def tell(client, target_handle, message):

    target = shared.HANDLE_DICT[target_handle]

    if client == target:
        target.send('^M  You tell yourself, %s\n' % message)

    else:
        target.send('^M  %s tells you, %s\n' % (client.name, message))


