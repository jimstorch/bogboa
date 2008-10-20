#!/usr/bin/env python
##-----------------------------------------------------------------------------
##  File:       ugen.py
##  Author:     Jim Storch
##-----------------------------------------------------------------------------

"""
Create a text file called 'uuid_list.txt' with 1000 randomly generated
UUID's suitable for cutting and pasting as needed.  Many text editors will
select the enter line by triple clicking.

See: http://en.wikipedia.org/wiki/UUID
"""


import uuid

fp = open('uuid_list.txt', 'w')

for x in range(1000):
    fp.write(str(uuid.uuid4()) + '\n')

fp.close()



