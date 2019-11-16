class HuffmanNode(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

def create_tree(frequencies):
    while len(frequencies) > 1:      # 2. While there is more than one node
                                     # 2a. remove two highest nodes
        l, r = find_two_lowest_feq(frequencies) 
        combi_freq = l[0] + r[0]
                                     # 2b. create internal node with children
        parent_node = HuffmanNode(l, r)
                                     # 2c. add new node to queue
        combi_freq_item = (combi_freq, parent_node)
        frequencies.append(combi_freq_item)
    return frequencies[0]            # 3. tree is complete - return root node

# find two lowest frequencies
# and REMOVE THEM FROM the list
# and combine them to a new freqency (also combine the letters)
def find_two_lowest_feq(frequency_list):
    first_lowest_feq = find_lowest_feq(frequency_list)
    frequency_list.remove(first_lowest_feq)
    second_lowest_feq = find_lowest_feq(frequency_list)
    frequency_list.remove(second_lowest_feq)
    
    return first_lowest_feq, second_lowest_feq

def find_lowest_feq(frequency_list):
    min_frequency = frequency_list[0]
    for frequency_item in frequency_list:
        if float(frequency_item[0]) < float(min_frequency[0]):
            min_frequency = frequency_item
    return min_frequency

# Recursively walk the tree down to the leaves,
# assigning a code value to each symbol
def walk_tree(node, prefix="", code={}):
    node_or_leaf = node[1].left[1]
    if isinstance(node_or_leaf, HuffmanNode):
        left_node = node[1].left
        walk_tree(left_node, prefix+"0", code)
    else:
        left_leaf = node_or_leaf
        code[left_leaf]=prefix+"0"

    node_or_leaf = node[1].right[1]
    if isinstance(node_or_leaf,HuffmanNode):
        right_node = node[1].right
        walk_tree(node[1].right,prefix+"1", code)
    else:
        right_leaf = node_or_leaf 
        code[right_leaf]=prefix+"1"
    return(code)

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
    
    code = walk_tree(root_node)

    for item in sorted(code.keys()):
        print (item, code[item])
