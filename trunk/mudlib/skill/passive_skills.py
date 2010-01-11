# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/skill/passive_skills.py
#   Copyright 2010 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

"""
Rate passive skills.
"""

from mudlib.stat import stat_bonus, greater_of_bonus


def level_rating(actor):
    """
    Simply return the Actor's level x 10.
    """
    return actor.level * 10.0


def body_rating(actor):
    """
    Return the Actor's max hitpoints.
    """
    base = actor.get_skill('body')
    bonus = greater_of_bonus(actor, 'brawn',)
    return base * bonus


def body_regen_rating(actor):
    """
    Return the Actor's health regeneration rating.
    """
    base = actor.get_skill('recovery')
    bonus = stat_bonus(actor, 'vigor')
    return base * bonus


def mind_rating(actor):
    """
    Return the Actor's maximum power/mana.
    """
    base = actor.get_skill('mind')
    bonus = greater_of_bonus(actor, 'knowledge')
    return base * bonus


def mind_regen_rating(actor):
    """
    Return the Actor's health regeneration rating.
    """
    base = actor.get_skill('meditation')
    bonus = stat_bonus(actor, 'faith')
    return base * bonus
