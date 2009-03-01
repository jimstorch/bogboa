# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   File:       mudlib/stringsub.py
#   Author:     Jim Storch
#------------------------------------------------------------------------------

from mudlib import shared


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

    