#!/usr/bin/env python
#------------------------------------------------------------------------------
#   trolls.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

import random


_LEADS =  ['s', 'x', 'z', 'v', 'w', 'k', 'g', 'b', 'p', 'n', 't', 'f', 'd',
    'h', 'r', 'm', 'j', 'gn', 'vr', 'c', 'gr', 'sl', 'kn', 'kr']

_INNERS =  ['ag', 'ug', 'ar', 'ig', 'or', 'ul', 'ur', 'aug', 'og', 'ot',
    'agh', 'ugb', 'akg', 'il', 'eg', 'org', 'od', 'arg', 'arf', 'ilg', 
    'urb', 'un', 'at', 'ugh', 'ab', 'ub', 'om', 'ol', 'ahg', 'uk', 'an',
    'ath', 'ough', 'uth', 'urgh']

_TAILS =  ['ug', 'u', 'ag', 'a', 'og', 'ig', 'at', 'ub', 'uk', 'an', 'ed',
    'e', 'od', 'ud', 'im', 'ok', 'ek', 'ut']


def namegen():
    syllables = random.randint(0,1)
    if random.random() > .95:
        syllables += 1
    name = random.choice(_LEADS)
    for x in range(syllables):
        name += random.choice(_INNERS)
    name += random.choice(_TAILS)
    return name.title()


if __name__ == '__main__':

    for x in range(100):
        print namegen(),

