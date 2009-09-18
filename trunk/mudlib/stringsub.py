# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/stringsub.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

from mudlib import shared


"""
${name}

${nom}      # Nominative form; he, she, it, they
${obj}      # Objective form; him, her, it, them
${pos}      # Possessive form; his, her, its, their
${npos}     # Noun possessive; his, hers, its, theirs
${refl}     # Reflexive form; himself, herself, itself, themselves

${guild}
${race}
${race_plur}

${target}
${target_race}
${target_guild}

"""


class StringSub(object):

    """
    Dictionary-like object that provides a substitution list for flavor text.
    """

    def __init__(self, client):

        self.client = client

    #------------------------------------------------------------------Get Item

    def __getitem__(self, key):

        ## Client Attributes

        if key == 'foo':
            retval = 'bar'

        ## Avatar Attributes

        elif key == 'name':
            if client.avatar:
                retval = client.avatar.name
            else:
                retval = '{name: no avatar}'

        elif key == 'race':
            if client.avatar:
                retval = client.avatar.race
            else:
                retval = '{race: no avatar}'

        elif key == 'level':
            if client.avatar:
                retval = client.avatar.level
            else:
                retval = '{level: no avatar}'

        ## Hostile Target Attributes

        elif key == 't':
            if client.target:
                retval = client.target.name
            else:
                retval = '{no target}'

        ## Beneficial Target Attributes

        elif key == 'bt':
            if client.btarget:
                retval = client.btarget.name
            else:
                retval = '{no beneficial target}'

        ## Conversational Target Attributes

        elif key == 'ct':
            if client.ctarget:
                retval = client.ctarget.name
            else:
                retval = '{no conversation target}'

        ## Room Attributes

        elif key == 'room':
            if client.room:
                retval = client.room.name
            else:
                retval = '{no room}'

        elif key == 'module':
            if client.room:
                retval = client.room.module
            else:
                retval = '{module: no room}'

        ## World Attributes

        elif key == 'realm':
            retval = shared.SERVER_NAME

        elif key == 'time':
            retval = 'FIXME: time'

        elif key == 'tod':
            retval = 'FIXME; tod'


        ## Else, bad key request

        else:
            retval = '{UNKNOWN KEY:%s}' % key

        return retval
