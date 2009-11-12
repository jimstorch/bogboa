#!/usr/bin/env python
#------------------------------------------------------------------------------
#   male.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

import random


_LEADS =  ['d', 'j', 'm', 'r', 'l', 'w', 'c', 'h', 'g', 'b', 'br', 't', 'k',
    'n', 's', 'cl', 'fr', 'f', 'p', 'st', 'v', 'ch', 'sh', 'gr', 'tr']
_INNERS =  ['er', 'ar', 'el', 'or', 'an', 'ic', 'arr', 'am', 'ol', 'on',
    'al', 'en', 'ill', 'in', 'err', 'and', 'il', 'om', 'et', 'arl', 'ev',
    'ac', 'ust', 'av', 'ert', 'enn', 'ent', 'ath', 'onn', 'it', 'os', 'enc',
    'yr', 'em', 'ist', 'anc', 'arc', 'ich', 'as', 'est']
_TAILS =  ['o', 'on', 'e', 'y', 'ey', 'er', 'in', 'an', 'ie', 'io', 'en',
    'is', 'el', 'us', 'es', 'as', 'ian', 'ed']


def namegen():
    syllables = random.randint(0,1)
    if random.random() > .85:
        syllables += 1
    name = random.choice(_LEADS)
    for x in range(syllables):
        name += random.choice(_INNERS)
    name += random.choice(_TAILS)
    return name.title()


if __name__ == '__main__':

    for x in range(100):
        print namegen(),
