# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/skill/skill_math.py
#   Copyright 2010 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

"""
Skill related computations.
"""

import math
import random

from mudlib.sys import GUILDS
from mudlib.dat import store_kv


def skill_cap(actor, skill_name)
    """
    Given an actor and skill name, return the maximum allowable skill value.
    """
    guild = GUILDS[actor.guild]
    modifier = guild.get_skill_modifier(skill_name)
    return actor.level * 10.0 * modifier


def update_skill(actor, skill_name, value):
    """
    Permanetly modify the Actor's given skill value.
    """
    value = int(value)
    actor.set_skill(skill_name, value)
    ## TODO: enable this
    #store_kv(actor.uuid, 'skills', skill_name, value)


def skillup_check(actor, skill_name):
    """
    Test for a possible skill increase.
    Chance decreases as skill level approaches the Actor's skill cap.
    Bonus stat = cunning.
    """
    cap = skill_cap(actor, skill_name)
    ## Does their Guild allow this skill?
    if cap > 0.0:
        skill = actor.get_skill(skill_name)
        if skill < cap:
            chance = ( cap / float(skill) ) / 100.00
            bonus = actor.get_stat('cunning') / 1000.0
            if (random.random() + bonus) > chance:
                skill += 1
                update_skill(actor, skill_name, skill)
                actor.inform('\nYour skill at %s has improved to %d.' %
                    (skill_name, skill))


def diminishing_returns(val, scale):
    """
    Scale a value over a limited, non-linear range.
    Courtesy of Lost Soul's  http://lostsouls.org/grimoire_diminishing_returns
    """
    if val < 0:
        retval = -diminishing_returns(-val, scale)
    else:
        mult = val / float(scale)
        trinum = (math.sqrt(8.0 * mult + 1.0) - 1.0) / 2.0
        retval = trinum * scale
    return retval
