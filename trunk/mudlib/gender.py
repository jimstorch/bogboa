# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   File:       mudlib/gender.py
#   Author:     Jim Storch
#------------------------------------------------------------------------------


class Neutral(object):

    noun = 'thing'
    nominative = 'it'
    objective = 'it'
    possessive_noun = 'its'
    noun_possessive = 'its'
    reflexive = 'itself'
    kinship = 'Friend'


class Female(Neutral):

    noun = 'female'
    nominative = 'she'
    objective = 'her'
    possessive_noun = 'her'
    noun_possessive = 'hers'
    reflexive = 'herself'
    kinship = 'Sister'


class Male(Neutral):

    noun = 'male'
    nominative = 'he'
    objective = 'him'
    possessive_noun = 'his'
    noun_possessive = 'his'
    reflexive = 'himself'
    kinship = 'Brother'


class Group(Neutral):

    noun = 'group'
    nominative = 'they'
    objective = 'them'
    possessive_noun = 'their'
    noun_possessive = 'theirs'
    reflexive = 'themselves'
    kinship = 'Friends'    







#import sys

#from mudlib.shared import GENDERS


##------------------------------------------------------------------------Gender

#class Gender(object):

#    def __init__(self):
#    
##        self.uuid = None
#        self.name = None
#        self.module = None
#        
#        self.nominative = None
#        self.objective = None
#        self.possessive_noun = None
#        self.noun_possessive = None
#        self.reflexive = None
#        self.kinship = None

##--------------------------------------------------------------Configure Gender

#def configure_gender(cfg):

#    """
#    Given a configuration dictionary, create a gender and configure it.
#    Returns the configured gender.
#    """

#    gender = Gender()

#    if 'name' in cfg:
#        gender.name = cfg.pop('name')
#    else:
#        print "ERROR! Missing name in gender config."
#        sys.exit(1)

##    if 'uuid' in cfg:
##        gender.uuid = cfg.pop('uuid')
##    else:
##        print "ERROR! Missing UUID in config for gender '%s'." % gender.name
##        sys.exit(1)

#    if 'desc' in cfg:
#        gender.desc = cfg.pop('desc')
#    else:
#        gender.desc = None

#    if 'module' in cfg:
#        gender.module = cfg.pop('module')
#    else:
#        gender.module = None

#    if 'nominative' in cfg:
#        gender.nominative = cfg.pop('nominative')
#    else:
#        gender.nominative = None
#    
#    if 'objective' in cfg:
#        gender.objective = cfg.pop('objective')
#    else:
#        gender.objective = None

#    if 'possessive_noun' in cfg:
#        gender.possessive_noun = cfg.pop('possessive_noun')
#    else:
#        gender.possessive_noun = None

#    if 'noun_possessive' in cfg:
#        gender.noun_possessive = cfg.pop('noun_possessive')
#    else:
#        gender.noun_possessive = None

#    if 'reflexive' in cfg:
#        gender.reflexive = cfg.pop('reflexive')
#    else:
#        gender.reflexive = None

#    if 'kinship' in cfg:
#        gender.kinship = cfg.pop('kinship')
#    else:
#        gender.kinship = None

#    ## Complain if there are leftover keys -- probably a typo in the YAML
#    if cfg:
#        print ( "WARNING! Unrecognized key(s) in config for gender '%s': %s" 
#            % ( gender.name, cfg.keys()) ) 

#    return gender


##---------------------------------------------------------------Register Gender

#def register_gender(gender):

#    """
#    Given a configured gender, register it with the shared gender dictionary.
#    """

#    if gender.name in GENDERS:
#        print ( "ERROR! Duplicate name (%s) found while registering "
#            "gender '%s' from module '%s'."  %  (
#            gender.uuid, gender.name, gender.module) )
#        sys.exit(1)
#    else:
#        GENDERS[gender.name] = gender         
