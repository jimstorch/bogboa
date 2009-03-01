# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   File:       driver/config.py
#   Author:     Jim Storch
#------------------------------------------------------------------------------

import sys

from driver.loader.file_loader import parse_file


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


