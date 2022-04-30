class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
  
 

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root



def searchRoot(root,key):
    
    if (root.left is not None and root.left.val == key) or (root.right is not None and root.right.val == key):
        return root.val

  
    if root.val == key :
        return root.val 

    if root is None:
        return None
    
    
    if root.val < key:
        return searchRoot(root.right,key)
    return searchRoot(root.left,key)

 
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val , root.index)
        inorder(root.right)


def main():
    array = [int(x) for x in input().split()]

    Bts = Node(array[0])
    for i in range(1, len(array)):
        insert(Bts , array[i])

    root_value = searchRoot(Bts,array[len(array)-1])
    
    print("Root value of {0} is {1}".format(array[len(array)-1],root_value))


if __name__== "__main__" :
    main()



""" 
    if we take as input these values
   
    3 6 12 7 45 32 9 55 43

    the formed BTS is:

        3
         \
          6
           \
            12
            / \
           7   45
              / \
            32   55
             \
              43

    So the root of last number 43 is 32
"""
