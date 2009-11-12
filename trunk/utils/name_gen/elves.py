#!/usr/bin/env python
#------------------------------------------------------------------------------
#   elves.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

import random

_LEADS =  ['f', 'm', 'c', 'g', 't', 'en', 'amr', 'd', 'l', 'n', 'or', 'el',
    'im', 'er', 'ingl', 'ingw', 'p']

_INNERS =  ['el', 'al', 'ind', 'ot', 'or', 'in', 'eg', 'ar', 'ebr', 'ing',
    'ell', 'ol', 'ald', 'ir', 'uil', 'oph', 'aer', 'od', 'un', 'at']

_TAILS =  ['or', 'in', 'e', 'el', 'as', 'il', 'ion', 'on', 'ir', 'od', 'iel',
    'an', 'ie', 'is', 'ye', 'os']


def namegen():
    syllables = random.randint(0,1)
    if random.random() > .75:
        syllables += 1
    name = random.choice(_LEADS)
    for x in range(syllables):
        name += random.choice(_INNERS)
    name += random.choice(_TAILS)
    return name.title()


if __name__ == '__main__':

    for x in range(100):
        print namegen(),

