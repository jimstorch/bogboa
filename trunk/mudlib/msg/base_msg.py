# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/msg/base_msg.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

"""
Base Class for Action Messages.
"""

#   {sname}     Name of the Actor that is the source of the Action
#   {sweap}     Name of the source Actor's Weapon
#   {sability}  Name of the source Actor's Ability
#   {salias}    Alias of the source Actor
#   {srace}     Race of the source Actor
#   {sgender}   Gender of the source Actor
#   {sguild}    Guild of the source Actor
#   {snom}      Nominative Form; he, she, it, they
#   {sobj}      Objective Form; him, her, it, them
#   {spos}      Possesive Form; his, her, its, their
#   {snpos}     Noun-Possessive Form; his hers, its, theirs
#   {sreflx}    Reflexive Form; himself, herself, itself, themselves
#   {tname}     Name of the Actor targeted by the action
#   {tweap}     Name of the target Actor's weapon
#   {tability}  Name of the target Actor's ability
#   {talias}    Alias of the target Actor
#   {trace}     Race of the target Actor
#   {tgender}   Gender of the target Actor
#   {tguild}    Guild of the target Actor
#   {tnom}      See above
#   {tobj}      ""
#   {tpos}      ""
#   {tnpos}     ""
#   {treflx}    ""
#   {val}       Value passed to the ActionMessage


class BaseMsg(object):

    source = ''
    viewer = ''

    def __init__(self, src=None, tar=None, val=None):

        self.source_msg = self._text_sub(self.source, src, tar, val)
        self.target_msg = self._text_sub(
            self.viewer.replace('{tname}', 'you'), src, tar, val)
        self.spectator_msg = self._text_sub(self.viewer, src, tar, val)

    def _text_sub(self, text, src, tar, val):

        if src:
            text = text.replace('{sname}', src.get_name())
            text = text.replace('{salias}', src.get_alias())
            text = text.replace('{srace}', src.get_race())
            text = text.replace('{sgender}', src.get_gender())        
            text = text.replace('{sguild}', src.get_guild())        
            text = text.replace('{snom}', src.get_nom())           
            text = text.replace('{sobj}', src.get_obj())       
            text = text.replace('{spos}', src.get_pos())               
            text = text.replace('{snpos}', src.get_npos())          
            text = text.replace('{sreflx}', src.get_reflx())

        if tar:
            text = text.replace('{tname}', tar.get_name())
            text = text.replace('{talias}', tar.get_alias())
            text = text.replace('{trace}', tar.get_race())
            text = text.replace('{tgender}', tar.get_gender())        
            text = text.replace('{tguild}', tar.get_guild())        
            text = text.replace('{tnom}', tar.get_nom())           
            text = text.replace('{tobj}', tar.get_obj())       
            text = text.replace('{tpos}', tar.get_pos())               
            text = text.replace('{tnpos}', tar.get_npos())          
            text = text.replace('{treflx}', tar.get_reflx())

        if val and '{val}' in text:
            text = text.replace('{val}', val)

        return text    
                   
