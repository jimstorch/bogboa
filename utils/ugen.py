#!/usr/bin/env python
#------------------------------------------------------------------------------
#   ugen.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

"""
Create a text file called 'uuid_list.txt' with 1000 randomly generated
UUID's suitable for cutting and pasting as needed.  Many text editors will
select the enter line by triple clicking.

Using the hex version (without the dashes) so it's easier to click and paste.

See: http://en.wikipedia.org/wiki/UUID
"""


import uuid

fp = open('uuid_list.txt', 'w')

for x in range(1000):
    fp.write(uuid.uuid4().get_hex() + '\n')

fp.close()



