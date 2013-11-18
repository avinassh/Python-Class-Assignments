#!/usr/bin/python

import re

#Assumptions only one final state. Given an initial state
#State names are always specified in numbers
#
#
#
#



def lexicalAnalyzer():
	fn = open('input.txt', 'r')
	invalidCharacters = r'?!([a-zA-Z0-9]+)'
	for line in fn:
		if (line == '\n'):
			continue
		key = line.split()[0]
		if (key[0] == '#'):
			#print 'comments found'
			continue
		#print line	
		print re.match(invalidCharacters, line)
		#print bool(re.search(invalidCharacters, line))

def serializeInput():
	inputData = {} #is a dictionary and has all the important data
	listOfTransitions = []
	#inputData['transition'] = []
	fn = open('input.txt', 'r')
	for line in fn:
		if (line == '\n'):
			continue
		key = line.split()[0]
		if (key[0] == '#'):
			#print 'comments found'
			continue
		if (key == 'transition'):
			listOfTransitions.append(line.split()[2:])
		inputData[key] = line.split()[2:]
	inputData['transition'] = listOfTransitions	
	return inputData	
	#print listOfTransitions

		
#fo = open('input.txt', 'r')
#for line in fo:
	#print line.split()

class FiniteState:
    """Class for the finite states"""
    def __init__(self, name):
    	self.name = name
    	self.isItInitial = False
    	self.isItFinal = False
    	self.isDead = False
    	self.validTransitions = []
    	self.validInputs = []

    #def getStateName(self):
    #	return self.name	

    def initTransitions(self, inputString, nextState):
    	self.validTransitions.append((inputString, nextState))
    	self.validInputs.append(inputString)

    #def transition(self, inputString):
    #	for validTrans in self.validTransitions:
    #		if validTrans[0] == inputString:
    #			return validTrans[1]
    #	return 'DeadState:-('		


def FSM(): #the beaf
	inputData = serializeInput()
	listOfStatesObjects = [] 
	for stateName in inputData['states']:
		listOfStatesObjects.append(FiniteState(stateName))
	#print listOfStatesObjects
	#create a dead state :(
	listOfStatesObjects.append(FiniteState('dead'))
	listOfStatesObjects[-1].isDead = True	

	for state in listOfStatesObjects:
		for transition in inputData['transition']:
			if(state.name == transition[0]):
				state.initTransitions(transition[1], transition[2])

	#set initial and final states
	for state in listOfStatesObjects:
		#print state.name
		if (state.name == inputData['initial'][0]):
			state.isItInitial = True
			currentState = state

	for finalStateName in inputData['final']:		
		for state in listOfStatesObjects:
			if (state.name == finalStateName):
				state.isItFinal = True

	stringA = 'aaaaaaaaaabaccb'
	
	deadState = listOfStatesObjects[-1]

	for character in stringA:
		if(character not in currentState.validInputs):
			currentState = 	deadState
			print 'aww, dead'
			break

		for validTrans in currentState.validTransitions:
			if(validTrans[0] == character):
				for state in listOfStatesObjects:
					if(state.name == validTrans[1]):
						currentState = state

	if (currentState.isItFinal):
		print 'string accepted'
	else: 
		print 'string rejected'	

#FSM()
lexicalAnalyzer()