##-----------------------------------------------------------------------------
##  File:       lib/skill.py
##  Author:     Jim Storch
##-----------------------------------------------------------------------------

import math
import random


#-------------------------------------------------------------------------Skill

class Skill(object):

    def __init__(self):

        self.uuid = None
        self.name = None


    



def skill_cap(skill_name, player):
    pass




def diminishing_returns(val, scale):

##  Courtesy of Lost Soul's 
##  http://lostsouls.org/grimoire_diminishing_returns

    if val < 0:
        retval = -diminishing_returns(-val, scale)

    else:
        mult = val / float(scale)
        trinum = (math.sqrt(8.0 * mult + 1.0) - 1.0) / 2.0
        retval = trinum * scale

    return retval