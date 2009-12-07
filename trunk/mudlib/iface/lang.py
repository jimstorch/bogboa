# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/lang.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

import re

from driver.error import BogCmdError

_VOWELS = 'aeiou'


#-------------------------------------------------------------------------found

def found(regex, msg):
    return bool(re.search(regex, msg))


#------------------------------------------------------------------------Keyset

## Regex to split sentences at non-alpha characters
_NON_ALPHA = re.compile("[^a-zA-Z]+")

## Articles and short words to omit from comparison
_OMIT = set(['a', 'an', 'of', 'the', 'for', 'with', 'on', 'to',
    'at', 'in', 'is', 'my', 'that',])


def keyset(phrase):
    """
    Generate a set of key words for use with a NameTrie's match() method.
    """
    phrase = phrase.replace("\'", "")   ## guard's == guards
    words = set(_NON_ALPHA.split(phrase.lower()))
    words = words - _OMIT
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
        words = keyset(phrase)
        for word in words:
            self._add_word(word)
            ## Also add the plural of each
            self._add_word(plural(word))

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


#------------------------------------------------------------------------Plural

_IRREGULAR = {
    'child':'children',
    'foot':'feet',
    'fungus':'fungi',
    'goose':'geece',
    'louse':'lice',
    'man':'men',
    'mouse':'mice',
    'ox':'oxen',
    'person':'people',
    'tooth':'teeth',
    'woman':'women',
    }


def plural(noun):

    """Roughly apply the rules of pluralization."""

    nl = noun.lower()

    ## is it too short to juggle?
    if len(nl) < 2:
        return noun + 's'

    ## Check for an irregular noun
    if nl in _IRREGULAR:
        return _IRREGULAR[nl]

    suffix = 's'
    if nl[-2:] in ('ss', 'sh', 'ch') or  nl[-1:] in ('x','z'):
        suffix = 'es'
    elif nl.endswith('y'):
        if nl[-2] not in _VOWELS:
            noun = noun[:-1]
            suffix = 'ies'
    elif nl.endswith('f'):
        noun = noun[:-1]
        suffix = 'ves'
    elif nl.endswith('o'):
        if nl[-2] not in _VOWELS:
            suffix = 'es'
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
    elif nl[0] in _VOWELS:
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


#--------------------------------------------------------------------Arg to Int

_WRITTEN = {
    'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6,
    'seven':7, 'eight':8, 'nine':9, 'ten':10, 'eleven':11,
    'twelve':12, 'thirteen':13, 'fourteen':14, 'fifteen':15,
    'sixteen':16, 'seventeen':17, 'eighteen':18, 'nineteen': 19,
    'twenty':20, 'thirty':30, 'forty':40, 'fifty':50, 'sixty':60,
    'seventy':70, 'eighty':80, 'ninety':90, 'a':1, 'an':1,
    }

def arg_to_int(arg):

    """
    Given a string, attempts to convert it into an integer value.
    Converts digits and simple one-word values.
    Returns integer value or None for non-numeric arguments.

    Note: raises BogCmdError()
    """

    ##TODO: add support for hyphenated word values maybe?

    arg = arg.lower()

    if arg.isdigit():
        ## Test for numeric abuse so we don't crash on ridiculous input
        if len(arg) > 9:
            raise BogCmdError('Too many digits in number.')
        else:
            return int(arg)

    elif arg in _WRITTEN:
        return _WRITTEN[arg]

    else:
        return None


#---------------------------------------------------------------Parse Item Pick

def parse_item_pick(args):

    # Start right to left ...

    count = None
    subject = None
    ex_count = None
    ex_subject = None
    target = None

    if len(args) > 0:

        if 'from' in args:
            i = args.index('from') + 1
            if len(args) == i:
                raise BogCmdError('from where?')

            else:
                target = ' '.join(args[i:])
                args = args[:i - 1]

        if 'but' in args:

            i = args.index('but') + 1
            if len(args) == i:
                raise BogCmdError('but what?')

            else:
                sub = args[i:]
                if sub > 1:
                    arg = sub[0]
                    num = arg_to_int(arg)
                    if num != None:
                        ex_count = num
                        sub = sub[1:]

                ex_subject = ' '.join(sub)
                args = args[:i - 1]


    # Now left to right ...

    if len(args) > 0:

        arg = args[0]

        num = arg_to_int(arg)
        if num != None:
            count = num
            args = args[1:]
            if not subject:
                subject = ' '.join(args)

        elif arg == 'all' or arg == 'everything' or arg == 'every':
            args = args[1:]
            if not subject:
                subject = ' '.join(args)

        else:
            subject = ' '.join(args)

    return (count, subject, ex_count, ex_subject, target)
