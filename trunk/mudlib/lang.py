# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/lang.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

import re


VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvw'

## Articles and short words to omit from comparison
OMIT = set(['a', 'an', 'of', 'the', 'for', 'with', 'on', 'to',
    'at', 'in', 'is', 'my', 'that',])

## Regex to split sentences at non-alpha characters
NON_ALPHA = re.compile("[^a-zA-Z]+")


#------------------------------------------------------------------------Keyset

def keyset(phrase):
    """
    Generate a set of key words for use with a NameTrie's match() method.
    """
    phrase = phrase.replace("\'", "")   ## guard's == guards
    words = set(NON_ALPHA.split(phrase.lower()))
    words = words - OMIT
    return words


#----------------------------------------------------------------------NameTrie

class NameTrie(object):

    """
    Trie object for matching of one-or-more word keys 
    against one-or-more word values.

    Allows for multiple, partial, and out-of-order matches.
    """


    class _Node(object):
        """
        Nested Node Class that maps a character value to the next Node.
        """
        def __init__(self):
            self.nodes = {}         

        def has(self, char):
            return self.nodes.get(char, False)
           
        def add(self, char):
            if char in self.nodes:
                node = self.nodes[char]
            else:
                node = NameTrie._Node()
                self.nodes[char] = node
            return node


    def __init__(self):
        self.root = NameTrie._Node()

    def _add_word(self, word):
        node = self.root
        for char in word:
            node = node.add(char)

    def _has_word(self, word):
        node = self.root
        for char in word:
            node = node.has(char)
            if not node:
                return False
        return bool(word and True)        
             
    def feed(self, phrase):
        """
        Adds the given name to the Trie.  Duplicates are overwritten.
        """
        words = keyset(phrase)
        for word in words:
            self._add_word(word)

    def match_phrase(self, phrase):
        """
        Tests a text string of zero or more words against the Trie.
        If you are going to be matching against multiple NameTries, create 
        one keyset and call test_keys() on each.
        """
        return self.test_keys(keyset(phrase))

    def match(self, keyset):
        """
        Given a keyset, return True if it matches the Trie.
        """
        for word in keyset:
            if not self._has_word(word):
                return False
        return bool(keyset and True)                


#------------------------------------------------------------------------Plural

def plural(noun):

    """
    Roughly apply the rules of pluralization.
    There are many exceptions in English that would require the overhead of
    a dictionary.
    """
 
    nl = noun.lower()

    ## is it too short to juggle?
    if len(nl) < 2:
        return noun + 's'

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

    """Return 'a' or 'an' depending on subject."""

    if not noun:
        return ''

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
      

#--------------------------------------------------------------------Guestimate

def guestimate(noun, num):

    """Give a general impression of quantity."""

    if num == 1:
        prefix = article(noun)

    elif num < 4:
        prefix = 'several'
        noun = plural(noun)

    elif num < 12:
        prefix = 'some'
        noun = plural(noun)

    elif num < 24:
        prefix = 'many'
        noun = plural(noun)

    elif num < 60:
        prefix = 'dozens of'
        noun = plural(noun)

    else:
        prefix = 'countless'         
        noun = plural(noun) 

    return prefix, noun
