#------------------------------------------------------------------------------
#   File:       new_character.py
#   Purpose:    create a character
#   Author:     Jim Storch
#------------------------------------------------------------------------------

from ruleset.dbm.mapping import check_name
from ruleset.dbm.mapping import insert_character


GREETING = """^y
  ***** ^!New Character Creation^1 *****

  To create your character you will need to select a name and a password.

  ^w[^Wname^w]^y

  * Names should be 3 to 20 letters long and begin with a capital letter.
  * Names may only contain letters -- no digits or spaces.
  * They should be appropriate for a fantasy setting.
  * Characters with stupid names often vanish mysteriously. 

  ^w[^Wpassword^w]^y

  * Passwords should be 6 to 20 characters long.
  * Use only letters and digits.
  ^R* It it strongly advised that you do not use a password that you use
    to protect data somewhere else!  Transmissions are not encrypted.
"""

HELP = """^c
  Valid commands currently are:

  ^Wname^c       - Select a name for your character.
  ^Wpassword^c   - Select a password for logging in.
  ^Wsave^c       - Save your selections and enter the game.
  ^Wquit^c       - Disconnect from the server
"""

class NewCharacter(object):

    def __init__(self, conn):
        self.active = True  
        self.conn = conn

        # Mode specific
        self.confusion = 0
        self.state = 'base'
        self.name = None
        self.password = None
        self.gender = 'male'
        self.race = 'human'
        self.role = 'fighter'
        
        self.conn.send(GREETING)
        self.conn.prompt()

    def process_command(self):
    
        cmd = self.conn.get_cmd()
        cmd_low = cmd.lower()
        print cmd
        
        #--[ Base State ]--------------------------------------------------

        if self.state == 'base':

            if cmd_low == 'quit':            
                self.deactivate()
                return

            elif cmd_low == 'help':
                self.conn.send(HELP)
                self.conn.prompt()

            elif cmd_low == 'set ansi off':
                self.conn.use_ansi = False
                self.conn.send('ANSI color encoding turned off.')
                self.conn.prompt()
            
            elif cmd_low == 'name':
                self.conn.send("  What name would you like to use?")
                self.state = 'name'
                self.conn.prompt() 
            
            elif cmd_low == 'password':
                self.conn.send("  What password would you like to use?")
                self.state = 'password'
                self.conn.prompt() 
            
            #--[ Save ]----------------------------------------------------

            elif cmd_low == 'save':
                
                happy = True

                if not self.name:
                    self.conn.send('  Please pick a ^!name^1 first.\n')
                    happy = False

                if not self.password:
                    self.conn.send('  Please pick a ^!password^1 first.\n')
                    happy = False

                if not happy:
                    self.state = 'base' 
                    self.conn.prompt()

                else:
                    self.conn.send('  Saving your selections.\n')
                    ## Move on from here
                    insert_character(self)

            else:
                self.conn.send("  Unknown command.")
                self.confusion += 1
                if self.confusion == 4:
                    self.conn.send("  Try typing '^!help^1' if you're lost.")
                    self.confusion = 0
                self.conn.prompt()  


        #--[ State Check Name ]--------------------------------------------

        elif self.state == 'name':
            name = cmd
            happy = True

            if check_name(name):
                self.conn.send('  Sorry, that name is not available.\n')
                happy = False                                               

            elif len(name) < 3:
                self.conn.send('  Sorry, that name is too short.\n')
                happy = False                            

            elif len(name) > 20:
                self.conn.send('  Sorry, that name is too long.\n')
                happy = False                       

            elif not name[0].isupper():
                self.conn.send('  Please start with a capital letter.\n')
                happy = False                      

            for letter in name:
                if not letter.isalpha():
                    self.conn.send('  Please use letters only.\n')
                    happy = False
                    break                         

            if not happy:
                self.conn.send('\n  What name would you like to use?')
                self.name = None
                self.state = 'name'
                self.conn.prompt()

            else:
                self.conn.send('  We will call you ^!%s^1.\n' % name)
                self.conn.send("  If you change your mind, enter " +
                    "'^!name^1' again prior to '^!save^1'.")
                self.name = name
                self.state = 'base'                   
                self.conn.prompt()

            
        #--[ State Check Password ]----------------------------------------

        elif self.state == 'password':
            password = cmd
            happy = True

            if len(password) < 6:
                self.conn.send('  Sorry, that password is too short.\n')
                happy = False                       

            if len(password) > 20:
                self.conn.send('  Sorry, that password is too long.\n')
                happy = False   

            if not happy:
                self.conn.send('\n  What password would you like to use?')
                self.password = None
                self.state = 'password'
                self.conn.prompt()

            else:
                self.conn.send('  Your password will be ^!%s^1.\n' % password)
                self.conn.send("  If you change your mind, enter " +
                    "'^!password^1' again prior to '^!save^1'.")
                self.password = password
                self.state = 'base'                   
                self.conn.prompt()

  
    #--[ Deactivate ]----------------------------------------------------------            
                    
    def deactivate(self):

        # 'self' gets deleted by control.purge_dead_clients()
        self.conn.active = False 

        # conn gets deleted by async.ThePortManager.poll()  
        self.active = False


