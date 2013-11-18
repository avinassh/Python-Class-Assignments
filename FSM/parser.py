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
    	self.isItInitial = False
    	self.isItFinal = False
    	self.name = name
    	self.validTransitions = []

    def getStateName(self):
    	return self.name	

    def initTransitions(self, inputString, nextState):
    	self.validTransitions.append((inputString, nextState))

    def transition(self, inputString):
    	for validTrans in self.validTransitions:
    		if validTrans[0] == inputString:
    			return validTrans[1]
    	return 'DeadState:-('		


def FSM(): #the beaf
	inputData = serializeInput()
	#print inputData
	listOfStatesObjects = [] 
	for stateName in inputData['states']:
		listOfStatesObjects.append(FiniteState(stateName))
	#print listOfStatesObjects

	for state in listOfStatesObjects:
		for transition in inputData['transition']:
			if(state.name == transition[0]):
				state.initTransitions(transition[1], transition[2])

	print listOfStatesObjects[0].transition('a')
	print listOfStatesObjects[0].transition('b')			

FSM()	

#for item in names:
#	state.append(FiniteState(item))

#state[0].initTransitions('a', '2')
#state[0].initTransitions('b', '3')



#initial = state[0]

#print state[0]
#print initial