# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   File:       mudlib/command/new_char.py
#   Author:     Jim Storch
#------------------------------------------------------------------------------

REJECT_NAMES = []

from mudlib.shared import RACES
from mudlib.shared import GUILDS
from driver.dbms.map import check_name
from driver.dbms.map import save_new_body

"""Functions for creating a new character."""


#------------------------------------------------------------------------Create

def create(client):

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
        client.send("Please use the format 'name Charactername'.")
        return

    _name = client.verb_args[0]
   
    if len(_name) < 3:
        client.send("That name is too short.")
        return

    if len(_name) > 30:
        client.send("That name is too long.")
        return       

    client.body.name = _name
    client.send("Your name is now %s." % _name)    
    review(client)


#------------------------------------------------------------------------Gender

def gender(client):
    if len(client.verb_args) != 1:
        client.send("Please use the format 'gender [male|female]'.")
        return

    _gender = client.verb_args[0].lower()

    if _gender != 'male' and _gender != 'female':
        client.send("Gender must be 'male' or 'female'.")
        return

    client.body.gender = _gender
    client.send("Your gender is now %s." % _gender)
    review(client)


#--------------------------------------------------------------------------Race

def race(client):

    if len(client.verb_args) != 1:
        client.send("Please use the format 'race racename'.")
        return

    _race = client.verb_args[0].lower()

    if _race not in RACES:
        client.send("That is not a playable race.")
        return        

    client.body.race = _race
    client.send("Your race is now %s." % _race)
    review(client)


#-------------------------------------------------------------------------Guild

def guild(client):

    if len(client.verb_args) != 1:
        client.send("Please use the format 'guild guildname'.")
        return

    _guild = client.verb_args[0].lower()

    if _guild == 'wizard':
        client.send(
            "You must first solve the riddle of 'Not just no...'")
        return

    if _guild not in GUILDS:
        client.send("That is not a playable guild.")
        return   

    client.body.guild = _guild
    client.send("Your guild is now %s." % _guild)
    review(client)


#----------------------------------------------------------------------Password

def password(client):

    if len(client.verb_args) != 1:
        client.send("Please use the format 'password yourpassword'.")
        return

    _password = client.verb_args[0]
   
    if len(_password) < 3:
        client.send("That password is too short.")
        return

    if len(_password) > 40:
        client.send("That password is too long.")
        return       

    client.body.password = _password
    client.send("Your password is now %s." % _password)
    review(client)


#------------------------------------------------------------------------Review

def review(client):
    client.send("\n\nCurrent character selections:\n")
    client.send("  name     %s\n" % client.body.name)
    client.send("  gender   %s\n" % client.body.gender)
    client.send("  race     %s\n" % client.body.race)
    client.send("  guild    %s\n" % client.body.guild)
    client.send("  password %s\n" % client.body.password)
    client.send(
        "Try 'help create' for more information or 'done' if finished.\n")

#--------------------------------------------------------------------------Done

def save(client):
    
    if client.body.name == '':
        client.send('You must select a name first.\n')
  
    elif client.body.gender == '':
        client.send('You must select a gender first.\n')

    elif client.body.race == '':
        client.send('You must select a race first.\n')

    elif client.body.guild == '':
        client.send('You must select a guild first.\n')

    elif client.body.password == '':
        client.send('You must select a password first.\n')    
 
    else:
        client.send('Saving your new character...')
    
    save_new_body(body)
    
