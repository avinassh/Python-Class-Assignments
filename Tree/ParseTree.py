import re

from Tree import *

class ParseTreeDescription:
    def __init__(self):
        pass

    def Parse(self, filename):
        """ Returns a Tree object after parsing the file """
        fn = open(filename, 'r')
        file_data = fn.read().split()
        #file_data = full_file.split()
        
        fn.close()

        file_data = self._sanitize(file_data)
        #print file_data
        
        root = Node()
        root.set_raw_subtrees(file_data, 1, -1) #highly unreadable
        root.set_node_val()
        root.set_node_parent() #I dont want data of this to be changed!
        self._initialize_node(root)  
        self._create_child_nodes(root)
        return root

    def _initialize_node(self, root):  ## add two stacks, one to validate braces and one to keep raw_data saved
        """ Initiliazes the node, sets its value, its parent and also adds subtree data """
        file_data = root.raw_subtrees
        end  = 0
        #print file_data, '\n'
        for index, char in enumerate(file_data):
            if index < end:
                #print 'here1', index
                continue  
            if char == "val":
                root.set_node_val()
                #all_nodes.append((root.val, root))
            if char == "subtree":
                child = Node()
                #all_nodes.append((child.val, child))
                start, end = get_subtree_data(file_data, index)
                child.set_raw_subtrees(file_data, start, end)
                child.set_node_parent(root)
                root.add_subtree(child) 

    def _create_child_nodes(self, node):
        """ This is used to recursivley work on subtrees and initialize them by calling _initialize_node """
        for subtree in node.subtrees:
            self._initialize_node(subtree)
            self._create_child_nodes(subtree)

    def _sanitize(self, unsanitized_data):
        """ Takes unsanitized and sanitizes it. Removes special characters etc."""
        invalid_characters = r'[:,"]'
        for index, char in enumerate(unsanitized_data):
            if char == '{' or char == '}':
                continue
            elif char == '},':
                unsanitized_data[index] = '}'   
            elif char == 'val:':
                unsanitized_data[index] = 'val'
            elif char == 'subtree:':
                unsanitized_data[index] = 'subtree'
            else:
                unsanitized_data[index] = re.sub(invalid_characters, '', char)

        return unsanitized_data            


my_parse = ParseTreeDescription()
Tree = my_parse.Parse('tree_input.txt')