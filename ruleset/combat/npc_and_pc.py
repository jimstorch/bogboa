#------------------------------------------------------------------------------
#   File:       npc_and_pc.py
#   Purpose:
#   Author:     James Mynderse
#------------------------------------------------------------------------------

##class NPC(object):
##    def __init__():
##        return
##
##
##class PC(object):
##    def __init__():
##        return

StatWeighting = ('warrior',())

def npcRuleSet(NPC):

    # create stats entry in NPC, if not present
    if 'stats' not in NPC.keys():
        NPC['stats'] = {}

    # create base stats, if not present
    # (what are base stats?)
    npcStats = ('str','sta','dex','agi','int','cha')
    for curStat in npcStats:
        if curStat not in NPC['stats'].keys():
            NPC['stats'][curStat] = 0
        
    # create health and mana, if not present
    # derived stats!
    # (could this be done better with an intelligent use of eval?)
    npcStats = (('hp',('sta',10)),
                ('mp',('int',10)))
    for curStat in npcStats:
        if curStat[0] not in NPC.keys():
            NPC[curStat[0]] = [NPC['stats'][curStat[1][0]]*curStat[1][1],
                               NPC['stats'][curStat[1][0]]*curStat[1][1]]

    return NPC
