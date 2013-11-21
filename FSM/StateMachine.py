#!/usr/bin/python

# incomplete code
#


import re
import sys
import os
import logging
from exceptions import Exception

class DuplicateStateException(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg)

class InvalidStateException(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg)

class NonExistentStateException(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg)

def lexicalAnalyzer():
    fn = open('input.txt', 'r')
    invalidCharacters = r'[^a-zA-Z0-9: \n]+'
    i = 1
    for line in fn:
        i = i + 1
        if (line == '\n'):
            continue
        key = line.split()[0]
        if (key[0] == '#'):
            continue
        #print line 
        if(bool(re.search(invalidCharacters, line))):
            logging.error('syntax error at line',i)
            break
    fn.close


def parser():
    keywords = ['states', 'alphabet', 'initial', 'final', 'transition']
    inputData = {}
    fn = open('input.txt', 'r')
    i = 1
    for line in fn:
        i = i + 1
        if (line == '\n'):
            continue
        key = line.split()[0]
        if (key[0] == '#'):
            continue
        #print line
        if(line.split()[0] not in keywords):
            print 'invalid keyword found at line', i
            break   
        if(line.split()[0] == 'states'):
            inputData['states'] = line.split()[2:]
        if(line.split()[0] == 'alphabet'):
            inputData['alphabet'] = line.split()[2:]

        if(line.split()[0] == 'initial'):
            if (len(line.split()) != 3):
                logging.error('One and only initial state should be present')
                break
            elif (line.split()[2] not in inputData['states']):
                print 'Invalid initial state'
                break

        if(line.split()[0] == 'final'):
            for finalStateName in line.split()[2:]:
                if (finalStateName not in inputData['states']):
                    print 'Invalid final state specified'
                    break

        if(line.split):
            pass                      

        if(line.split()[1] != ':'):
            logging.error('invalid keyword found at line', i)
            break   
    fn.close        


def serializeInput():
    inputData = {} #is a dictionary and has all the important data
    listOfTransitions = []
    fn = open('input.txt', 'r')
    for line in fn:
        if (line == '\n'):
            continue
        key = line.split()[0]
        if (key[0] == '#'): #starting with '#' are comments, ignore
            continue
        if (key == 'transition'):
            listOfTransitions.append(line.split()[2:])
        inputData[key] = line.split()[2:]
    inputData['transition'] = listOfTransitions
    #print inputData    
    return inputData

class StateMachine(object):
    """ This is the StateMachine """
    meta = { 'author' : 'avinash', 
            'version' : '0.1', 
            'date' : '21-Nov-2013' }

    def __init__(self, state_machine_spec = 'input.txt', name = 'MyStateMachine'):
        #read state machine spec and initialize here
        self.name = name
        self.initial_state = None
        self.final_states = []
        self.transitions = {}
        self.alphabet = []
        self.states = []
        self.dead_state = None

    # def is_invalid_statename(self, statename):
    #     invalid_state_name_regex = r'^[a-zA-Z0-9]'
    #     return bool(re.search(invalid_state_name_regex, statename))

    # def cleanse_state_name(self, statename):
    #     if type(statename) != str:
    #         statename = str(statename)
    #     statename = statename.strip()
    #     return statename

    def add_state(self, statename):
        invalid_state_name_regex = r'^[a-zA-Z0-9]'
        if type(statename) != str:
            statename = str(statename)        
        statename = statename.strip()
        if not bool(re.search(invalid_state_name_regex, statename)):
            raise InvalidStateException("Invalid state name")
            #print 'InvalidStateException'
        if statename in self.states:
            raise DuplicateStateException("State already exists")
            #print 'DuplicateStateException'
        self.states.append(statename)

    def add_states(self, *statenames):
        for statename in statenames:
            self.add_state(statename)

    def set_initial_state(self, statename):
        invalid_state_name_regex = r'^[a-zA-Z0-9]'
        if type(statename) != str:
            statename = str(statename)        
        statename = statename.strip()
        if not bool(re.search(invalid_state_name_regex, statename)):
            raise InvalidStateException("Invalid state name")
        if self.initial_state is None:
            self.initial_state = statename
            return 
        #return False    



def FSM(inputString): #the beef
    inputData = serializeInput()
    listOfStatesObjects = [] 
    for stateName in inputData['states']:
        listOfStatesObjects.append(FiniteState(stateName))
    #create a dead state :(
    listOfStatesObjects.append(FiniteState('dead'))
    listOfStatesObjects[-1].isDead = True   

    for state in listOfStatesObjects:
        for transition in inputData['transition']:
            if(state.name == transition[0]):
                state.initTransitions(transition[1], transition[2])

    #set initial and final states
    for state in listOfStatesObjects:
        if (state.name == inputData['initial'][0]):
            state.isItInitial = True
            currentState = state

    for finalStateName in inputData['final']:       
        for state in listOfStatesObjects:
            if (state.name == finalStateName):
                state.isItFinal = True
    
    deadState = listOfStatesObjects[-1]

    for character in inputString:
        if(character not in currentState.validInputs):
            currentState =  deadState
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
#lexicalAnalyzer()

#if (len(sys.argv) < 2):
#   print 'no input string given'
#   sys.exit()
#else:
#   FSM(sys.argv[1])

parser()