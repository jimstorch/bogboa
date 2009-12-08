# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/usr/cmd_account.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

import uuid

from mudlib.sys import shared
from mudlib.sys.log import THE_LOG
from mudlib.sys.config import LOBBY_UUID
from mudlib.sys.config import START_UUID

from mudlib.dat.map import check_name
#from mudlib.dat.map import save_new_body
from mudlib.dat.map import check_login
#from mudlib.dat.map import load_body
from mudlib.dat.map import ban_ip
from mudlib.dat.map import record_visit
#from mudlib.dat.map import last_on
from mudlib.usr.cmd_speech import broadcast


"""Functions for creating a new character."""


#------------------------------------------------------------------------Create

def create(client):

    """Grant a lobby client the needed commands to create a character."""

    client.revoke_command_silent('load')
    client.revoke_command_silent('create')
    client.grant_command('name')
    client.grant_command('gender')
    client.grant_command('race')
    client.grant_command('guild')
    client.grant_command('password')
    client.grant_command('review')
    client.grant_command('save')
    review(client)


#--------------------------------------------------------------------------Name

def name(client):

    if len(client.verb_args) != 1:
        client.alert("Please use the format 'name Charactername'.")
        return

    _name = client.verb_args[0]

    if len(_name) < 3:
        client.alert("That name is too short.")
        return

    if len(_name) > 30:
        client.alert("That name is too long.")
        return

    if check_name(_name):
        client.alert("Sorry, that name is not available.")
        return

    ###########################################################################
    ## OMG, I'm so sick of entering this
    ## TODO: remove this later.
    client.send('Dev auto setting junk...')
    client.body.race = 'human'
    client.body.gender = 'male'
    client.body.guild = 'figher'
    client.body.password = 'x'
    ###########################################################################

    client.body.name = _name
    client.inform("Your name is now %s." % _name)
    review(client)


#------------------------------------------------------------------------Gender

def gender(client):
    if len(client.verb_args) != 1:
        client.alert("Please use the format 'gender [male|female]'.")
        return

    _gender = client.verb_args[0].lower()

    if _gender != 'male' and _gender != 'female':
        client.alert("Gender must be 'male' or 'female'.")
        return

    client.body.gender = _gender
    client.inform("Your gender is now %s." % _gender)
    review(client)


#--------------------------------------------------------------------------Race

def race(client):

    if len(client.verb_args) != 1:
        client.alert("Please use the format 'race racename'.")
        return

    _race = client.verb_args[0].lower()

    if _race not in shared.RACES:
        client.alert("That is not a playable race.")
        return

    client.body.race = _race
    client.inform("Your race is now %s." % _race)
    review(client)


#-------------------------------------------------------------------------Guild

def guild(client):

    if len(client.verb_args) != 1:
        client.alert("Please use the format 'guild guildname'.")
        return

    _guild = client.verb_args[0].lower()

    if _guild == 'wizard':
        client.warn(
            "You must first solve the riddle of 'Not just no...'")
        return

    if _guild not in shared.GUILDS:
        client.alert("That is not a playable guild.")
        return

    client.body.guild = _guild
    client.inform("Your guild is now %s." % _guild)
    review(client)


#----------------------------------------------------------------------Password

def password(client):

    if len(client.verb_args) != 1:
        client.alert("Please use the format 'password yourpassword'.")
        return

    _password = client.verb_args[0]

    if len(_password) < 3:
        client.alert("That password is too short.")
        return

    if len(_password) > 40:
        client.alert("That password is too long.")
        return

    client.body.password = _password
    client.inform("Your password is now %s." % _password)
    review(client)


##-------------------------------------------------------------------------Email

#def email(client):

#    if len(client.verb_args) != 1:
#        client.send("Please use the format 'email name@domain.com'.")
#        return

#    _email = client.verb_args[0].lower()

#    if len(_email) < 8:
#        client.send("That email is too short.")
#        return

#    if len(_password) > 90:
#        client.send("That email is too long.")
#        return

#    client.body.email = email
#    client.send("Your email is now %s." % _email)
#    review(client)


#------------------------------------------------------------------------Review

def review(client):

    client.send("\nCurrent character selections:\n")
    client.send("  name     %s\n" % client.body.name)
    client.send("  gender   %s\n" % client.body.gender)
    client.send("  race     %s\n" % client.body.race)
    client.send("  guild    %s\n" % client.body.guild)
    client.send("  password %s\n" % client.body.password)
    client.send(
        "Try 'help create' for more information or 'save' if finished.")


#--------------------------------------------------------------------------Save

def save(client):

    if client.body.name == '':
        client.alert('You must select a name first.')

    elif client.body.gender == '':
        client.alert('You must select a gender first.')

    elif client.body.race == '':
        client.alert('You must select a race first.')

    elif client.body.guild == '':
        client.alert('You must select a guild first.')

    elif client.body.password == '':
        client.alert('You must select a password first.')

    else:
        client.inform('Saving your new character...')
        ## Assign a permanent UUID
        client.body.uuid = uuid.uuid4().get_hex()
        save_new_body(client.body)
        client.name = client.body.name
        client.body.is_visible = False
        ## Start Playing
        player_connect(client)

#--------------------------------------------------------------------------Load

def load(client):

    if len(client.verb_args) != 2:
        client.alert("Please use the format 'load name password'.")
        return

    name = client.verb_args[0]
    password = client.verb_args[1]

    if check_login(name, password):

        if shared.is_online(name.lower()):
            THE_LOG.add("?? Attempt to use active '%s' from %s" %
                (name, client.origin()))
            client.warn("That account is already in use.")
            return

        else:
            client.inform("Welcome back, %s. " % name)
            client.send("Your last visit was %s." % last_on(name))
            load_body(client.body, name)
            client.name = name
            ## Start Playing
            record_visit(name, client.conn.addr)
            player_connect(client)

    else:
        client.login_attempts += 1
        client.alert("Character name or password error.")

        if client.login_attempts > 3:
            THE_LOG.add("?? Suspicious login guessing '%s'/'%s' from %s" %
                (name, password, client.origin()))

        ## Watch for excessive login guesses and if, so, ban them
        if client.login_attempts > 30:
            ban_ip(client.conn.addr, 'account.py',
                'Auto-banned for 30+ consecutive login guesses.')
            client.deactivate()


#------------------------------------------------------------Player Command Set

def player_command_set(client):

    """
    Grant the player the normal set of user commands.
    """

    ## Start with a clean slate
    client.clear_commands()

    ## Start Granting
    ## change these to grant_command_silect() if too spammy
    client.grant_command('north')
    client.grant_command('south')
    client.grant_command('east')
    client.grant_command('west')

    client.grant_command('tell')
    client.grant_command('reply')
    client.grant_command('say')
    client.grant_command('emote')
    client.grant_command('ooc')
    client.grant_command('shout')

    client.grant_command('help')
    client.grant_command('commands')
    client.grant_command('quit')

    client.grant_command('kick')
    client.grant_command('time')
    client.grant_command('date')
    client.grant_command('uptime')
    client.grant_command('ansi')
    client.grant_command('stats')
    client.grant_command('topics')
    client.grant_command('look')
    client.grant_command('shutdown')
    client.grant_command('take')

#----------------------------------------------------------------Player Connect

def player_connect(client):

    """
    Given a newly created or loaded character, transfer them from the lobby
    to the game world.
    """

    ## Log the terminal type for general info
    THE_LOG.add('tt %s is using %s' % (client.name,
        client.conn.terminal_type))

    ## Assing a normal set of player commands
    player_command_set(client)

    ## Calculate stats
    client.body.reset_stats()

    ## Remove client from the lobby list and lobby room
    shared.ROOMS[LOBBY_UUID].on_exit(client.body)
    shared.LOBBY.remove(client)

    broadcast('^g%s is now online.^w' % client.name)

    ## Add client to the player's list
    shared.PLAYERS.append(client)
    shared.BY_NAME[client.name.lower()] = client

    ## If the client has no room, place them at the start
    if client.body.room == None or client.body.room.uuid == LOBBY_UUID:
        client.body.room = shared.find_room(START_UUID)

    ## And walk in
    client.body.is_visible = True
    client.body.room.on_enter(client.body)
