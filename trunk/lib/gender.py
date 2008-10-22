##-----------------------------------------------------------------------------
##  File:       lib/gender.py
##  Author:     Jim Storch
##-----------------------------------------------------------------------------

import sys

from lib.shared import GENDER

#------------------------------------------------------------------------Gender

class Gender(object):

    def __init__(self):
    
        self.uuid = None
        self.name = None
        self.module = None
        
        self.nominative = None
        self.objective = None
        self.possessive_noun = None
        self.noun_possessive = None
        self.reflexive = None


#---------------------------------------------------------------Register gender

def register_gender(gender):

    """
    Given a configured gender, register it with the shared gender dictionary.
    """

    if gender.uuid in GENDER:
        print ( "ERROR! Duplicate UUID (%s) found while registering "
            "gender '%s' from module '%s'."  %  (
            gender.uuid, gender.name, gender.module) )
        sys.exit(1)
    else:
        GENDER[gender.uuid] = gender


#-------------------------------------------------------------Configured Gender

def configured_gender(cfg):

    """
    Given a configuration dictionary, create a gender and configure it.
    Returns the configured gender.
    """

    gender = Gender()

    if 'name' in cfg:
        gender.name = cfg.pop('name')
    else:
        print "ERROR! Missing name in gender config."
        sys.exit(1)

    if 'uuid' in cfg:
        gender.uuid = cfg.pop('uuid')
    else:
        print "ERROR! Missing UUID in config for gender '%s'." % gender.name
        sys.exit(1)

    if 'desc' in cfg:
        gender.desc = cfg.pop('desc')
    else:
        gender.desc = None

    if 'module' in cfg:
        gender.module = cfg.pop('module')
    else:
        gender.module = None

    if 'nominative' in cfg:
        gender.nominative = cfg.pop('nominative')
    else:
        gender.nominative = None
    
    if 'objective' in cfg:
        gender.objective = cfg.pop('objective')
    else:
        gender.objective = None

    if 'possessive_noun' in cfg:
        gender.possessive_noun = cfg.pop('possessive_noun')
    else:
        gender.possessive_noun = None

    if 'noun_possessive' in cfg:
        gender.noun_possessive = cfg.pop('noun_possessive')
    else:
        gender.noun_possessive = None

    if 'reflexive' in cfg:
        gender.reflexive = cfg.pop('reflexive')
    else:
        gender.reflexive = None

    ## Complain if there are leftover keys -- probably a typo in the YAML
    if cfg:
        print ( "WARNING! Unrecognized key(s) in config for gender '%s': %s" 
            % ( gender.name, cfg.keys()) ) 

    return gender         
