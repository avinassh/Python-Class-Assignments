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

def check_braces(start):
    stack = Stack()
    full = full_file[start:]
    print start
    for char in full:
        start = start + 1
        if char == '{':
            stack.push('{')
        elif char == '}':
            stack.pop()
            if stack.isEmpty:
                return start

#print full_file[ full_file.find('subtree')+len('subtree') : check_braces(full_file.find('val'))]

class node(object):
  """docstring for node"""
  def __init__(self, val=''):
    #super(node, self).__init__()
    self.val = val #value of the node
    self.subtrees = [] #list of objects
    self.parent = None