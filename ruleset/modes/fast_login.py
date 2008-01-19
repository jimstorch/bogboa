#------------------------------------------------------------------------------
#   File:       fast_login.py
#   Purpose:    exquick -n- dirty login / registration
#   Author:     Jim Storch
#------------------------------------------------------------------------------

from server import shared

from ruleset.modes.base import BaseMode
from ruleset.modes.player import Player
from ruleset.dbm.mapping import check_name
from ruleset.dbm.mapping import check_password
from ruleset.dbm.mapping import insert_character
from ruleset.dbm.mapping import load_character


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

  ^yNew character names should be 3 to 15 characters long, contain only 
    letters, and begin with a capital.  Thanks.
"""    


#--[ Welcome Class ]-----------------------------------------------------------

class FastLogin(BaseMode):

    def __init__(self, conn):
        self.active = True  
        self.conn = conn
        self.name = None
        self.password = None
        self.state = 'name'
        self.attempts = 0
        self.gender = 'male'
        self.race = 'human'
        self.role = 'fighter'

        ## Request Terminal Type
        self.conn.request_terminal_type()
        ## Request Window Size
        self.conn.request_naws()
        self.send(GREETING)
        self.send("^C  Please enter your new or returning character's name:") 
        self.prompt()

    
    #---[ Process Command ]----------------------------------------------------

    def process_command(self):
        """A state machine to process login/new accounts."""
         
        cmd = self.get_cmd()
        #print cmd

        ## Look for a name, either new or old
        
        if self.state == 'name':
            
            ## Is it in the system already?
            if check_name(cmd):
                self.name = cmd
                self.send('  Welcome back ^!%s^1.\n' % cmd)
                self.send('^C  Enter password:')
                self.prompt()
                ## Turn off local echo
                self.conn.password_mode_on()            
                self.state = 'get_password'

            ## New player, check the name
            else:

                ## Is the name acceptable?
                if self.validate_name(cmd):
                    self.name = cmd
                    self.send('  The name ^!%s^1 is available.\n' % cmd) 
                    self.send('^C  Please select a password:')
                    self.prompt()
                    ## Turn off local echo
                    self.conn.password_mode_on()
                    self.state = 'check_one'
                
                # No, ask again 
                else:
                    self.send("^C  Please enter your new or returning character's name:")   
                    self.prompt()
                    self.state = 'name'                                        
    
        elif self.state == 'get_password':
            
            if check_password(self.name, cmd):
                ## Restore local echo
                self.conn.password_mode_off()

                ##
                ## Returning Character
                ##
                self.begin_play()

            else:
                ## Too many guesses?
                self.attempts += 1
                if self.attempts > 2:
                    self.deactivate()
                else:
                    self.send('\n^C  ^yIncorrect password. Try again:')
                    self.prompt()
                    self.state = 'get_password'

        elif self.state == 'check_one':

            ## Is the password acceptable?
            if self.validate_password(cmd):
                self.password = cmd
                self.send('\n^C  ...and enter it again just to be sure:')
                self.prompt()
                self.state = 'check_two'
                             
            ## Nope, ask again
            else:
                self.send('\r^C  Please select a password:')
                self.prompt()
                self.state = 'check_one'

        elif self.state == 'check_two':
            
            ## Did they match both times?
            if cmd == self.password:
                ## Restore local echo
                self.conn.password_mode_off()
                insert_character(self)
                ##
                ## New Character
                ##
                self.begin_play()

            else:
                self.send('\n  ^ySorry, those did not match.\n')
                self.send('  ^CPlease select a password:')
                self.prompt()
                self.state = 'check_one'
           
            

    #---[ Validate Name ]------------------------------------------------------

    def validate_name(self, name):
        """Check a proposed name for acceptability."""

        happy = True

        if len(name) < 3:
            self.send('  ^ySorry, that name is too short.\n')
            happy = False                            

        if len(name) > 20:
            self.send('  ^ySorry, that name is too long.\n')
            happy = False                       
        
        if len(name) and not name[0].isupper():
            self.send('  ^yPlease start with a capital letter.\n')
            happy = False                      

        for letter in name:
            if not letter.isalpha():
                self.send('  ^yPlease use letters only.\n')
                happy = False
                break                         

        return happy       


    #---[ Validate Password ]--------------------------------------------------
      
    def validate_password(self, password):
        """Check a proposed password for acceptability."""

        happy = True

        if len(password) < 6:
            self.send('\r\n  ^ySorry, that password is too short.\n')
            happy = False                       

        if len(password) > 20:
            self.send('\r\n  ^ySorry, that password is too long.\n')
            happy = False

        return happy   
       
    #---[ Begin Play ]---------------------------------------------------------

    def begin_play(self):
        """Move the connection to a playing mode."""

        mode = Player(self.conn)
        load_character(self.name, mode)
        shared.PLAY_LIST.append(mode)
        self.active = False
           

