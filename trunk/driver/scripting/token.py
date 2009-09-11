# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   driver/scripting/token.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

from driver.error import BogScriptError
from driver.scripting.source_iter import CharIter
from driver.scripting.security import WHITELIST


NUMBER_START = '-.1234567890'
NUMBER_MORE = '.1234567890'
ID_START = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
ID_MORE = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_1234567890.'
SYMBOLS = '={}(),;*/'
CONDITIONALS = ['if', 'elif', 'else',]
KEYWORDS = ['and', 'or', 'not',]


#-------------------------------------------------------------------------Token

class Token(object):
   
    def __init__(self, category=None, value=None, line_number=None, 
            char_number=None):
        self.category = category
        self.value = value
        self.line_number = line_number
        self.char_number = char_number

    def __str__(self):
        return ( self.category + ', ' + self.value + ', ' + 
            str(self.line_number) + ', ' + str(self.char_number) )


#--------------------------------------------------------------------Token Iter

class TokenIter(object):

    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0
        self.last = len(tokens) - 1

    def __iter__(self):
        return self

    def next(self):
        if self.index > self.last:
            raise StopIteration
        retval = self.tokens[self.index]
        self.index += 1
        return retval

    def previous_token(self):
        if index > 1:
            return self.tokens[self.index -2]
        else:
            return None
        
    def next_token(self):
        if self.index < self.last:
            return self.tokens[self.index]
        else:
            return None


#---------------------------------------------------------------------Tokenizer

class Tokenizer(object):

    """
    Given source as a character stream, break it into tokens for the parser.
    Used inside the Parser class.
    """ 
    
    def __init__(self, bogscript):
        self.char_iter = CharIter(bogscript)
        self.tokens = []
        self._tokenize()

    def create_token(self, category, value):
        token = Token(category, value, 
            self.char_iter.current_line_number(),
            self.char_iter.current_char_number())
        return token

    def _tokenize(self):

        ## "Everyone writes a crummy parser/tokenizer by hand at least once"
        lex = ''
        state = 'hunting'
        quote_style = None
        space_count = 0
        newline_count = 0
        
        for char in self.char_iter:

            ## Start of a new lexeme
            if state == 'hunting':

                if char == ';' or char == '\n':
                    token = self.create_token('symbol', 'eol')
                    self.tokens.append(token)
                    continue  

                if char.isspace():
                    continue

                if char == '#':
                    state = 'comment'
                    continue
              
                if char == '=':
                    token = self.create_token('symbol', 'assignment')
                    self.tokens.append(token)
                    continue

                if char == '*':
                    token = self.create_token('symbol', 'multiplication')
                    self.tokens.append(token)
                    continue

                if char == '/':
                    token = self.create_token('symbol', 'division')
                    self.tokens.append(token)
                    continue

                if char == '{':
                    token = self.create_token('symbol', 'begin_block')
                    self.tokens.append(token)                    
                    continue

                if char == '}':
                    token = self.create_token('symbol', 'end_block')
                    self.tokens.append(token)                    
                    continue

                if char == '(':
                    token = self.create_token('symbol', 'begin_paren')
                    self.tokens.append(token)
                    continue

                if char == ')':
                    token = self.create_token('symbol', 'end_paren')
                    self.tokens.append(token)
                    continue

                if char == '\"':
                    state = 'quoting'
                    quote_style = 'double'
                    continue

                if char == '\'':
                    state = 'quoting'
                    quote_style = 'single'
                    continue

                if char == ',':
                    token = self.create_token('symbol', 'separator')
                    self.tokens.append(token)
                    continue                    

                if char in NUMBER_START:
                    lex += char
                    state = 'numberish'
                    continue

                if char in ID_START:
                    lex += char
                    state = 'wordish'
                    continue

                ## Ran into something unknown
                raise BogScriptError(
                    'Tokenizer encountered a syntax error near:\n%s' %
                    self.char_iter.trace() )          

            elif state == 'comment':
                ## Are we at the end of a line?
                if char == '\n':
                    ## If so, cancel comment state
                    state = 'hunting'
                    continue    
        
            elif state == 'quoting':

                ## Handle newlines, note the fall-through to the next 'if'
                ## since newlines are also white spaces
                if char == '\n':
                    newline_count += 1
                    ## Only pass the second of two or more newlines
                    if newline_count == 2:    
                        lex += '\n'
                else:
                    newline_count = 0

                ## Handle whitespace (spaces, tabs, and newlines)
                if char.isspace():
                    space_count += 1
                    ## Only pass the first of one or more whitespaces
                    if space_count == 1:
                        lex += ' '
                    continue
                else:
                    space_count = 0

#                ## Consume a backslash if it precedes a quote mark
#                if char == '\\':
#                    next = self.char_iter.next_char()
#                    print "Next = %s" % next
#                    if next == '\'' or next == '\"':
#                        continue

#                ## Pass an escaped single quote
#                if char == '\'':
#                    prev = self.char_iter.prev_char()
#                    if prev == '\\':
#                        lex += '\''
#                        continue

#                ## Pass an escaped double quote
#                if char == '\"':
#                    prev = self.char_iter.prev_char()
#                    if prev == '\\':
#                        lex += '\"'
#                        continue

                ## Handle closing quotes of either style
                if char =='\"' and quote_style == 'double':
                    token = self.create_token('string', lex)
                    self.tokens.append(token)
                    lex = ''
                    newline_count = 0
                    space_count = 0
                    state = 'hunting'
                    quote_style = None
                    continue                                    
                
                elif char == '\'' and quote_style == 'single':
                    token = self.create_token('string', lex)
                    self.tokens.append(token)
                    lex = ''
                    newline_count = 0
                    space_count = 0
                    state = 'hunting'
                    quote_style = None
                    continue                        

                ## Otherwise, carry the character
                lex += char
                continue
                                                   
            elif state == 'numberish':
                if char.isspace() or char in SYMBOLS:
                    
                    if len(lex) > 12:
                        raise BogScriptError('Oversized number.\n%s' %
                            self.char_iter.trace() )                          

                    if '.' in lex:
                        token = self.create_token('float', lex)    
                    else:
                        token = self.create_token('integer', lex) 
                    self.tokens.append(token)                    
                    state = 'hunting'
                    lex = ''
                    self.char_iter.roll_back()
                    continue

                elif char not in NUMBER_MORE:
                    raise BogScriptError(
                        'Illegal character in numeric value.\n%s' %
                        self.char_iter.trace() )

                else:
                    lex += char
                    continue

            elif state == 'wordish':
                ## Have we completed a word?
                if char.isspace() or char in SYMBOLS:

                    ## Is it a function call?
                    if char == '(' or self.char_iter.next_non_space() == '(':
                        ## Legal function name?
                        ## TODO: Re-enable this check
#                        if lex not in WHITELIST:
#                            raise BogScriptError("Security Error: "
#                            "Function call '%s' is not in whitelist\n%s" %
#                            (lex, self.char_iter.trace() ) )                              

                        token = self.create_token('call', lex)
                        self.tokens.append(token)                    
                        state = 'hunting'
                        lex = ''
                        self.char_iter.roll_back()
                        continue  

                    if lex in CONDITIONALS:
                        token = self.create_token('conditional', lex)
                        self.tokens.append(token)                    
                        state = 'hunting'
                        lex = ''
                        self.char_iter.roll_back()
                        continue                        

                    elif lex in KEYWORDS:
                        token = self.create_token('keyword', lex)
                        self.tokens.append(token)                    
                        state = 'hunting'
                        lex = ''
                        self.char_iter.roll_back()
                        continue    
            
                    else:
                        token = self.create_token('indentifier', lex)
                        self.tokens.append(token)                    
                        state = 'hunting'
                        lex = ''
                        self.char_iter.roll_back()
                        continue

                elif char not in ID_MORE:
                    raise BogScriptError('Tokenizer Error: '
                        'illegal character in keyword/identifier.\n%s' %
                        self.char_iter.trace() )

                else:
                    lex += char
                    continue
        
        if state == 'quoting':
            raise BogScriptError('Tokenizer Error: '
                'Quoted string was never closed.\n%s' %
                self.char_iter.trace() )              
              
