#!/usr/bin/python2

from PSXTree import PSXCore


core = PSXCore()
core.load('examples/test1.psx')
core.load('examples/test2.zip')
core.load('examples/test3.tar')
core.load('examples/test.csv')
