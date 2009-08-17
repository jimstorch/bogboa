# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/parsers.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

    
#---------------------------------------------------------------------Monologue    
    
def monologue(words):

    """Parse text directed at no one in particular."""

    return (' '.join(words),)
    


#----------------------------------------------------------------------Dialogue

def dialogue(words):

    """Parse text directed at a target."""

    count = len(words)

    if count == 0:
        target = None
        text = ''

    elif count == 1:
        target = words[0].lower()
        text = ''

    else:
        target = words[0].lower()
        text = ' '.join(words[1:])

    return (target, text)

#----------------------------------------------------------------------Singular

def singular(words):

    """Test that input was a single word"""

    if len(words) == 0:
        retval = True

    else:
        retval = False

    return retval
    

