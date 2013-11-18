#!/usr/bin/python

#Assumptions only one final state. Given an initial state
#State names are always specified in numbers
#
#
#
#

def lexicalAnalyzer():
	return None  #check all invalid keywords 

def serializeInput():
	inputData = {} #is a dictionary and has all the important data
	listOfTransitions = []
	#inputData['transition'] = []
	fn = open('input.txt', 'r')
	for line in fn:
		key = line.split()[0]
		if (key[0] == '#'):
			#print 'comments found'
			continue
		if (key == 'transition'):
			listOfTransitions.append(line.split()[2:])
		inputData[key] = line.split()[2:]
	inputData['transition'] = listOfTransitions	
	print inputData	
	#print listOfTransitions

serializeInput()			
#fo = open('input.txt', 'r')
#for line in fo:
	#print line.split()

class FiniteState:
    """Class for the finite states"""
    def __init__(self, name):
    	self.isItInitial = False
    	self.isItFinal = False
    	self.name = name
    	self.validTransitions = []

    def initTransitions(self, inputString, nextState):
    	self.validTransitions.append((inputString, nextState))

    def transition(self, inputString):
    	for validTrans in self.validTransitions:
    		if validTrans[0] == inputString:
    			return validTrans[1]
    	return 'DeadState:-('		


names = ['1','2','3','4']

state = []

#for item in names:
#	state.append(FiniteState(item))

#state[0].initTransitions('a', '2')
#state[0].initTransitions('b', '3')

#print state[0].transition('a')
#print state[0].transition('b')

#initial = state[0]

#print state[0]
#print initial