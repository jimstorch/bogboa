# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/sys/config.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

import sys

from mudlib.dat.file_loader import parse_file


#--[ Read Configuration ]------------------------------------------------------

"""
Read the settings from data/config.yml.
Please edit that file to make changes.
"""

_cfg = parse_file('data/config.yml')

PORT = _cfg['port']
ADDRESS = _cfg['address']
IDLE_TIMEOUT = _cfg['idle_timeout']
YEAR_OFFSET = _cfg['year_offset']

## YAML uses None for empty values, which would choke socket.bind()
if ADDRESS == None:
    ADDRESS = ''

START_UUID = _cfg['start_uuid']
