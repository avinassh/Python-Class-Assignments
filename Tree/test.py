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

def braces_validation(): #this function works on whole input file considering it as a string
    stack = Stack()
    for char in file_content:
        start = start + 1
        if char == '{':
            stack.push('{')
        elif char == '}':
            stack.pop()
            if stack.isEmpty(): #and file_content.index(char)+1 < len(file_content):
                return True

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

#print file_data
#start, end = get_subtree_data(file_data)
#print file_data[start : end]

#root = node()
##root.val = '1'
#root.subtrees_raw_data = file_data[start : end]
#print root.subtrees_raw_data

def create_child_nodes(root):  ## add two stacks, one to validate braces and one to keep raw_data saved
    file_data = root.raw_subtrees
    end  = 0
    #print file_data, '\n'
    for index, char in enumerate(file_data):
        if index < end:
            #print 'here1', index
            continue  
        if char == "val:":
            root.val = file_data[index+1]
            all_nodes.append((root.val, root))
        if char == "subtree:":
            child = node()
            #all_nodes.append((child.val, child))
            start, end = get_subtree_data(file_data, index)
            child.raw_subtrees = file_data[start:end]
            child.parent = root
            root.subtrees.append(child)  

#for child in root1.subtrees:
#    print child.raw_subtrees

#for child in root1.subtrees:
#    create_child_nodes(child, child.raw_subtrees)

#print root1.subtrees[1].subtrees[0].raw_subtrees
#print root1.subtrees[1].subtrees[1].raw_subtrees

fn = open('tree_input.txt', 'r')
full_file = fn.read()
fn.close()

file_data = full_file.split()

all_nodes = []

root1 = node()
#root1.val = '1'
#all_nodes.append((root1.val,root1))
root1.raw_subtrees = file_data[1:-1] #highly unreadable
root1.val = root1.raw_subtrees[1]
root1.parent = None #I dont want data of this to be changed!
create_child_nodes(root1)

def temp_function(node):
    for child in node.subtrees:
        create_child_nodes(child)
        temp_function(child)

def temp_search(node, key):
    if node.val == key:
        print 'found', node
        return node     
    for subtree in node.subtrees:         
        temp = temp_search(subtree, key)
        if temp:
            return temp

def temp_multi_search(some_node, key):
    result = []
    if some_node.val == key:
        return [some_node]
    for subtree in some_node.subtrees:         
        temp = temp_multi_search(subtree, key)
        if temp:
            result.extend(temp)
    return result

def temp_add_node(node, parent_node_id):
    pass

def temp_child_nodes(node, value):
    pass    

#for child in root1.subtrees:
#    tree_build(child, child.raw_subtrees)

#for child in root1.subtrees[0].subtrees:
#    tree_build(child, child.raw_subtrees)    

temp_function(root1)
#print root1.val == '"1",'
#search_result = temp_search_1(root1, '"14"')
#print search_result

search_result = temp_multi_search(root1, '"9"')
print search_result

# print root1.subtrees[0].subtrees[0].subtrees[0].raw_subtrees
# print root1.subtrees[0].subtrees[0].raw_subtrees

# print root1.subtrees[0].subtrees[0].val
# print root1.subtrees[0].subtrees[0].subtrees[0].val

#----------------------------------------------
# REPL : checking nodes can access parent
#----------------------------------------------

# print root1.subtrees[0].subtrees[0].val #the 
# print root1.subtrees[0].subtrees[0].parent.val
# print root1.subtrees[0].subtrees[0].parent.parent.val
# print root1.subtrees[0].subtrees[0].parent.parent.parent

#----------------------------------------------
# REPL : List of subtrees of a node [as lits of objects]
#----------------------------------------------
# print root1.subtrees

# print root1.subtrees[0].subtrees
# print root1.subtrees[1].subtrees
# print root1.subtrees[2].subtrees
# print root1.subtrees[3].subtrees
# print root1.subtrees[4].subtrees

# print root1.subtrees[0].subtrees[0].subtrees

# print root1.subtrees[1].subtrees[0].subtrees
# print root1.subtrees[1].subtrees[1].subtrees


#----------------------------------------------
# REPL : raw subtree data of a node
#----------------------------------------------
# print root1.raw_subtrees

# print root1.subtrees[0].raw_subtrees
# print root1.subtrees[1].raw_subtrees
# print root1.subtrees[2].raw_subtrees
# print root1.subtrees[3].raw_subtrees
# print root1.subtrees[4].raw_subtrees

# print root1.subtrees[0].subtrees[0].raw_subtrees

# print root1.subtrees[1].subtrees[0].raw_subtrees
# print root1.subtrees[1].subtrees[1].raw_subtrees


#----------------------------------------------
# REPL : value of a node
#----------------------------------------------

# print root1.val
# print root1.subtrees[0].val
# print root1.subtrees[1].val
# print root1.subtrees[2].val
# print root1.subtrees[3].val
# print root1.subtrees[4].val

# print root1.subtrees[0].subtrees[0].val

# print root1.subtrees[1].subtrees[0].val
# print root1.subtrees[1].subtrees[1].val

# print root1.subtrees[2].subtrees[0].val
# print root1.subtrees[2].subtrees[1].val