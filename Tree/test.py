import json

#http://www.greenteapress.com/thinkpython/thinkCSpy/html/chap18.html
class Stack(object) : 
  def __init__(self) : 
    self.items = [] 

  def push(self, item) : 
    self.items.append(item) 

  def pop(self) : 
    return self.items.pop() 

  def isEmpty(self) : 
    return (self.items == [])

  def getStack(self) :
    return self.items

fn = open('tree_input.txt', 'r')
full_file = fn.read()
fn.close()

def check_braces(start): #this function works on whole input file considering it as a string
    stack = Stack()
    full = full_file[start:]
    print start
    for char in full:
        start = start + 1
        if char == '{':
            stack.push('{')
        elif char == '}':
            stack.pop()
            if stack.isEmpty():
                return start

def get_subtree_data_test(file_data):
    "Returns the subtree data"
    print 'first line'
    stack = Stack()
    for index, char in enumerate(file_data):
        #print index, char
        if char == '{': #the subtree is started
            stack.push('{')
            print stack.getStack()
            #start = index
        if char == '}':
            stack.pop()
            #print index
            print stack.getStack()
            if stack.isEmpty(): #damn! took so many minutes debug this
                print stack.isEmpty()
                print index
                end = index
                print type(start)
                print type(end)
                return (start, end)

def get_subtree_data(file_data):
    "Returns the subtree data"
    print 'first line'
    stack = Stack()
    for char in file_data:
        #print index, char
        if char == '{': #the subtree is started
            stack.push('{')
            print stack.getStack()
            #start = index
        if char == '}':
            stack.pop()
            #print index
            print stack.getStack()
            if stack.isEmpty(): #damn! took so many minutes debug this
                return 'braces are valid'
                print stack.isEmpty()
                #print index
                #end = index
                #print type(start)
                #print type(end)
                #return (start, end)
    return 'braces are invalid'                            

#print full_file[ full_file.find('subtree')+len('subtree') : check_braces(full_file.find('val'))]

class node(object):
  """docstring for node"""
  def __init__(self, val=''):
    #super(node, self).__init__()
    self.val = val #value of the node
    self.subtrees = [] #list of objects
    self.parent = None #[parent object]

file_data = full_file.split()

print file_data
#start, end = 
#print get_subtree_data(file_data)

#print file_data[start : end]