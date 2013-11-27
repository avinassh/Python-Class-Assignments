from Tree import *

class ParseTreeDescription:
    def __init__(self):
        pass

    def Parse(self, filename):
        """ Returns a Tree object after parsing the file """
        fn = open(filename, 'r')
        full_file = fn.read()
        fn.close()
        file_data = full_file.split()

        root = Node()
        root.raw_subtrees = file_data[1:-1] #highly unreadable
        root.val = root.raw_subtrees[1]
        root.parent = None #I dont want data of this to be changed!
        self._initialize_node(root)  
        self._create_child_nodes(root)
        return root

    def _initialize_node(self, root):  ## add two stacks, one to validate braces and one to keep raw_data saved
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

    def _create_child_nodes(self, node):
        for subtree in node.subtrees:
            self._initialize_node(subtree)
            self._create_child_nodes(subtree) 


my_parse = ParseTreeDescription()
root1 = my_parse.Parse('tree_input.txt')
search_result = root1.find_nodes('"9"')
print root1.subtrees[0]                