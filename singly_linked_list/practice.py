# Create Notes
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create Linked List
class LinkedList:
    def __init__(self):
        # when our linked list is initially empty we make sure HEAD starts out as NONE
        self.head = None

    def listLength(self):
        currentNode = self.head
        length = 0
        while currentNode is not None:
            length += 1
            currentNode = currentNode.next
        return length

    def isListEmpty(self):
        if self.head is None:
            return True
        else:
            return False

#CREATING A NEW HEAD NODE AND INSERTING INTO THE LIST AS THE HEAD NODE INSTRUCTIONS
# 1.) Store current head node in a temporary node!
# 2.) Remove the status of the original head node and put the status on the new node you want to be head
# 3.) Now make the .next of the new headnode point to the original headnode.

    def insertHead(self, newNode):
        # data => ILOVEFOOD, next => None
        #storing original head value
        temporaryNode = self.head # Robert
        #assigning the new node to the head node 
        self.head = newNode #ILOVEFOOD
        # new head node needs to point to original head node
        self.head.next = temporaryNode #ILOVEFOOD -> Robert

        #NO LONGER NEED TEMPORARY NODE.. SO DELETE IT
        del temporaryNode

#PROGRAM LOGIC FOR INSERTING INBETWEEN 2 NODES
    # 1.) Loop over your list till you find where you want to insert your new node
        # nodes act as arrays in a way similar to the index starting at 0 and goes 1,2,3,4,5, etc...
        # once you find where you want to insert say you want to insert at index 4. then 3 will become
        # your previous node and you need to point the .next of your previous node to the node your inserting.
    # 2.) Store the details of the previous node so you dont lose your nodes information
    # 3.) Point the .next of the previous node to the new node being added 
    # 4.) The new node is now your node at position 4 and the node that was there before will be placed at index 5

    def insertAt(self, newNode, position):

        if position < 0 or position > self.listLength():
            print("Invalid Position")
            return
        #if trying to add it to the head
        if position == 0:
            self.insertHead(newNode)
            return
        # head => 10 -> 20 -> None || newNode=>15-> None || position=>1
        #1.) store your previous nodes value
        currentNode = self.head # our old head was 10 but now its 20 after adding 
        currentPosition = 0 #This keeps track of where we are during our loop. AND we START AT 0
        while True:
            # while looping check each value to see if it matches the value we declare
            if currentPosition == position:
                #redirect the .next of our previous node which is (10) to our new node were inserting.
                previousNode.next = newNode
                #redirect the .next of the new node to the current node which is now 20.
                newNode.next = currentNode
                break
            #BEFORE ADVANCING TO THE NEXT NODE STORE THE VALUE OF THE PREVIOUS NODE!
            previousNode = currentNode
            #keeps track of our loop and since there is only 2 current values it goes from 0 to 1 current node equals index 0 and in order to make it move to the next node you set it equal to currentNode.next
            currentNode = currentNode.next
            # now your current position in the loop over our list is 1.
            currentPosition += 1

    def insertEnd(self, newNode):
        # head => Robert which points to none
        if self.head is None:
            self.head = newNode
        else:
            # storing the head of our list in the lastNOde variable so we have something to start at when it comes to our loop
            lastNode = self.head
            # starting our loop here and were going to go through the list and if the current node.next is equal to none we know we have reached the end of our list or (tail) and that is where we insert our new node
            while True:
                if lastNode.next is None:
                    break
                # this marks our last node and we know this because the node after is none. When we run this for loop again when we insert our next value it will do the same thing
            # Each node has data and points to the next node
                lastNode = lastNode.next
            # Here we know what our last node is so we simply add our new node right after it.
            lastNode.next = newNode

    def printList(self):
        if self.head is None:
            print("List is empty")
            return
        # creating a starting point for our loop
        currentNode = self.head
        # inside our loop here 
        while True:
            # as we move through our list print the data but if we get to a point where the node is = to none then break the printing loop
            if currentNode is None:
                break
            # print all nodes value IF its not = none
            print(currentNode.data)
            # currentNode print then move to next
            currentNode = currentNode.next

    def deleteEnd(self):
        #since were deleting the last node in our list
        #start at head
        lastNode = self.head
        #loop through list till currentNode.next is equal to None
        while lastNode.next is not None:
            #in order to fully delete lastNode
            previousNode = lastNode
            #this will simply delete the referrence to our last node but will not delete the data
            lastNode = lastNode.next
        previousNode.next = None

#PROGRAM LOGIC:
    #1.)Loop through list til you find the node you want to delete
    #2.)Store value of previous node
    #3.)Point the .next of previous node to the deletedNode.next value
    #4.)Make the next of this node point to None
    def deleteAt(self, position):

        #CHECK IF INVALID POSITION
        if position < 0 or position >= self.listLength():
            print("Invalid position")
            return

        #CHECK IF LIST IS NOT EMPTY
        if self.isListEmpty() is False:
            if position is 0:
                self.deleteHead()
                return 
        currentNode = self.head
        currentPosition = 0

        while True:
            if currentPosition == position:
                previousNode.next = currentNode.next
                currentNode.next = None
                break
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition += 1



firstNode = Node('Robert')
linkedList = LinkedList()
linkedList.insertEnd(firstNode)
secondNode = Node("Ben")
linkedList.insertEnd(secondNode)
thirdNode = Node("Matthew")
linkedList.insertEnd(thirdNode)
#creating deletemethod
linkedList.deleteEnd()
#creating deleteAt Method
linkedList.deleteAt(1)
linkedList.printList()


# firstNode = Node(10)
# linkedList = LinkedList()
# linkedList.insertEnd(firstNode)
# secondNode = Node(20)
# linkedList.insertEnd(secondNode)
# # linkedList.printList()
# thirdNode = Node(15)
# linkedList.insertAt(thirdNode, 1)
# linkedList.printList()



