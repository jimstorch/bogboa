# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   driver/decorate.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------


#--[ Caret Code to ANSI TABLE ]------------------------------------------------

ANSI_CODES = (

    # Note: order here matters to keep '^b' from clobbering '^bb'
    ( '^kb', '\x1b[40m' ),          # black background
    ( '^rb', '\x1b[41m' ),          # red background
    ( '^gb', '\x1b[42m' ),          # green background
    ( '^yb', '\x1b[43m' ),          # yellow background
    ( '^bb', '\x1b[44m' ),          # blue background
    ( '^mb', '\x1b[45m' ),          # magenta background
    ( '^cb', '\x1b[46m' ),          # cyan background
    ( '^k', '\x1b[22;30m' ),        # black
    ( '^K', '\x1b[1;30m' ),         # bright black (grey)
    ( '^r', '\x1b[22;31m' ),        # red
    ( '^R', '\x1b[1;31m' ),         # bright red
    ( '^g', '\x1b[22;32m' ),        # green
    ( '^G', '\x1b[1;32m' ),         # bright green
    ( '^y', '\x1b[22;33m' ),        # yellow
    ( '^Y', '\x1b[1;33m' ),         # bright yellow
    ( '^b', '\x1b[22;34m' ),        # blue
    ( '^B', '\x1b[1;34m' ),         # bright blue
    ( '^m', '\x1b[22;35m' ),        # magenta
    ( '^M', '\x1b[1;35m' ),         # bright magenta
    ( '^c', '\x1b[22;36m' ),        # cyan
    ( '^C', '\x1b[1;36m' ),         # bright cyan
    ( '^w', '\x1b[22;37m' ),        # white
    ( '^W', '\x1b[1;37m' ),         # bright white
    ( '^d', '\x1b[39m' ),           # default (should be white on black)    
    ( '^i', '\x1b[7m' ),            # inverse text on  
    ( '^I', '\x1b[27m' ),           # inverse text off
    ( '^^', '\x1b[0m' ),            # reset all
    ( '^_', '\x1b[4m' ),            # underline on
    ( '^-', '\x1b[24m' ),           # underline off
    ( '^!', '\x1b[1m' ),            # bold on
    ( '^1', '\x1b[22m'),            # bold off
    ( '^s', '\x1b[2J'),             # clear screen
    ( '^l', '\x1b[2K'),             # clear to end of line
    )


#--[ Colorize ]----------------------------------------------------------------

def colorize(text, ansi=True):
    """ If the client wants ansi, replace the tokens with ansi sequences --
    otherwise, simply strip them out."""

    if ansi:
        for token, code in ANSI_CODES:
            text = text.replace(token, code)

    else:
        text = strip_caret_codes(text)
       
    return text


#--[ Strip Caret Codes ]-------------------------------------------------------

def strip_caret_codes(text):

    """Strip out any caret codes from a string."""

    for token, throwaway in ANSI_CODES:
        text = text.replace(token, '')
    return text



#--[ Word Wrap ]---------------------------------------------------------------

def word_wrap(text, columns=78, indent=2, padding=2):
    """Wraps a block of text to a set column-width with paragraph indentation
    and left padding.  Single newlines are not preserved, but double-newlines 
    (paragraph breaks) are.  Designed to give text an easy to read, book-like
    appearance.
    Note: Caret Codes don't display so will cause some lines to shorten."""
    # Initially, I wanted to split on '\n\n', but that would have missed lines
    # that were only white space -- like '\n\t\t\n'.
    paragraphs = text.split('\n')
    wtext = ''
    line = ' ' * padding + ' ' * indent
    for para in paragraphs:
        if len(para.strip()):
            words = para.split()
            for word in words:        
                if ( len(line) + len(word) + 1 ) < columns:
                    line += word + ' '
                else:
                    wtext += line + '\n'
                    line = ' ' * padding + word + ' '
        # So I check here        
        else:
            wtext += line + '\n\n'
            line = ' ' * padding + ' ' * indent
    wtext += line            
    return wtext

