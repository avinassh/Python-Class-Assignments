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

class Node(object):
    """docstring for node"""
    def __init__(self, val=''):
        self.val = val #value of the node
        self.subtrees = [] #list of objects
        self.raw_subtrees = []
        self.parent = None #[parent object]

    def initialize_node(root):  ## add two stacks, one to validate braces and one to keep raw_data saved
        file_data = root.raw_subtrees
        end  = 0
        #print file_data, '\n'
        for index, char in enumerate(file_data):
            if index < end:
                #print 'here1', index
                continue  
            if char == "val:":
                root.val = file_data[index+1]
                #all_nodes.append((root.val, root))
            if char == "subtree:":
                child = Node()
                #all_nodes.append((child.val, child))
                start, end = get_subtree_data(file_data, index)
                child.raw_subtrees = file_data[start:end]
                child.parent = root
                root.subtrees.append(child)  

    def create_child_nodes(node):
        for subtree in node.subtrees:
            subtree.initialize_node()
            subtree.create_child_nodes()            

    def find_nodes(some_node, key):
        result = []
        if some_node.val == key:
            return [some_node]
        for subtree in some_node.subtrees:         
            temp = subtree.find_nodes(key)
            if temp:
                result.extend(temp)
        return result

    def delete_node(self, value):
        """ deletes entire sub-tree """
        pass

    def add_node(self, value, parent_node_ID):
        pass    

    def add_node(node, parent_node_id):
        pass

    def child_nodes(node, value):
        pass                          

fn = open('tree_input.txt', 'r')
full_file = fn.read()
fn.close()

file_data = full_file.split()

all_nodes = []

root1 = Node()
#root1.val = '1'
#all_nodes.append((root1.val,root1))
root1.raw_subtrees = file_data[1:-1] #highly unreadable
root1.val = root1.raw_subtrees[1]
root1.parent = None #I dont want data of this to be changed!
root1.initialize_node()  
root1.create_child_nodes()
 
#print root1.val == '"1",'
#search_result = temp_search_1(root1, '"14"')
#print search_result

search_result = root1.find_nodes('"9"')
print search_result
print root1.subtrees[0]

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