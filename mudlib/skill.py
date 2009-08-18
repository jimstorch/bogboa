# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/skill.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

import math
import random

import shared
from driver.dbms.map import update_skill

# 10 points of Deterity = 1% bonus to hit.
# 10 points of Agility = 1% bonus to dodge.
# 10 points of Strength = 1% bonus to damage.

# max_skill = ( level * 10 ) * ( 1.0 + class_mod + race_mod )
# proficiency
# adeptness


"""
Skills

Comprised of a name + two bonus stats

skill cap = ( level * 10 ) * guild modifier 
current = the current skill level, i.e. 0 - cap
effective = current skill level * (1 + stat bonus)
stat bonus = skill's relevent stat from race, items, buffs


Guild has a huge impact on skills.
Race has either no impact or minor bonus via stat, never a penalty.


stats

str
agi
dex
sta
chr
wis
int
luc

"""


SKILLS = {


    ## Offense
    'one handed blunt':('str', 'wis'),
    'two handed blunt':('str','wis'),
    'one handed swords':('str', 'dex'),
    'two handed swords':('str', 'dex'),
    'archery':('dex','int'),
    'bare hand':('str','agi'),
    
 
    ## Magic
    'fire damage':('agi', 'int'),
    'cold damage':('sta', 'int'),
    'charm' : ('int', 'chr'),

    ## Movement
    'sneak':('agi', 'luc'),


    ## Defense & Saving Throws
    'dodge':('agi', 'luc'),
    'armor':('sta','agi'),
    'mind control':('int','wis'),
    'falling':('agi','luc'),
    'death':('sta','luc'),
    'poison':('sta','str'),
    'freezing':('sta', 'int'),
    'burning':('agi','int'),
    'disease':('sta','wis'),    

    } 



#---------------------------------------------------------------------Skill Cap

def skill_cap(skill, body)

    """Give a skill name and a body, return that body's skill cap value."""

    guild = shared.GUILD[body.guild]
    modifier = guild.skills.get(skill, 0)
    return = ( body.level * 10.0 ) * modifier

    
#----------------------------------------------------------------Skill Up Check

def skillup_check(skill, body):

    curr, cap = body.skills[skill]

    if curr < cap:
        chance = ( float(cap) / float(curr) ) / 100.00
        if random.random() > chance:
            curr += 1 
            update_skill(body.name, skill, curr)
            body,send('Your skill at %s has improved to %d\n' % (skill, curr))


#-----------------------------------------------------------Diminishing Returns

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
