# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/lang/brace_sub.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

"""
Code to process brace-delineated text substitution.
"""

## Regex to match a {brace enclosed keys}, {orphaned {braces, and plain text
_BRACE_REGEX_STRING = r"{([^{]*?)}|([{}])|([^{}]*)"
_BRACE_REGEX = re.compile(_BRACE_REGEX_STRING, re.MULTILINE|re.DOTALL)


def brace_lexer(text):
    """
    Convert a block of text into a list of token tuples
    in the format (integer, string) where integer is:
        1 = substitution key with braces stripped
        2 = unmatched open or close brace character
        3 = other (plain text)
    """
    pos = 0
    end = len(text)
    tokens = []
    while pos < end:
        match = _BRACE_REGEX.match(text, pos)
        ## TODO: Remove this test for production, should always get a match.
        if match:
            kind = match.lastindex
            value = match.group(kind)
            tokens.append( (kind, value) )
            pos = match.end()
        else:
            raise ValueError("Error brace lexing: %s" % text )
    return tokens
