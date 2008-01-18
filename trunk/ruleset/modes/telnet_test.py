#------------------------------------------------------------------------------
#   File:       telnet_test.py
#   Purpose:    for trouble-shooting telnet negotiations
#   Author:     Jim Storch
#------------------------------------------------------------------------------

from ruleset.modes.base import BaseMode

GREETING = """
---[ Telnet Test Screen ]------------------------------------------------------

"""

HELP = """
---[ Help ]--------------------------------------------------------------------

  Valid commands currenly are:
  
    echo on
    echo off
    help
    naws
    pw on
    pw off
    quit
    sga
    ttype
"""

class TelnetTest(BaseMode):
    
    def __init__(self, conn):
        self.active = True  
        self.conn = conn
    
        self.send(GREETING)

        
    def process_command(self):
    
        cmd = self.get_cmd().lower()
        print cmd
        
        if cmd == 'quit':
            self.deactivate()
            return
            
        elif cmd == '':
            return            
            
        elif cmd == 'echo on':
            self.conn.request_will_echo()

        elif cmd == 'echo off':
            self.conn.request_wont_echo()            

        elif cmd == 'help':
            self.conn.send(HELP)
   
        elif cmd == 'naws':
            self.conn.request_naws()
   
        elif cmd == 'pw on':
            self.conn.password_mode_on()

        elif cmd == 'pw off':
            self.conn.password_mode_off()
            
        elif cmd == 'sga':
            self.conn.request_do_sga()

        elif cmd == 'ttype':
            self.conn.request_terminal_type() 

        else:
            self.send("?\n")


       
