#------------------------------------------------------------------------------
#   File:       base.py
#   Purpose:
#   Author:     Jim Storch
#------------------------------------------------------------------------------

from server.decorate import colorize

class BaseMode(object):

    def __init__(self, conn):
    
        self.conn = conn
        self.active = True   

    #--[ Get Cmd ]-------------------------------------------------------------

    def get_cmd(self):
        return self.conn.get_cmd()
    

    #--[ Send ]----------------------------------------------------------------        

    def send(self, text):
        ## convert Python linebreaks to Telnet/DOS
        text = text.replace('\n', '\r\n')
        self.conn.send(colorize(text, self.conn.use_ansi))

    #---[ Prompt ]-------------------------------------------------------------

    def prompt(self):
        """Show the command entry prompt on the DE's screen."""
        self.send('\r\n^G>^w ')


    #--[ Deactivate Method ]---------------------------------------------------
                    
    def deactivate(self):

        # 'self' gets deleted by control.purge_dead_clients()
        self.conn.active = False 

        # conn gets deleted by async.ThePortManager.poll()  
        self.active = False     
