# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/sys/__init__.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

"""
Module to Manage Logs, Scheduling, and Network IO.
"""


from mudlib.sys.log import Log
from mudlib.sys.error import *

## Shared Log instance
THE_LOG = Log('server.log', append=True)
