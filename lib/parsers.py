##-----------------------------------------------------------------------------
##  File:       parsers.py
##  Purpose:    various parsers to extract command data on a per verb basis
##  Author:     Jim Storch
##-----------------------------------------------------------------------------


#--------------------------------------------------------------------Split Verb
   
def split_verb(text):

    """Break a sentence into the verb and the balance of the remaining words.
    Strips off trailing punctuation and extra spaces.
    Returns a (verb, balance) tuple."""    
    
    words = text.split()
    count = len(words)

    if count == 0:
        verb = None
        balance = []        

    elif count == 1:
        verb = words[0].lower()
        balance = []

    else:
        verb = words[0].lower()
        balance = words[1:] 
   
    return (verb, balance)

    
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
    

