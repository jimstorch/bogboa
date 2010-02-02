# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/lang/trie.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

"""
Trie Class used for flexible name matching.
"""

import re

from mudlib.lang.plural import make_plural

## Regex to split sentences at non-alpha characters
_NON_ALPHA = re.compile("[^a-zA-Z]+")

## Articles and short words to omit from comparison
_OMIT = set(['a', 'an', 'of', 'the', 'for', 'with', 'on', 'to',
    'at', 'in', 'is', 'my', 'that',])


def create_keyset(phrase):
    """
    Generate a set of key words for use with a NameTrie's match() method.
    """
    phrase = phrase.replace("\'", "")   ## guard's == guards
    words = set(_NON_ALPHA.split(phrase.lower()))
    words = words - _OMIT
    return words


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
        #print word
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
        words = create_keyset(phrase)
        for word in words:
            self._add_word(word)
            ## Also add the plural of each
            self._add_word(make_plural(word))

    def match_phrase(self, phrase):
        """
        Tests a text string of zero or more words against the Trie.
        If you are going to be matching against multiple NameTries, create
        one keyset and call test_keys() on each.
        """
        return self.test_keys(keyset(phrase))

    def match_keyset(self, keyset):
        """
        Given a keyset, return True if it matches the Trie.
        """
        for word in keyset:
            if not self._has_word(word):
                return False
        return bool(keyset and True)
