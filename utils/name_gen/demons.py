#!/usr/bin/env python
#------------------------------------------------------------------------------
#   demons.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

import random

_LEADS =  ['b', 'm', 'l', 's', 'r', 'n', 'v', 'd', 't', 'f', 'h', 'p', 'sh',
    'andr', 'g', 'z', 'ab', 'gr', 'ag', 'am', 'al', 'ap', 'as', 'ch', 'ast',
    'st', 'asm', 'or']
_INNERS =  ['er', 'em', 'al', 'ar', 'el', 'oc', 'am', 'ab', 'ec', 'ol', 'ot',
    'or', 'it', 'us', 'ag', 'as', 'in', 'il', 'en', 'om', 'os', 'aph', 'at',
    'art', 'eh', 'ek', 'ed', 'eg', 'et', 'ev', 'ast', 'org', 'od', 'ob',
    'ath', 'ov', 'uch', 'ul', 'uc', 'ub', 'ah', 'an', 'ant', 'av', 'az',
    'ig', 'if', 'alph']
_TAILS =  ['a', 'as', 'on', 'us', 'u', 'an', 'e', 'i', 'el', 'o', 'es', 'os',
    'ac', 'al', 'im', 'ia', 'ion', 'ael', 'ius', 'ur', 'ax', 'or', 'em',
    'is', 'am', 'ar', 'in', 'ias', 'it', 'eus', 'aal']


def namegen():
    syllables = random.randint(1,2)
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

