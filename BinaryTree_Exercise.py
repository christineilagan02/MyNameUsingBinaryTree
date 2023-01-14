# Binary Tree 
# src: https://youtu.be/lFq5mYUWEBk

import sys

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
  
# list off numbers and letters
if __name__ == '__main__':
    
    def menu():
        print("\t\33[1m\33[33m*\33[0m---+---+--\33[1m\33[33mMENU\33[0m--+---+---\33[1m\33[33m*\33[0m")
        menu_list = ["\n\t \33[3m\33[1m 1 -> Numbers \33[0m", "\t \33[3m\33[1m 2 -> Letters \33[0m", "\t \33[3m\33[1m 7 -> Exit \33[0m\n"]
        for item in menu_list:
            print(item)
        print("\t\33[1m\33[33m*\33[0m---+---+---\33[1m\33[33m*\33[0m---+---+---\33[1m\33[33m*\33[0m")
            
    def start():
        while True:
            choice = input("\n\t\33[92mEnter your choice[1-3]\33[0m \n\t>> ")
            if choice == '1':
                numbers = [17, 4 , 1, 20, 9, 23, 18, 34, 18, 4]
                numbers_tree = build_tree(numbers)
                
                print("\n\t\33[1m\33[33m*\33[0m---+---+---\33[1m\33[33m*\33[0m---+---+---\33[1m\33[33m*\33[0m")
                print("\t\t\33[1m Numbers \33[0m")
                print("\t\33[1m\33[33m*\33[0m---+---+---\33[1m\33[33m*\33[0m---+---+---\33[1m\33[33m*\33[0m")
                
                search_numbers = int(input("\n\t\33[1mSearch: \33[0m"))
                print("\n\t\33[1m\33[33m*\33[0m---+---+---\33[1m\33[33m*\33[0m---+---+---\33[1m\33[33m*\33[0m")
                
                print(f"\n\t\33[1mIs {search_numbers} included in the list \n\t>> \33[0m", numbers_tree.search(search_numbers))
                print("\t\33[92m=========================\33[0m")
                print("\t\33[1mMinimum: \33[0m",numbers_tree.find_min())
                print("\t\33[92m=========================\33[0m")
                print("\t\33[1mMaximum: \33[0m",numbers_tree.find_max())
                print("\t\33[92m=========================\33[0m")
                print("\t\33[1mCalculate Sum: \33[0m", numbers_tree.calculate_sum())
                print("\t\33[92m=========================\33[0m")
                print("\t\33[1mIn order traversal \n\t>> \33[0m", numbers_tree.in_order_traversal())
                print("\t\33[92m=========================\33[0m")
                print("\t\33[1mPre order traversal \n\t>> \33[0m", numbers_tree.pre_order_traversal())
                print("\t\33[92m=========================\33[0m")
                print("\t\33[1mPost order traversal \n\t>> \33[0m", numbers_tree.post_order_traversal())
                print("\t\33[92m=========================\33[0m")
                
            elif choice == '2':
                myName = ["C", "H", "R", "I", "S", "T", "I", "N", "E", "S", "A", "L", "V", "A", "N", "T", "E", "I", "L", "A", "G", "A", "N"]
                myName_tree = build_tree(myName)
                
                print("\n\t\33[1m\33[33m*\33[0m---+---+---\33[1m\33[33m*\33[0m---+---+---\33[1m\33[33m*\33[0m")
                print("\t\t\33[1m Letters \33[0m")
                print("\t\33[1m\33[33m*\33[0m---+---+---\33[1m\33[33m*\33[0m---+---+---\33[1m\33[33m*\33[0m")
                
                search_letters = input("\n\t\33[1mSearch (UPPERCASE ONLY): \n\t>> \33[0m")
                print("\n\t\33[1m\33[33m*\33[0m---+---+---\33[1m\33[33m*\33[0m---+---+---\33[1m\33[33m*\33[0m")
                print(f"\n\t\33[1mIs {search_letters} included in the list \n\t>> \33[0m", myName_tree.search(search_letters))
                print("\t\33[92m=========================\33[0m")
                print("\t\33[1mMinimum: \33[0m",myName_tree.find_min())
                print("\t\33[92m=========================\33[0m")
                print("\t\33[1mMaximum: \33[0m",myName_tree.find_max())
                print("\t\33[92m=========================\33[0m")
                print("\t\33[1mIn order traversal \n\t>> \33[0m", myName_tree.in_order_traversal())
                print("\t\33[92m=========================\33[0m")
                print("\t\33[1mPre order traversal \n\t>> \33[0m", myName_tree.pre_order_traversal())
                print("\t\33[92m=========================\33[0m")
                print("\t\33[1mPost order traversal \n\t>> \33[0m", myName_tree.post_order_traversal())
                print("\t\33[92m=========================\33[0m")
    
            elif choice == '3':
                print("\n")
                print("\t\33[1m\33[33m*\33[0m---+---+---\33[1m\33[33m*\33[0m---+---+---\33[1m\33[33m*\33[0m")
                print ("\t\33[1m\33[93m\33[3m   You can now exit.\33[0m")
                print("\t\33[1m\33[33m*\33[0m---+---+---\33[1m\33[33m*\33[0m---+---+---\33[1m\33[33m*\33[0m")
                sys.exit("\n")
            
            else:
                print("\t\33[1m\33[33m*\33[0m---+---+---\33[1m\33[33m*\33[0m---+---+---\33[1m\33[33m*\33[0m")
                print("\33[31m\33[1m\tError! Invalid input.\33[0m")
                print("\33[31m\33[1m\tPlease try again...\33[0m")
                print("\t\33[1m\33[33m*\33[0m---+---+---\33[1m\33[33m*\33[0m---+---+---\33[1m\33[33m*\33[0m")
    def main():
        menu()
        start()       
                
main()