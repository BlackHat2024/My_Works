from functools import *
# convert string to int value according to ASCII table 
def value(str):
    result  = reduce((lambda a ,b : a + b) , [ord(x) for x in list(str)])
    return result 




class Node:
    def __init__(self, key, index):
        self.left = None
        self.right = None
        self.val = key
        self.index= index
 

def insert(root, key, index):
    if root is None:
        return Node(key,index)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key ,index)
        else:
            root.left = insert(root.left, key, index)
    return root



def search(root,key):
     
    if root is None:
        return Node(key, -1)
     
    if root.val == key:
        return root
   
  

    if root.val < key:
        return search(root.right,key)
   
    return search(root.left,key)

 
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val , root.index)
        inorder(root.right)

def main():
    array = [value(x) for x in input().split()]

    Bts = Node(array[0], 0)
    for i in range(1, len(array)):
        insert(Bts , array[i], i)
    
    str1 = "Paul"
    Node1 = Bts 
    Node1 = search(Node1,value(str1))
    print("{0} index is {1}".format(str1, Node1.index))

if __name__== "__main__" :
    main()
