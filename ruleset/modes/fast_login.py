#------------------------------------------------------------------------------
#   File:       fast_login.py
#   Purpose:    quick -n- dirty login / registration
#   Author:     Jim Storch
#------------------------------------------------------------------------------


from ruleset import shared
from ruleset.lookup import is_online
from ruleset.modes.base_mode import BaseMode
from ruleset.modes.player import Player
from ruleset.dbm.mapping import check_name
from ruleset.dbm.mapping import check_password
from ruleset.dbm.mapping import insert_character
from ruleset.dbm.mapping import load_character
from ruleset.abilities.speech import broadcast


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
        self.handle = ''
        self.name = ''
        self.password = None
        self.state = 'name'
        self.attempts = 0
        self.gender = 'male'
        self.race = 'human'
        self.role = 'fighter'
        self.room = None

        ## Request Terminal Type
        self.conn.request_terminal_type()
        ## Request Window Size
        self.conn.request_naws()
        self.send(GREETING)
        self.send("^CPlease enter your new or returning character's name:") 
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
                self.handle = cmd.lower()
                self.send('Welcome back ^!%s^1.' % cmd)
                self.send('^CEnter password:')
                self.prompt()
                ## Turn off local echo
                self.conn.password_mode_on()            
                self.state = 'get_password'

            ## New player, check the name
            else:

                ## Is the name acceptable?
                if self.validate_name(cmd):
                    self.name = cmd
                    self.handle = cmd.lower()
                    self.send('The name ^!%s^1 is available.' % cmd) 
                    self.send('^CPlease select a password:')
                    self.prompt()
                    ## Turn off local echo
                    self.conn.password_mode_on()
                    self.state = 'check_one'
                
                # No, ask again 
                else:
                    self.send("^CPlease enter your new or returning character's name:")   
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
                    self.send('^yIncorrect password. Try again:')
                    self.prompt()
                    self.state = 'get_password'

        elif self.state == 'check_one':

            ## Is the password acceptable?
            if self.validate_password(cmd):
                self.password = cmd
                self.send('^C...and enter it again just to be sure:')
                self.prompt()
                self.state = 'check_two'
                             
            ## Nope, ask again
            else:
                self.send('^CPlease select a password:')
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
                self.send('^ySorry, those did not match.')
                self.send('^CPlease select a password:')
                self.prompt()
                self.state = 'check_one'
           
            

    #---[ Validate Name ]------------------------------------------------------

    def validate_name(self, name):
        """Check a proposed name for acceptability."""

        happy = True

        if len(name) < 3:
            self.send('^ySorry, that name is too short.')
            happy = False                            

        if len(name) > 20:
            self.send('^ySorry, that name is too long.')
            happy = False                       
        
        if len(name) and not name[0].isupper():
            self.send('^yPlease start with a capital letter.')
            happy = False                      

        for letter in name:
            if not letter.isalpha():
                self.send('^yPlease use letters only.')
                happy = False
                break                         

        return happy       


    #---[ Validate Password ]--------------------------------------------------
      
    def validate_password(self, password):
        """Check a proposed password for acceptability."""

        happy = True
# TODO: restore short check
#        if len(password) < 6:
#            self.send('\r\n^ySorry, that password is too short.\n')
#            happy = False                       

        if len(password) > 20:
            self.send('^ySorry, that password is too long.')
            happy = False

        return happy   
       
    #---[ Begin Play ]---------------------------------------------------------

    def begin_play(self):
        """Move the connection to a playing mode."""
        if not is_online(self.handle):
            mode = Player(self.conn)
            ## Load the character from the database
            load_character(self.handle, mode)
            broadcast('^y%s has come online.' % mode.name)
            ## Add it to the PLAY_LIST 
            shared.PLAY_LIST.append(mode)
            ## Add this to the dictionary of play handles
            shared.HANDLE_DICT[self.handle] = mode
            ## Put into a room
            shared.ROOM_DICT['start'].add_player(mode,'')
            mode.prompt()
            self.active = False
        
        else:
            self.send('^RAccount is in use!')
            self.send('^CPlease enter a character name:')
            self.prompt() 
            self.state = 'name'

