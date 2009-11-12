#!/usr/bin/env python
#------------------------------------------------------------------------------
#   lovecraft.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

import random


_LEADS =  ['n', 'sh', 'b', 'h', 's', 'z', 'zh', 'gh', 'c', 'cth', 'oth',
    'gl', 't', 'rh', 'm', 'kth', 'v', 'k']

_INNERS =  ['at', 'ag', 'ath', 'ot', 'oth', 'an', 'ad', 'as', 'ak', 'am',
    'al', 'ar', 'igg', 'og', 'ut', 'ulh', 'or']

_TAILS =  ['a', 'on', 'ah', 'ar', 'og', 'ua', 'os', 'is', 'an', 'oom']


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

