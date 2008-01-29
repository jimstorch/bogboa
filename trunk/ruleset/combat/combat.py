#------------------------------------------------------------------------------
#   File:       combat_test.py
#   Purpose:
#   Author:     James Mynderse
#------------------------------------------------------------------------------

from npc_and_pc import npcRuleSet
from string import capwords
from xml.etree import cElementTree as et
from roll_dice import d20
##from monsters import load_monsters
##from server.decorate import colorize

class CombatMode(object):

    def __init__(self, conn, CombatLayout):
        self.conn = conn
        self.active = True
        self.CombatLayout = CombatLayout
        self.CombatAbilities = {}
        self.MonstersByHandle = {}
##        self.MonstersByName = {}
        self.load_combat_abilities()
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
        # load the monsters_list.xml file
        XMLFile = r"data\mobs\monster_list.xml"
        tree = et.parse(XMLFile)
        root = tree.getroot()
        allMobs = root.getchildren()
        for curMob in allMobs:
            out = self.dig_xml(curMob)
##            self.MonstersByHandle[out['handle']] = out
            self.MonstersByHandle[out['handle']] = npcRuleSet(out)
##            print self.MonstersByHandle[out['handle']]
##            self.MonstersByName[out['name']] = out
##            self.MonstersByHandle = npcRuleSet(self.MonstersByHandle)
##        self.MonstersByName = npcRuleSet(self.MonstersByName)
        return

    #--[ ]--
    def load_combat_abilities(self):
        XMLFile = r"data\abilities\combat_abilities.xml"
        tree = et.parse(XMLFile)
        root = tree.getroot()
        allClasses = root.getchildren()
        for Class in allClasses:
            out = self.dig_xml(Class)
            self.CombatAbilities[Class.tag] = out
##        print self.CombatAbilities
        return

    #--[ ]--   
    def dig_xml(self, root):
        out = {}
        children = root.getchildren()
        if len(children) > 0:
            for child in children:
                out[child.tag] = self.dig_xml(child)
        else:
            # determine what type of value is represented: int, float, str
            if root.text.isdigit():
                out = int(root.text)
            elif root.text.replace('.','0',1).isdigit():
                out = float(root.text)
            else:
                out = root.text
        return out

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
        if Handle in self.MonstersByHandle.keys():
            Combatant = self.MonstersByHandle[Handle]
            Combatant['initiative'] = d20()
##            Combatant['health'] = 0
##            Combatant['energy'] = 0
        else:
            Combatant = {}
            Combatant['name'] = capwords(Handle.replace('_', ' '))
            Combatant['initiative'] = d20()
            Combatant['hp'] = [0, 0]
            Combatant['mp'] = [0, 0]
        return Combatant

    #--[ ]--
    def roll_initiative(self):
        for Combatant in self.Combatants:
##            print self.Combatants[Combatant]
            self.Combatants[Combatant]['initiative'] = d20()
        return
    
    #--[ ]--
    def attack(self,strAttacker,strTarget):
        return

    #--[ ]--
    def defend(self):
        return

    #--[ ]--
    def display_layout(self):
##        print self.Combatants
        for i, Army in enumerate(self.Armies):
            print ('Army %d') % (i)
##            print self.Armies
##            print Army
            for j, Combatant in enumerate(Army):

##                print ('\tCombatant %d: %s') % (j, Combatant)
                print ('\t%s:') % (self.Combatants[Combatant]['name'])
                print ('\t\tInitiative: %d') % (self.Combatants[Combatant]['initiative'])
                print ('\t\tHealth: %d / %d') % (self.Combatants[Combatant]['hp'][0],
                                                 self.Combatants[Combatant]['hp'][1])
                print ('\t\tMana: %d / %d') % (self.Combatants[Combatant]['mp'][0],
                                               self.Combatants[Combatant]['mp'][1])
        return
                
