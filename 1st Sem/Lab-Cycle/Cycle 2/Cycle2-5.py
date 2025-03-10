# Question 11: Binary search tree
from traversal import inorder, preorder, postorder
from BST_operations import insert, search, delete

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


#Driver code 
if __name__ == '__main__':

  r = Node(None)

  while True:
    print(
        """
Enter any of the number below to perform following operations

1. Insertion
2. Deletion
3. Search a node
4. Traversal
5. Exit 
  """
    )
    choice = int(input("=> "))

    if choice:
      if choice == 1:
          print("Insertion", end="\n\n")
          
          while True:
              nodeValue = int(input("Enter the node to be inserted => "))
              insert(r, nodeValue, Node)
              print(
                  "\n Enter :",
                  "X = to Stop insertion",
                  "Enter key to continue",
                  sep="  ",
                  end="\n\n",
              )
              stop = input()
              if stop == "X" or stop == "x":
                  break
          input("Press enter to continue")

      elif choice == 2:
        print("Deletion", end='\n\n')
        nodeValue = int(input("Enter the element to be deleted : "))
        
        if search(r, nodeValue, Node):  
          delete(r, nodeValue, Node)
          print("\nSpecified element has been deleted")
        else :
           print("\nSpecified element is not in the given tree")
        
        input("\nPress enter to continue")

      elif choice == 3:
        print("Search a node", end='\n\n')
        key = int(input("Enter the element to be searched : "))

        if search(r, key, Node):
          print("\nElement found in the given tree")
        else:
          print("\nElement not found in the given tree")
        
        input("\nPress enter to continue")

      elif choice == 4:
        print("Traversal", end="\n\n")
        print(
          "Enter the number given below to perform corresponding traversal",
          "1. Inorder",
          "2. Pre-Order",
          "3. Post-Order",
          sep= "\n", end="\n\n"
        )
        opted = int(input("=>"))

        if opted == 1:
          print("Inorder traversal \n")
          inorder(r)


        elif opted == 2:
          print("Pre-order traversal \n")
          preorder(r)

        elif opted == 3:
          print("Post-order traversal \n")
          postorder(r)

        else :
          print("Invalid Input\n")
          print("Try again")

        input("\nPress enter to continue")      

      elif choice == 5:
        print("Exiting")
        break
    
      else:
        print("\nInvalid entry try again..")
        input("\npress enter to continue..")
