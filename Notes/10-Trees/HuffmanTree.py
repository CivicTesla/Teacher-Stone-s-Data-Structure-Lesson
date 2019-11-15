import re
class HuffmanNode(object):
    def __init__(self, left=None, right=None, parent=None, char=None, visited=False):
        self.left = left
        self.right = right
        self.parent = parent
        self.char = char
        self.visited = visited
    def link_children(self, left=None, right=None):
        self.left = left
        self.right = right
    def children(self):
        return((self.left, self.right))
    def toString(self):
        print ("left node:", self.left)
        print ("right node:", self.right)

def create_tree(frequencies):
    while len(frequencies) > 1:           # 2. While there is more than one node
                                          # 2a. remove two highest nodes
        l, r = find_two_highest_feq(frequencies) 
        combi_freq = l[0]+r[0]
        left_leaf_char = l[1]
        right_leaf_char = r[1]

                                          # 2b. create internal node with children
        parent_node = HuffmanNode()
        left_child = HuffmanNode(None, None, parent_node, left_leaf_char)
        right_child = HuffmanNode(None, None, parent_node, right_leaf_char)
        parent_node.link_children(left_child, right_child)
    return parent_node                    # 3. tree is complete - return root node

# find two highest frequencies
# and REMOVE THEM FROM the list
# and combine them to a new freqency
def find_two_highest_feq(frequency_list):
    first_highest_feq = find_highest_feq(frequency_list)
    frequency_list.remove(first_highest_feq)
    second_highest_feq = find_highest_feq(frequency_list)
    frequency_list.remove(second_highest_feq)
    
    frequency_list.append((first_highest_feq[0]+second_highest_feq[0], None))
    
    return first_highest_feq, second_highest_feq

def find_highest_feq(frequency_list):
    max_frequency = frequency_list[0]
    for frequency_item in frequency_list:
        if frequency_item[0] > max_frequency[0]:
            max_frequency = frequency_item
    return max_frequency

# go through the tree
# return a coding table
def walk_tree(node, coding_stack, coding_table):
    node_is_leaf = is_leaf(node)
    if node_is_leaf or both_children_visited(node):
        if node_is_leaf:
            coding = stack2coding(coding_stack)
            coding_table[coding]=node.char
        node.visited = True
        if len(coding_stack)==0:
            return coding_table
        else:
            walk_tree(node.parent, coding_stack, coding_table)
    elif node!=None: # PROBLEM HERE
        # if the node is a node in the tree (not the bottom leaves, not the top root,
        #                       not None either (a leave may have a None left and a None right))
        if (not node.left.visited):
            coding_stack.append(0)
            walk_tree(node.left, coding_stack, coding_table)
        if (not node.right.visited):
            coding_stack.append(1)
            walk_tree(node.right, coding_stack, coding_table)
# PROMBLEM HERE: AttributeError: 'NoneType' object has no attribute 'left'
# determine whether a node is a leaf
def is_leaf(node):
    if node == None:
        return False
    if node.left == None and node.right == None:
        return True
    return False

# determine if all children of a node are visited
def both_children_visited(node):
    left_visited = False
    right_visited = False
    if node.left !=None:
        if node.left.visited:
            left_visited = True
    if node.right !=None:
        if node.right.visited:
            right_visited = True

    return left_visited and right_visited

# read the queue from left to right as coding
def stack2coding(stack):
    coding = ""
    for item in stack:
        coding+=str(item)
    return coding

if __name__ == '__main__':
    freq = [
    (8.167, 'a'), (1.492, 'b'), (2.782, 'c'), (4.253, 'd'),
    (12.702, 'e'),(2.228, 'f'), (2.015, 'g'), (6.094, 'h'),
    (6.966, 'i'), (0.153, 'j'), (0.747, 'k'), (4.025, 'l'),
    (2.406, 'm'), (6.749, 'n'), (7.507, 'o'), (1.929, 'p'), 
    (0.095, 'q'), (5.987, 'r'), (6.327, 's'), (9.056, 't'), 
    (2.758, 'u'), (1.037, 'v'), (2.365, 'w'), (0.150, 'x'),
    (1.974, 'y'), (0.074, 'z') ]

    root_node = create_tree(freq)
    
    coding_table = walk_tree(root_node, [], {})

    print(coding_table)
