# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/stat/__init__.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

"""
Stats
-----

Stats are character statistics.  Derived from the Actor's race and increased
(or lowered) by equipment and spells.

The stats in use are:

    Physical    Mental
    ---------------------
    Brawn       Knowledge
    Vigor       Faith
    Precision   Cunning

Warrior     - brawn, vigor, precision
Monk        - Precision, Faith, Vigor
Paladin     - Brawn, Faith, Knowledge
Priest      - Faith, Knowledge, Precision  
Necromancer - Knowledge, Precision, Cunning    
Ninja       - Cunning, Precision, Brawn  
Ranger      - Precision, Faith, Cunning 
Rogue       - Precision, Brawn, Cunning
Shaman      - Faith, Brawn, Knowledge
Druid       - Knowledge, Faith, Cunning

"""


from mudlib.stat.stat_math import *



