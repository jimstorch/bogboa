#!/usr/bin/env python
#------------------------------------------------------------------------------
#   clean.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

fname_in =  'data/elves.txt'
fname_out = 'data/elves2.txt'
min_length = 4
max_lines = 1000

fin = open(fname_in, 'rt')
lines = fin.readlines()

wordlist = []

for line in lines:
    words = line.split()
    if words:
        word = words[0].lower()
        if word.isalpha() and word not in wordlist and len(word) >= min_length:
            wordlist.append(word)
    if len(wordlist) >= max_lines:
        break

wordlist.sort()

print wordlist
print len(wordlist)

fout = open(fname_out, 'wt')
text = '\n'.join(wordlist)
fout.write(text)
