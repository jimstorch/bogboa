# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   driver/scripting/source_iter.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

"""
Classes to support line and character based iteration of event source.
"""

#---------------------------------------------------------------------Line Iter

## Splitting the iterators like this makes it easier to keep track of
## line numbers for meaningful error messages.

class LineIter(object):

    """
    Break a block of source script into lines and iterate them.
    Used inside the CharIter class.
    """

    def __init__(self, text):
        self.lines = text.split('\n')
        self.last_row = len(self.lines) - 1
        self.row = 0

    def __iter__(self):
        return self

    def next(self):
        if self.row > self.last_row:
            raise StopIteration
        retval = self.current_line()
        self.row += 1
        return retval

    def roll_back(self):
        if self.row > 0:
            self.row -= 1
        return self.current_line()

    def prev_line(self):
        if self.row > 1:
            return self.lines[self.row - 2]
        else:
            return ''

    def current_line(self):
        if self.row > 0:
            return self.lines[self.row - 1]
        else:
            return ''

    def next_line(self):
        if self.row < self.last_row:
            return self.lines[self.row]
        else:
            return ''
    
    def current_line_number(self):
        return self.row + 1


#---------------------------------------------------------------------Char Iter

class CharIter(object):
    
    """
    Break the lines of a source script into charaters and iterate them.
    Used inside the Tokenizer class.
    """

    def __init__(self, text):
        self.line_iter = LineIter(text) 
        self.line = self.line_iter.next() + '\n'
        self.last_column = len(self.line) - 1
        self.column = 0

    def __iter__(self):
        return self            

    def next(self):

        if self.column > self.last_column:
            self.line = self.line_iter.next() + '\n'
            self.last_column = len(self.line) - 1
            self.column = 0

        retval = self.current_char()
        self.column += 1
        return retval

    def roll_back(self):
        if self.column > 0:
            self.column -= 1
        else:
            self.line = self.line_iter.roll_back() + '\n'
            self.last_colum = len(self.line)
            self.column = self.last_column            

    def prev_char(self):
        if self.column > 1:
            return self.line[self.column - 2]
        else:
            return '\n'
        
    def current_char(self):
        return self.line[self.column]

    def next_char(self):
        if self.column < self.last_column:
            return self.line[self.column]
        else:
            return ''

    def next_non_space(self):
        rest = self.line[self.column:].strip()
        if len(rest) > 0:
            return rest[0]
        else:
            return '\n'

    def current_line(self):
        return self.line
  
    def current_line_number(self):
        return self.line_iter.current_line_number()

    def current_char_number(self):
        return self.column + 1


    def trace(self):
        col = self.column
        if col > 1:
            arrow = '-' * (col -1) + '^'
        else:
            arrow = '^'
        msg = 'Line %d, character %d:' % (
            self.current_line_number(), col) 
        msg += '\n' + self.current_line()
        msg += '\n' + arrow

        return msg

