#------------------------------------------------------------------------------
#   File:       svr.py
#   Purpose:
#   Author:     Jim Storch
#------------------------------------------------------------------------------

from server import shared

#--[ General Player Commands ]-------------------------------------------------

def say(client, text):
    pass
    
def shout(client, text):
    pass
    
def tell(client, target, text):
    pass

def emote(client, text);
    pass

def who(client):
    pass
    
def consider(client, target):
    pass

def inspect(client, target):
    pass
    
def quit(client):
    pass


#--[ GM Commands ]-------------------------------------------------------------

def set_note(name, text):
    pass

def whom(name):
    pass

def set_motd(text):
    pass

def kick(name):
    pass

def suspend(name):
    pass

def unsuspend(name):
    pass

def list_suspensions():
    pass

def ban(name):
    pass

def unban(name):
    pass

def list_bans():
    pass

def ban_ip(address):
    pass

def unban_ip(address):
    pass
    

#--[ Scripting Commands ]------------------------------------------------------

def inform(client, text):
    pass

def inform_all(text):
    pass
    
def inform_all_but(client, text):
    pass


#--[ ANSI Text Decorations ]---------------------------------------------------    
    
def color_none(client):
    pass
    
def color_red(client):
    pass

def color_bright_red(client):
    pass


