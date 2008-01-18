#------------------------------------------------------------------------------
#   File:       commands.py
#   Purpose:
#   Author:     Jim Storch
#------------------------------------------------------------------------------


class Commander(object):

    def __init__(self, **kwds):
        self.__dict__.update(kwds)
        ## Populate the command dictionary with all class methods that
        ## start with 'cmd_'.  This is used to match command tokens to 
        ## class methods.
        self.cmd_dict = {}
        cmd_list = [ fn for fn in dir(self) if fn.startswith('cmd_') ]
        for cmd in cmd_list:
            ## Cut off the leading 'cmd_' for the key token
            token = script[4:]
            ## This much introspection feels kinda fragile...
            self.cmd_dict[token] = self.__class__.__dict__[cmd]
            

    def cmd_say(self, client, text):
        pass
 
    def cmd_shout(self, client, text):
        pass       
        
    def cmd_tell(self, client, target, text)
        pass        
        
    def cmd_quit(self, client):
        pass
        
        
#--[ Shared Instance ]---------------------------------------------------------

the_commander = Commander()

#------------------------------------------------------------------------------

