# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/lang/finders.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

"""
Functions to match object name tries to keysets.
"""


def match_carried(actor, keyset):
    """
    Matches actor carried items against a keyset
    """
    matches = []
    for item in actor.carried:
        if item.trie.match_keyset(keyset):
            matches.append(item)
    return matches


def match_worn(actor, keyset):
    """
    Matches actor worn items against a keyset
    """
    matches = []
    for item in actor.worn.values:
        if item.trie.match_keyset(keyset):
            matches.append(item)
    return matches


def match_room_contents(room, keyset):
    """
    Matches items inside a room against a keyset.
    """
    matches = []
    for item in room.contents:
        if item.trie.match_keyset(keyset):
            matches.append(item)
    return matches
