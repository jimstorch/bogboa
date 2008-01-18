#!/usr/bin/env python

import random

## From http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/117241
def weighted_rand(wlist):
    wtotal = sum([x[1] for x in wlist])
    n = random.uniform(0, wtotal)
    for item, weight in wlist:
        if n < weight:
            break
        n = n - weight
    return item

def between(num, lower, upper):
    if num >= lower and num <= upper:
        return True
    else:
        return False


class Vowel(object):
    freq = [ ('e',.20), ('a',.15), ('o',.10), ('i', .09), ('u',.08), ('y',.03),
        ('ou',.03), ('ie',.03), ('oo', .02), ('ee', .03), ('ae', .03),
        ('oi',.03), ('ea',.03) ]

    def rand(self):
        return weighted_rand(self.freq)

class Prefix(object):
    freq = [ ('t',.25), ('n',.24), ('r',.23), ('s',.22), ('h',.23), ('d',.22),
        ('l',.20), ('c',.19), ('m',.18), ('w',.17), ('f',.16), ('p',.15),
        ('g',.14), ('b',.13), ('v',.12), ('k',.11), ('j',.10), ('x',.03),
        ('qu',.01), ('z',.02),
        ('th',.15), ('st', .15),
        ('bl',.10), ('br',.10), ('cl',.10), ('cr',.10), ('dr',.10),
        ('fr',.10), ('fl',.10), ('sl',.10), ('st',.10), ('pr',.10),
        ('pl',.10), ('kr',.10), ('kl',.10), ('vl',.02), ('wr',.10),
        ('thr',.10),
        ]

    def rand(self):
        return weighted_rand(self.freq)

class Inner(object):
    freq = [ ('t',.25), ('n',.24), ('r',.23), ('s',.22), ('h',.23), ('d',.22),
        ('l',.20), ('c',.19), ('m',.18), ('w',.17), ('f',.16), ('p',.15),
        ('g',.14), ('b',.13), ('v',.12), ('k',.11), ('j',.10), ('x',.06),
        ('qu',.05), ('z',.10), ('th',.15),
        ('rn',.15), ('rk',.15), ('rt',.15), ('nt',.15), ('nk',.15), ('st',.15),
        ('ll',.02), ('ss',.02), ('tt',.02), ('mm',.01), ('ff',.01), ('pp',.01),
        ('rr',.01), ('nn',.01), ('cc',.01), ('dd',.01), ('ck',.05), ('th',.05),
        ]

    def rand(self):
        return weighted_rand(self.freq)

class End(object):
    freq = [ ('t',.25), ('n',.24), ('r',.23), ('s',.22), ('h',.23), ('d',.22),
        ('l',.20), ('c',.19), ('m',.18), ('w',.17), ('f',.16), ('p',.15),
        ('g',.14), ('b',.13), ('v',.12), ('k',.11), ('j',.10), ('x',.06),
        ('qu',.05), ('z',.10), ('th',.15),
        ('rn',.15), ('rk',.15), ('rt',.15), ('nt',.15), ('nk',.15), ('st',.15),
        ('nd',.10), ('rd',.10),
        ]

    def rand(self):
        return weighted_rand(self.freq)


if __name__ == '__main__':

    p = Prefix()
    v = Vowel()
    i = Inner()
    e = End()

    for _ in range(23):
        x =  int(random.uniform(0,77))

        # One syllable
        if between(x, 0, 5):
            print p.rand().capitalize() + v.rand() + e.rand()

        # leading vowel and a syllable
        elif between(x, 5, 9):
            print ( v.rand().capitalize() + p.rand() + v.rand() + e.rand() )

        # two syllables
        elif between(x,10,49):
            print ( p.rand().capitalize() + v.rand() + i.rand() + v.rand()
                + e.rand() )

        # leading vowell and two syllables
        elif between(x,50,69):
            print ( v.rand().capitalize() + p.rand() + v.rand() + i.rand()
                + v.rand() + i.rand() + v.rand() + e.rand() )

        # three syllables
        elif between(x,70,73):
            print ( p.rand().capitalize() + v.rand() + i.rand() + v.rand()
                + i.rand() + v.rand() + i.rand() + v.rand() + e.rand() )

        # leading vowell and three syllables
        elif between(x,74,76):
            print ( v.rand().capitalize() + p.rand() + v.rand() + i.rand()
                + v.rand() + i.rand() + v.rand() + i.rand() + v.rand()
                + e.rand() )
