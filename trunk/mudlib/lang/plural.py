# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/lang/trie.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

"""
Plurals Support, used to see Name Tries.
"""


_IRREGULAR = {
    'child':'children',
    'foot':'feet',
    'fungus':'fungi',
    'goose':'geece',
    'louse':'lice',
    'man':'men',
    'mouse':'mice',
    'ox':'oxen',
    'person':'people',
    'tooth':'teeth',
    'woman':'women',
    }

_VOWELS = 'aeiou'


def make_plural(noun):

    """Roughly apply the rules of pluralization."""

    nl = noun.lower()

    ## is it too short to juggle?
    if len(nl) < 2:
        return noun + 's'

    ## Check for an irregular noun
    if nl in _IRREGULAR:
        return _IRREGULAR[nl]

    suffix = 's'
    if nl[-2:] in ('ss', 'sh', 'ch') or  nl[-1:] in ('x','z'):
        suffix = 'es'
    elif nl.endswith('y'):
        if nl[-2] not in _VOWELS:
            noun = noun[:-1]
            suffix = 'ies'
    elif nl.endswith('f'):
        noun = noun[:-1]
        suffix = 'ves'
    elif nl.endswith('o'):
        if nl[-2] not in _VOWELS:
            suffix = 'es'
    return noun + suffix
