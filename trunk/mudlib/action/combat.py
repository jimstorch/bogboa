# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/action/combat.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

import random

from mudlib.skill import *

def init_combat(src, tar):
    """
    Alert Target that Source means them harm.
    """
    pass


def primary_weapon_test(src, tar):
    """
    Test for a hit using Source's primary melee weapon.
    """
    hit = primary_hit_rating(src)
    defend = defense_rating(tar)
    return bool(random.randrange(defend + hit) > defend)


def primary_weapon_dmg(src, tar):
    """
    Scales Source's primary weapon damage against Target's armor.
    """
    dmg = primary_max_dmg(src)
    armor = armor_rating(tar)
    hit = primary_hit_rating(src) * .25
    attack = random.randrange(armor + hit)      
    if attack < armor:
        scale = (armor / 100.0) * attack
        dmg *= scale 
    return dmg
        

def secondary_weapon_test(src, tar):
    """
    Test for a hit using Source's secondary melee weapon.
    """
    hit = skill.primary_hit_rating(src)
    defend = skill.defense_rating(tar)
    return bool(random.randrange(defend + hit) > defend) 


def secondary_weapon_dmg(src, tar):
    """
    Scales Source's secondary weapon damage against Target's armor.
    """
    dmg = secondary_max_dmg(src)
    armor = armor_rating(tar)
    hit = secondary_hit_rating(src) * .25
    attack = random.randrange(armor + hit)      
    if attack < armor:
        scale = (armor / 100.0) * attack
        dmg *= scale 
    return dmg


def ranged_weapon_test(src, tar):
    """
    Test for a hit using Source's ranged weapon.
    """
    hit = skill.missile_hit_rating(src)
    defend = skill.defense_rating(tar)
    return bool(random.randrange(defend + hit) > defend) 


def ranged_weapon_dmg(src, tar):
    """
    Scales Source's ranged damage against Target's armor.
    """
    dmg = ranged_max_dmg(src)
    armor = armor_rating(tar)
    hit = ranged_hit_rating(src) * .25
    attack = random.randrange(armor + hit)      
    if attack < armor:
        scale = (armor / 100.0) * attack
        dmg *= scale 
    return dmg
    
    
