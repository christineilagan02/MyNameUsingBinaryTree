# Binary Tree 
# src: https://youtu.be/lFq5mYUWEBk

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    # Checking the value 
    def add_child(self, data):
        if data == self.data:
            return
        
        if data < self.data:
            # add data in left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            # add data in right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
                
    # Implementing in order traversal method
    def in_order_traversal(self):
        elements = []
        
        # visit the left tree
        if self.left:
            elements += self.left.in_order_traversal()
            
        # visit the base node
        elements.append(self.data)
        
        # visit the right tree
        if self.right:
            elements += self.right.in_order_traversal()
        
        return elements
    
    # performs post order traversal of a binary tree
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements
    
    # perofrms pre order traversal of a binary tree
    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements
    
    # searching method
    def search(self, val):
        if self.data == val:
            return True
        
        if val < self.data:
            # val might be in left subtree
            if self.left:
                return self.left.search(val)
            else:
                return False
            
        if val > self.data:
            # val might be in right subtree
            if self.right:
                return self.right.search(val)
            else:
                return False
            
    # finds minimum element in entire binary tree
    def find_min(self):
        if self.left == None:
            return self.data
        return self.left.find_min()
    
    # finds maximum element in entire binary tree
    def find_max(self):
        if self.right == None:
            return self.data
        return self.right.find_max()
    
    # calcualtes sum of all elements
    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum
    
# build tree
def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    
    for i in range(1, len(elements)):
        root.add_child(elements[i])
        
    return root
  
# list off numbers 
if __name__ == '__main__':
    numbers = [17, 4 , 1, 20, 9, 23, 18, 34, 18, 4]
    numbers_tree = build_tree(numbers)
    
    print("Search:", numbers_tree.search(21))
    print("Minimum:",numbers_tree.find_min())
    print("Maximum:",numbers_tree.find_max())
    print("Calculate Sum:", numbers_tree.calculate_sum())
    print("In order traversal:", numbers_tree.in_order_traversal())
    print("Pre order traversal:", numbers_tree.pre_order_traversal())
    print("Post order traversal:", numbers_tree.post_order_traversal())
    