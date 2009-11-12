#!/usr/bin/env python
#------------------------------------------------------------------------------
#   analyze.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

import re
import random
import operator


_FILENAME = 'data/female2.txt'
_CULL = 7

## Match 0 or more vowels + 1 or more consonants at the start of the word
_LEAD = re.compile(r'^[aeiouy]*[bcdfghjklmnprstvwxz]+')
## Match 1 or more vowels + 1 or more consonants inside a word (not start/end)
_INNER = re.compile(r'\B[aeiouy]+[bcdfghjklmnprstvwxz]+\B')
# Match 1 or more vowels + 0 or more consonats at the end of a word
_TRAIL = re.compile(r'[aeiouy]+[bcdfghjklmnprstvwxzy]?$')


def token_lists(names):

    lead, inner, tail = {}, {}, {}

    ## Populate dictionaries; key=pattern, value=frequency
    for name in names:

        match = re.match(_LEAD, name)
        if match:
            pat = match.group(0)
            count = lead.get(pat,0)
            lead[pat] = count +1

        matches = re.findall(_INNER, name)
        for pat in matches:
            count = inner.get(pat,0)
            inner[pat] = count +1

        match = re.search(_TRAIL, name)
        if match:
            pat = match.group(0)
            count = tail.get(pat,0)
            tail[pat] = count +1

    ## Convert dicts to a list of tuples in the format (pattern, frequency)
    lead_srt  = sorted(lead.items(),key=operator.itemgetter(1),reverse=True)
    inner_srt  = sorted(inner.items(),key=operator.itemgetter(1),reverse=True)
    tail_srt  = sorted(tail.items(),key=operator.itemgetter(1),reverse=True)

    ## Build lists of patterns ordered most to least frequent and cull rares
    lead_list = [ x[0] for x in lead_srt if x[1] > _CULL ]
    inner_list = [ x[0] for x in inner_srt if x[1] > _CULL ]
    tail_list = [ x[0] for x in tail_srt if x[1] > _CULL ]

    return lead_list, inner_list, tail_list


if __name__ == '__main__':

    names = open(_FILENAME, 'rt').readlines()
    lead_list, inner_list, tail_list = token_lists(names)

    print '#', len(lead_list), len(inner_list), len(tail_list)
    print '_LEADS = ', lead_list
    print '_INNERS = ', inner_list
    print '_TAILS = ', tail_list
