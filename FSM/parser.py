#!/usr/bin/python

fo = open('input.txt', 'r')
#for line in fo:
	#print line.split()

class FiniteState:
    """Class for the finite states"""
    def __init__(self, name):
    	self.isItInitial = False
    	self.isItFinal = False
    	self.name = name

names = ['1','2','3','4']

state = []

for item in names:
	state.append(FiniteState(item))

print state[0].name	