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

def get_subtree_data(file_data, starter):
    "Returns the subtree data"
    #print 'first line'
    stack = Stack()
    start = None
    for index, char in enumerate(file_data):    
        #print index, char
        if index < starter:
            continue
        if char == '{': #the subtree is started
            stack.push('{')
            if bool(not start):
                start = index + 1
        if char == '}' or char == '},':
            stack.pop()
            if stack.isEmpty(): #damn! took so many minutes debug this
                end = index
                return (start, end)                            

class node(object):
  """docstring for node"""
  def __init__(self, val=''):
    #super(node, self).__init__()
    self.val = val #value of the node
    self.subtrees = [] #list of objects
    self.raw_subtrees = []
    self.parent = None #[parent object]

file_data = full_file.split()
#print file_data
#start, end = get_subtree_data(file_data)
#print file_data[start : end]

#root = node()
##root.val = '1'
#root.subtrees_raw_data = file_data[start : end]
#print root.subtrees_raw_data

root1 = node()

def create_child_nodes(root, file_data):
    end  = 0
    for index, char in enumerate(file_data):
        if index < end:
            continue  
        if char == "val:":
            root.val = file_data[index+1]
        if char == "subtree:":
            child = node()
            start, end = get_subtree_data(file_data, index)
            child.raw_subtrees = file_data[start:end]
            root.subtrees.append(child)  


create_child_nodes(root1, file_data)

for child in root1.subtrees:
    print child.raw_subtrees

for child in root1.subtrees:
    create_child_nodes(child, child.raw_subtrees)

#print root1.subtrees[1].subtrees[0].raw_subtrees
#print root1.subtrees[1].subtrees[1].raw_subtrees