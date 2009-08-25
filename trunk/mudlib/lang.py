# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/lang.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvw'


#---------------------------------------------------------------------Pluralize

def pluralize(noun):

    """
    Roughly apply the rules of pluralization.
    There are many exceptions in English that would require the overhead of
    a dictionary.
    """
 
    nl = noun.lower()

    if len(nl) < 2:
        return 'short input into pluralize!'

    elif nl.endswith('ss'):
        suffix = 'es'
    elif nl.endswith('sh'):
        suffix = 'es'        
    elif nl.endswith('ch'):
        suffix = 'es'
    elif nl.endswith('x'):
        suffix = 'es'
    elif nl.endswith('z'):
        suffix = 'es'
    elif nl.endswith('y'):
        if nl[-2] in CONSONANTS:
            noun = noun[:-1]
            suffix = 'ies'
        else:
            suffix = 's'
    elif nl.endswith('f'):
        noun = noun[:-1]
        suffix = 'ves'
    elif nl.endswith('y'):
        suffix = 's'
    elif nl.endswith('o'):
        if nl[-2] in CONSONANTS:
            suffix = 'es'
        else:
            suffix = 's'
    else:
        suffix = 's'

    return noun + suffix    


#-----------------------------------------------------------------------Article

def article(noun):

    nl = noun.lower()

    if nl.startswith('uni'):
        art = 'a'
    elif nl.startswith('one'):
        art = 'a'
    elif nl.startswith('use'):
        art = 'a'
    elif nl.startswith('hon'):
        art = 'a'        
    elif nl[0] in VOWELS:
        art = 'an'
    else:
        art = 'a'

    return art
      

#----------------------------------------------------------------------Numerate

def numerate(noun, num):

    if num == 1:
        prefix = article(noun)

    elif num < 4:
        prefix = 'several'
        noun = pluralize(noun)

    elif num < 12:
        prefix = 'some'
        noun = pluralize(noun)

    elif num < 24:
        prefix = 'many'
        noun = pluralize(noun)

    elif num < 60:
        prefix = 'dozens of'
        noun = pluralize(noun)

    else:
        prefix = 'countless'         
        noun = pluralize(noun) 

    return prefix, noun
