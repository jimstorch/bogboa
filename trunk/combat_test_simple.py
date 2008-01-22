#------------------------------------------------------------------------------
#   File:       combat_test.py
#   Purpose:
#   Author:     James Mynderse
#------------------------------------------------------------------------------

from ruleset.combat.combat import CombatMode
from ruleset.combat.roll_dice import d20

mobElements = (('handle', 'handle'),
               ('name', 'name'),
               ('description', 'description'))
##               ('stats', (('level', 'level'),('brain', 'brain'),('soak', 'soak')),
##               ('temp', 'temp'))

conn = 1;
Army1 = ('barm','sarkoris','ugsomecur')
Army2 = ('queen_sald',)
CombatLayout = (Army1,Army2)
##print CombatLayout
test = CombatMode(conn, CombatLayout)


