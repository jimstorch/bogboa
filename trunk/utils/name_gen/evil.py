#!/usr/bin/env python
#------------------------------------------------------------------------------
#   evil.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

import random


_LEADS =  ['d', 'm', 's', 'p', 'h', 'r', 'c', 'v', 'w', 'b', 'n', 't', 'f',
    'inf', 'ab', 'cr', 'st', 'sc']
_INNERS =  ['in', 'en', 'er', 'at', 'it', 'ef', 'il', 'is', 'or', 'al', 'am',
    'ut', 'abl', 'om', 'ol', 'ag', 'an', 'ic', 'em', 'ec', 'es', 'eat', 'ick',
    'orr', 'ect', 'ecr', 'ill', 'ers', 'ur', 'ain', 'ac', 'ir', 'ar']
_TAILS =  ['e', 'y', 'ion', 'ous', 'ed', 'er', 'ul', 'al', 'ious', 'ic', 'en',
    'id']


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

