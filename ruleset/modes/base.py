#------------------------------------------------------------------------------
#   File:       base.py
#   Purpose:
#   Author:     Jim Storch
#------------------------------------------------------------------------------

from ruleset import shared
from server.decorate import colorize

class BaseMode(object):

    def __init__(self, conn):
    
        self.conn = conn
        self.handle = None
        self.active = True   

    #---[ Del ]----------------------------------------------------------------

    def __del__(self):

#        print "Base destructor called"
        pass



    #--[ Get Cmd ]-------------------------------------------------------------

    def get_cmd(self):
        return self.conn.get_cmd()
    

    #--[ Send ]----------------------------------------------------------------        

    def send(self, text):
        ## convert Python linebreaks to Telnet/DOS
        text = '\r' + text + '\n^w'
        text = text.replace('\n', '\r\n')
        self.conn.send(colorize(text, self.conn.use_ansi))

    #---[ Prompt ]-------------------------------------------------------------

    def prompt(self):
        """Show the command entry prompt on the DE's screen."""
        #self.send('\r^G>^w ')
        self.conn.send(colorize('\r^G>^w '))


    #--[ Deactivate Method ]---------------------------------------------------
                    
    def deactivate(self):

        ## If we're in the HANDLE_DICT remove us 
        if shared.HANDLE_DICT.has_key(self.handle):
            del(shared.HANDLE_DICT[self.handle]) 

        ## 'self' gets deleted by control.purge_dead_clients()
        self.active = False

        ## conn gets deleted by async.ThePortManager.poll()  
        self.conn.active = False


        
     
