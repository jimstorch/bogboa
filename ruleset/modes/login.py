#------------------------------------------------------------------------------
#   File:       login.py
#   Purpose:    validate a user login
#   Author:     Jim Storch
#------------------------------------------------------------------------------

from ruleset.dbm.mapping import check_name
from ruleset.dbm.mapping import check_password
#from gameplay.dbm.mapping import login_character


GREETING = """
  ^cPlease enter your character name:
"""


HELP = """
"""


#---[ Login Class ]------------------------------------------------------------ 

class Login(object):

    def __init__(self, conn):
                        
        self.active = True  
        self.conn = conn

        # Mode specific
        self.confusion = 0
        self.state = 'base'
        self.name = None
        self.password = None

        conn.send(GREETING)
        self.conn.prompt()    


    #---[ Process Command ]----------------------------------------------------

    def process_command(self):
    
        cmd = self.conn.get_cmd()





    #--[ Deactivate Method ]---------------------------------------------------            
                    
    def deactivate(self):

        # 'self' gets deleted by control.purge_dead_clients()
        self.conn.active = False 

        # conn gets deleted by async.ThePortManager.poll()  
        self.active = False
