#------------------------------------------------------------------------------
#   File:       combat_test.py
#   Purpose:
#   Author:     James Mynderse
#------------------------------------------------------------------------------

from ruleset.combat.combat import CombatMode
from ruleset.combat.roll_dice import d20
    
##a = {}
##a['test1'] = {}
##a['test1']['test2'] = 2
##print a
##d = d20()
##print d

conn = 1;
Army1 = ('Barm','Sarkoris','Ugsomecur')
Army2 = ('Queen Sald',)
CombatLayout = (Army1,Army2)
##print CombatLayout
test = CombatMode(conn, CombatLayout)


