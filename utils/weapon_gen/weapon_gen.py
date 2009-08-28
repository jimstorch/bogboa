#!/usr/bin/env python
#------------------------------------------------------------------------------
#   weapon_gen.py
#   Copyright 2006 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

import random

class Words:
	"""Manage a list of words loaded from a text file."""
	def __init__(self, word_file=None):
		self.word_count = 0
		self.word_list = []
		if word_file:
			self.read_file(word_file)
	def read_file(self, word_file):
		file = open(word_file,'r')
		for line in file:
			if line:
				self.word_list.append(line.strip('\n'))
				self.word_count += 1
	def random(self):
		return self.word_list[random.randint(0,self.word_count - 1)]


if __name__ == "__main__":
	nouns = Words("noun.txt")
	adjectives = Words("adjective.txt")
	aspects = Words("aspect.txt")
	random.seed()
	for x in xrange(23):
		r = random.randint(0,2)
		if r == 0:
			print adjectives.random(), nouns.random()
		elif r == 1:
			print nouns.random(), "of", aspects.random()
		elif r == 2:
			print adjectives.random(), nouns.random(), "of", aspects.random()
			
	
