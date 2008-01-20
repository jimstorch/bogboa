#------------------------------------------------------------------------------
#   File:       combat_test.py
#   Purpose:
#   Author:     James Mynderse
#------------------------------------------------------------------------------

from roll_dice import d20
##from server.decorate import colorize

class CombatMode(object):

    def __init__(self, conn, CombatLayout):
        self.conn = conn
        self.active = True
        self.CombatLayout = CombatLayout
        self.parse_combatlayout()
        self.display_layout()
        return
    
    #--[ Get Cmd ]-------------------------------------------------------------
    def get_cmd(self):
        return self.conn.get_cmd()

    #--[ Send ]----------------------------------------------------------------        
    def send(self, text):
        text = text.replace('\n', '\r\n')
        self.conn.send(colorize(text, self.conn.use_ansi))
        return
    
    #---[ Prompt ]-------------------------------------------------------------
    def prompt(self):
        """Show the command entry prompt on the DE's screen."""
        self.send('\r\n^G>^w ')
        return
    
    #--[ Deactivate Method ]---------------------------------------------------
    def deactivate(self):

        # 'self' gets deleted by control.purge_dead_clients()
        self.conn.active = False 

        # conn gets deleted by async.ThePortManager.poll()  
        self.active = False   
        return

    #--[ ]--
    def parse_combatlayout(self):
        self.Combatants = {}
        self.Armies = []
        for i, Army in enumerate(self.CombatLayout):
            self.Armies.append(Army)
            for Combatant in Army:
##                print Combatant
                self.Combatants[Combatant] = self.init_combatant(Combatant)
##                print self.Combatants[Combatant]
        self.roll_initiative()
        return

    #--[ ]--
    def init_combatant(self,Name):
        Combatant = {}
        Combatant['Name'] = Name
        Combatant['Inititive'] = 0
        Combatant['Health'] = 0
        Combatant['Energy'] = 0
        return Combatant

    #--[ ]--
    def roll_initiative(self):
        for Combatant in self.Combatants:
##            print self.Combatants[Combatant]
            self.Combatants[Combatant]['Initiative'] = d20()
        return
    
    #--[ ]--
    def attack(self,strAttacker,strTarget):
        return

    #--[ ]--
    def defend(self):
        return

    #--[ ]--
    def display_layout(self):
        for i, Army in enumerate(self.Armies):
            print ('Army %d') % (i)
##            print self.Armies
##            print Army
            for j, Combatant in enumerate(Army):
##                print ('\tCombatant %d: %s') % (j, Combatant)
                print ('\t%s:') % (self.Combatants[Combatant]['Name'])
                print ('\t\tInitiative: %d') % (self.Combatants[Combatant]['Initiative'])
                print ('\t\tHealth: %d') % (self.Combatants[Combatant]['Health'])
                print ('\t\tEnergy: %d') % (self.Combatants[Combatant]['Energy'])
        return
                
