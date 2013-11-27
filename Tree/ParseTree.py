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
        root.set_raw_subtrees(file_data, 1, -1) #highly unreadable
        root.set_node_val()
        root.set_node_parent() #I dont want data of this to be changed!
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
                root.set_node_val()
                # print 'before', root.raw_subtrees[1]
                # root.val = file_data[index+1]
                # print 'after', root.val
                #all_nodes.append((root.val, root))
            if char == "subtree:":
                child = Node()
                #all_nodes.append((child.val, child))
                start, end = get_subtree_data(file_data, index)
                #child.raw_subtrees = file_data[start:end]
                child.set_raw_subtrees(file_data, start, end)
                child.set_node_parent(root)
                root.add_subtree(child)
                #root.subtrees.append(child)  

    def _create_child_nodes(self, node):
        for subtree in node.subtrees:
            self._initialize_node(subtree)
            self._create_child_nodes(subtree) 


my_parse = ParseTreeDescription()
root1 = my_parse.Parse('tree_input.txt')
search_result = root1.find_nodes('"9"')
print search_result[0].parent.val

