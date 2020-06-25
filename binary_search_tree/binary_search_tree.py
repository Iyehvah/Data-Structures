"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Take the current value of our node (self.value)
        # Compare to the new value we want to insert
        # if new value < self.value
        if value < self.value:
            # go left now since the value is less than the parent node.
            if not self.left:
                # IF self.left is already taken by a node
                self.left = BSTNode(value)
            # Make THAT NODE call the insert function.
            # Set the left to the new node with the new value
            else:
                self.left.insert(value)

        # if new value >= self.value *bigger or equal to our root node*
        else:
            if not self.right:
                #if self.right is already taken by a node
                self.right = BSTNode(value)
            # Set the right child to the new node with new value
            # Make THAT node call insert
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True

        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)

        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
    # Return the maximum value found in the tree
    def get_max(self):
        #if you cant go right anymore
        if not self.right:
            #return the last value
            return self.value
        #returning the last value and calling the getmax function.
        return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
