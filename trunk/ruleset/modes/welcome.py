#------------------------------------------------------------------------------
#   File:       welcome.py
#   Purpose:    initial login state
#   Author:     Jim Storch
#------------------------------------------------------------------------------

from server import shared
from ruleset.modes.login import Login
from ruleset.modes.new_character import NewCharacter

GREETING = """^kb^s

                  ^YWELCOME TO THE^C 
                     ____              ____              
                    |  _ \            |  _ \             
                    | |_) | ___   __ _| |_) | ___   __ _ 
                    |  _ < / _ \ / _` |  _ < / _ \ / _` |
                    | |_) | (_) | (_| | |_) | (_) | (_| |
                    |____/ \___/ \__, |____/ \___/ \__,_|
                                  __/ |                  
                                 |___/   
                                         ^YDevelopment Server
           
                 ^w^i Source available at bogboa.googlecode.com ^I
"""

HELP = """^c
  Valid commands currently are:

  ^Wcreate^c     - Create a new character to play on this server.
  ^Wlogin^c      - Login a character you created previously. 
  ^Whelp^c       - Show this message again.
  ^Wquit^c       - Disconnect from the server.
"""

#--[ Welcome Class ]-----------------------------------------------------------

class Welcome(object):

    def __init__(self, conn):
        self.active = True  
        self.conn = conn
        self.name = "UNKNOWN"
        
        conn.send(GREETING)
        conn.prompt()

    
    #--[ Process Command ]-----------------------------------------------------

    def process_command(self):
         
        cmd = self.conn.get_cmd().lower()
        #print cmd
    
        if cmd == 'quit':            
            self.deactivate()

        elif cmd == 'login':
            mode = Login(self.conn)
            shared.LOBBY_LIST.append(mode)
            self.active = False
            
        elif cmd == 'create':
            mode = NewCharacter(self.conn)
            shared.LOBBY_LIST.append(mode)
            self.active = False
            
        elif cmd == 'help':
            self.conn.send(HELP)
            self.conn.prompt()
        
        elif cmd == 'set ansi off':
            self.conn.use_ansi = False
            self.conn.send('ANSI color encoding turned off.')
            self.conn.prompt()
        
        else:
            self.conn.send("Unknown command.")
            self.confusion += 1
            if self.confusion == 4:
                self.conn.send("Try typing '^!help^1' if you're lost.")
                self.confusion = 0
            self.conn.prompt()
                

#--[ Deactivate Method ]-------------------------------------------------------
                    
    def deactivate(self):

        # 'self' gets deleted by control.purge_dead_clients()
        self.conn.active = False 

        # conn gets deleted by async.ThePortManager.poll()  
        self.active = False

       
