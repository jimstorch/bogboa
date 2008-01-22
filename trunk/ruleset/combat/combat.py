#------------------------------------------------------------------------------
#   File:       combat_test.py
#   Purpose:
#   Author:     James Mynderse
#------------------------------------------------------------------------------

from xml.etree import cElementTree as et
from roll_dice import d20
##from monsters import load_monsters
##from server.decorate import colorize

class CombatMode(object):

    def __init__(self, conn, CombatLayout):
        self.conn = conn
        self.active = True
        self.CombatLayout = CombatLayout
        self.monsters = {}
        self.load_monsters()
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
    def load_monsters(self):
        # make a tuple of the expected elements
        mobStats = (('level', 'level'),
                    ('brain', 'brain'),
                    ('soak', 'soak'))
        quote = ('quote', 'quote')
        mobQuotes = (('anger', quote),
                     ('pain', quote),
                     ('death', quote))
        mobElements = (('handle', 'handle'),
                       ('name', 'name'),
                       ('description', 'description'),
                       ('stats', mobStats),
                       ('quotes', mobQuotes))

        # load the monsters_list.xml file
        XMLFile = r"data\mobs\monster_list.xml"
        tree = et.parse(XMLFile)

        # get all "mob" elements
        allMobs = tree.getroot().findall('mob')
        for curMob in allMobs:
            dicMob = {}
            for curElement in mobElements:
##                print curElement
                dicMob[curElement[0]] = self.parse_chunk(curMob, curElement)
##                print dicMob
            self.monsters[dicMob['handle']] = dicMob
        # loop through all "mob" elements
##        for curMob in allMobs:
##            dicMob = {}
##            for curElement in mobElements:
##                temp = curMob.findall(curElement[0])
##                if (len(curElement[1]) == 1):
##                    dicMob[curElement[0]] = temp[0].text
##                else:
##                    dicMob[curElement[0]] = {}
##                    for curSubElement in curElement[1]:
##                        print curElement[1]
##                        print curSubElement
##                        subtemp = temp.findall(curSubElement[0])
##                        dicMob[curElement[0]][curSubElement[0]] = subtemp[0].text
##            self.monsters[dicMob['handle']] = dicMob
        return

    def parse_chunk(self, curTree, curChunk):
##        print curChunk[0]
        temp = curTree.findall(curChunk[0])[0]
##        print temp
        if isinstance(curChunk[1],str):
            if temp.text:
                output = temp.text
            elif temp.value:
                output = temp.value
        else:
            for curSubChunk in curChunk[1]:
                output = {}
##                print curSubChunk
##                output[curSubChunk[0]] = self.parse_chunk(curTree, curSubChunk)
                output[curSubChunk[0]] = self.parse_chunk(temp, curSubChunk)
        return output

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
##        self.roll_initiative()
        return

    #--[ ]--
    def init_combatant(self,Handle):
        if Handle in self.monsters.keys():
            Combatant = self.monsters[Handle]
            Combatant['inititive'] = d20()
            Combatant['health'] = 0
            Combatant['energy'] = 0
        else:
            Combatant = {}
            Combatant['name'] = Handle
            Combatant['inititive'] = d20()
            Combatant['health'] = 0
            Combatant['energy'] = 0
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
                print ('\t%s:') % (self.Combatants[Combatant]['name'])
                print ('\t\tInitiative: %d') % (self.Combatants[Combatant]['initiative'])
                print ('\t\tHealth: %d') % (self.Combatants[Combatant]['health'])
                print ('\t\tEnergy: %d') % (self.Combatants[Combatant]['energy'])
        return
                
