# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/skill/melee.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

"""
Functions related to melee skills.
"""

from mudlib.stat import stat_bonus
from mudlib.skill import skill_check


def dual_wield_rating(actor, tutor=True):
    """
    Rate Actor's abilty to use two weapons at once.
    """
    if tutor:
        skillup_check(actor, 'dual_wield')     
    base = actor.get_skill('dual_wield')
    bonus = stat_bonus(actor, 'cunning')
    return base * bonus


def melee_combat_rating(actor, tutor=True):
    """
    Rate Actor's general combat prowess.
    """
    if tutor:
        skillup_check(actor, 'melee_combat')              
    base = actor.get_skill('melee_combat')
    bonus = stat_bonus(actor, 'brawn')
    return base * bonus


def primary_weapon_rating(actor, tutor=True):
    """
    Rate Actor's ability to use his selected primary weapon.
    """
    weapon_type = actor.get_primary_type()
    if tutor:
        skillup_check(actor, weapon_type)  
    base = actor.get_skill(weapon_type)
    bonus = stat_bonus(actor, 'precision')
    return base * bonus    


def primary_hit_rating(actor):
    """
    Rate Actor's ability to score a hit with his primary weapon.
    Uses the average of melee combat + weapon skill.
    Adjusts for dual wielding.
    """
    offense = melee_combat_rating(actor)
    weapon = primary_weapon_rating(actor)
    rating =  (offense + weapon) / 2.0
    if actor.is_dual_wielding():
        dual = dual_wield_rating(actor)
        rating = (dual + rating) / 2.0
    return rating


def primary_crit_rating(actor):
    """
    Rate Actor's ability to crit with the selected primary weapon.
    """
    weapon_type = actor.get_primary_type()
    base = actor.get_skill(weapon_type)
    bonus = stat_bonus(actor, 'cunning')
    return base * bonus 


def primary_max_dmg(actor):
    """
    Return the maximum damage for the Actor's primary weapon.
    """
    dmg = actor.get_primary_dmg()
    bonus = stat_bonus(actor, 'brawn')
    return dmg * bonus


def secondary_weapon_rating(actor, tutor=True):
    """
    Rate Actor's ability to use his selected secondary weapon.
    """
    weapon_type = actor.get_secondary_type()
    if tutor:
        skillup_check(actor, weapon_type)  
    base = actor.get_skill(weapon_type)
    bonus = stat_bonus(actor, 'precision')
    return base * bonus 


def secondary_hit_rating(actor):
    """
    Rate Actor's ability to score a hit with his secondary weapon.
    Uses the average of melee combat + weapon skill.
    Adjusts for dual wielding.
    """
    offense = melee_combat_rating(actor)
    weapon = primary_weapon_rating(actor)
    rating =  (offense + weapon) / 2.0
    if actor.is_dual_wielding():
        dual = dual_wield_rating(actor)
        rating = (dual + rating) / 2.0
    return rating


def secondary_crit_rating(actor):
    """
    Rate Actor's ability to crit with the selected secondary weapon.
    """
    weapon_type = actor.get_primary_type()
    base = actor.get_skill(weapon_type)
    bonus = stat_bonus(actor, 'cunning')
    return base * bonus  


def secondary_max_dmg(actor):
    """
    Return the maximum damage for the Actor's primary weapon.
    """
    dmg = actor.get_primary_dmg()
    bonus = stat_bonus(actor, 'brawn')
    return dmg * bonus    



    
