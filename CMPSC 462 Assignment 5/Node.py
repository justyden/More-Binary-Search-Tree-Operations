# A node class that functions as the links for the binary tree class.

class Node:
    def __init__(self, inputNumber, inputNode1=None, inputNode2=None):
        self.number = inputNumber
        self.child1 = inputNode1
        self.child2 = inputNode2
