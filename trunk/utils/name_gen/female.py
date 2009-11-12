#!/usr/bin/env python
#------------------------------------------------------------------------------
#   female.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

import random


_LEADS =  ['m', 'l', 'j', 'c', 'd', 'r', 's', 'k', 'b', 't', 'sh', 'h', 'p',
    'v', 'n', 'g', 'al', 'br', 'el', 'ch', 'w', 'chr', 'fr', 'kr', 'tr',
    'ang', 'cl']
_INNERS =  ['in', 'ar', 'el', 'en', 'or', 'an', 'ett', 'ell', 'er', 'ic',
    'al', 'os', 'ist', 'ann', 'it', 'ac', 'il', 'ill', 'and', 'on', 'at',
    'ol', 'am', 'arl', 'err', 'is', 'ath', 'ad', 'ess', 'eann', 'ab', 'ind',
    'ean', 'aur', 'oll', 'et', 'est', 'ul', 'ish', 'iann', 'ian', 'anc']
_TAILS =  ['a', 'e', 'ie', 'y', 'ia', 'i', 'ey', 'yn', 'el', 'en', 'een',
    'er', 'ah', 'is', 'in', 'on']


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
