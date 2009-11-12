#!/usr/bin/env python
#------------------------------------------------------------------------------
#   orcs.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

import random


_LEADS =  ['k', 'm', 'g', 'gr', 'th', 'z', 'r', 'b', 's', 'h', 't', 'orm',
    'n', 'kr', 'sh', 'sn', 'or']

_INNERS =  ['ar', 'or', 'an', 'om', 'org', 'and', 'am', 'ag', 'elm', 'elgr',
    'ath', 'un']

_TAILS =  ['an', 'a', 'ul', 'ak', 'ok', 'ar', 'us', 'u', 'uk', 'ag', 'o',
    'in', 'ek', 'uul', 'om']



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

