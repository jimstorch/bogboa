# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   driver/dsl.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

import re

from driver.error import BogScriptError

#-------------------------------------------------------------------------Lexer

##  References:
##  http://www.evanfosmark.com/2009/02/sexy-lexing-with-python/
##  http://www.gooli.org/blog/a-simple-lexer-in-python/
##  http://effbot.org/zone/xml-scanner.htm


def group_re(items):
    bounded = [ item + r'\b' for item in items ]
    return '(' + '|'.join(bounded) + ')'


## The following keywords are not permitted within scripts.  Expand as needed.
_RESTRICTED = [
    'Exception', '__builtin__', '__class__', '__debug__', '__dict__',
    '__init__', '__local__', '__subclasses__', 'as', 'assert', 'break',
    'class', 'compile', 'continue', 'def', 'del', 'delattr', 'dict',
    'dir', 'eval', 'except', 'exec', 'execfile', 'exit', 'file', 'finally',
    'for', 'from', 'getattr', 'global', 'import', 'input', 'lambda', 'locals',
    'object', 'open', 'property', 'raise', 'raw_input', 'reload', 'return',
    'setattr', 'staticmethod', 'try', 'while', 'with', 'yield',
    ]

_CONDITIONALS = ['if', 'elif', 'else',]
_KEYWORDS = ['and', 'in', 'is', 'not', 'or', 'print',]

## Regular expressions to parse script tokens.  Order matters!
_DEFINITIONS = [
    ("comment", r"#[^\r\n]*"),
    ("string", r"""[ru]?(\"([^\"\\]|(\\.))*\")|('([^\'\\]|(\\.))*')"""),
    ("restricted", group_re(_RESTRICTED)),
    ("conditional", group_re(_CONDITIONALS)),
    ("keyword", group_re(_KEYWORDS)),
    ("blockstart", r"{"),
    ("blockend", r"}"),
    ("eol", r"[\n]"),
    ("operator", r"[%s]+" % re.escape("<>=*/+-~!%&()|[],.?;")),
    ("identifier", r"[A-Za-z_][A-Za-z0-9_]*"),
    ("integer", r"[0-9]+"),
    ("float", r"[0-9.]+"),
    ("whitespace", r"[ \t\r]+"),
    ("unknown", r".+"),
    ]

_PARTS = []
for name, part in _DEFINITIONS:
    _PARTS.append("(?P<%s>%s)" % (name, part))
_REGEX_STRING = "|".join(_PARTS)
_REGEX = re.compile(_REGEX_STRING, re.MULTILINE)


def lexer(source):

    """
    Convert a script source string into tokens.
    Returns a list of tuples in the format (token name, value, line number).
    """

    pos = 0
    end = len(source)
    line_number = 1
    tokens = []

    while pos < end:
        match = _REGEX.match(source, pos)
        if match:
            name = match.lastgroup
            value = match.group(0)
            tokens.append( (name, value, line_number) )
            if name == 'eol':
                line_number += 1
            pos = match.end()
        else:
            ## This should never occur since 'unknown' matches anything.
            raise ValueError("Unmatched script segment on line %d." %
                line_number)

    return tokens


#-------------------------------------------------------------------------PyGen

## Indention is four spaces
__INDENT = chr(32) * 4

def pygen(tokens):

    """
    Given a list of token tuples from lexer(), generates a string of Python
    source code.
    """

    pycode = ''
    indent_level = 0
    parens = 0
    is_conditional = False
    line = ''

    for token, value, line_number in tokens:

        if token == 'eol':
            if is_conditional:
                line += ':'
                is_conditional = False
            if not line.isspace():
                pycode += line + '\n'
            line = __INDENT * indent_level

        elif token == 'whitespace' or token == 'comment':
            continue

        elif token == 'blockstart':
            indent_level += 1

        elif token == 'blockend':
            indent_level -= 1

        elif token == 'conditional':
            line += value + chr(32)
            is_conditional = True

        elif token in ['identifier', 'string', 'keyword', 'integer', 'float']:
            line += value

        elif token == 'operator':
            line += value
            ## Count parentheses
            if value == '(':
                parens += 1
            if value == ')':
                parens -= 1

        elif token == 'restricted':
            raise BogScriptError("Use of restricted keyword '%s' on line %d."
                % (value, line_number))

        elif token == 'unknown':
            raise BogScriptError("Unknown instruction '%s:%s' on line %d."
                % (token, value, line_number))

        else:
            ## This should never occur since 'unknown' matches anything.
            raise ValueError("Unmatched script token '%s:%s' on line %d."
                % (token, value, line_number))

    if indent_level > 0:
        raise BogScriptError('Unmatched opening brace in source.')
    if indent_level < 0:
        raise BogScriptError('Unmatched closing brace in source.')
    if parens > 0:
        raise BogScriptError('Unmatched opening parenthesis in source.')
    if parens < 0:
        raise BogScriptError('Unmatched closing parenthesis in source.')

    return pycode


#-----------------------------------------------------------------------ByteGen

def bytegen(pycode):

    """
    Given a string of generated Python source from pygen(),
    attempts to compile it into Python byte Code.
    """

    try:
        bytecode = compile(pycode, 'pygen script', 'exec')

    except SyntaxError, error:
        raise BogScriptError("ByteGen Compile Error: %s\n" % error)

    return bytecode
