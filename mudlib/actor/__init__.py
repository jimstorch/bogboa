# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/actor/__init__.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

"""
Actor Code; NPCs & Player Avatars.
"""

## Defined wear slots for equipable weapons, armor, and jewelry.
WEAR_SLOTS = ['head', 'face', 'ears', 'neck', 'shoulders', 'back',
    'chest', 'arms', 'wrists', 'hands', 'fingers',
    'main hand', 'off hand', 'both hands','waist', 'legs', 'feet']

## Order to show worn items in, main/off/both hands handled separately.
DISPLAY_SLOTS = ['head', 'face', 'ears', 'neck', 'shoulders', 'back',
    'chest', 'arms', 'wrists', 'hands', 'fingers', 'waist', 'legs', 'feet']
