#That being said, this method of appending is O(n) complexity, 
#and you can make it O(1) by keeping a pointer to the tail of 
#the list and modifying the tail without traversing the list to find it

#TODO add the tail pointer to keep track of the last element
class Node:
  
  # instanciate the node object
  def __init__(self, data = None):
    self.data = data
    self.next = None

class LinkedList:
  
  # instanciate the linked list object
  def __init__(self):
    self.head = None
    self.tail = None
  
  # display a linked list
  def DisplayList(self):
    itr = self.head
    listr = ''
    while itr.next:
      listr += str(itr.data)
      if itr.next.next is not None:
        listr += '->'
      itr = itr.next
    print(listr)
  
  # insert at the beginning of the list
  def Push(self,data = None):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node
  
  # delete element from the beginning from the list
  def DeleteAtHead(self):
    if self.head is None:
      print("The list has no element to delete")
      return
    self.head = self.head.next
    return
  
  #insert at the end of the list
  def Append(self, data = None):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
    itr = self.head
    while itr.next is not None:
      itr = itr.next
    itr.next = new_node
  
  #delete element from the end    
  def Pop(self):
    if self.head is None:
      print('list is empty you can\'t delete anything')
      return
    itr = self.head
    while itr.next is not None:
      if itr.next.next is None:
        itr.next = None
      itr = itr.next

  # insert an element after a specific node  
  def InsertAfterNode(self,current_node_data = None,data = None):
    new_node = Node(data)
    if self.IsEmpty():
      self.head = new_node
      return
    itr = self.head
    while itr is not None:
      if itr.data == current_node_data:
        new_node.next = itr.next
        itr.next = new_node
        break
      itr = itr.next
      if itr == None:
        print('item not in the list')

  # insert an element before a specific node
  def InsertBeforNode(self, current_node_data = None, data = None):
    new_node = Node(data)
    if self.IsEmpty():
      print('this is an empty list')
      return
    if self.head.data == current_node_data:
      new_node.next = self.head
      self.head = new_node
      return
    itr = self.head
    while itr.next is not None:
      if itr.next.data == current_node_data:
        new_node.next = itr.next
        itr.next = new_node
        break 
      else:
        itr = itr.next

  def DeleteSpecificNode(self, Node_Data = None):
    if self.IsEmpty():
      print('this is an empty list')
      return
    if self.head.data == Node_Data:
      self.head = self.head.next
      return
    itr = self.head
    while itr.next is not None:
      if itr.next.data == Node_Data:
        itr.next = itr.next.next
        break
      itr = itr.next
    if itr.next is None:
      print('element not found')
      
  # check if the list is empty
  def IsEmpty(self):
    if self.head == None:
      return True
    return False
  # search if an element exist in the list
  def Search(self, data = None):
    if self.IsEmpty():
      print('list is empty')
    itr  = self.head
    while itr is not None:
      if itr.data == data:
        return True
      itr = itr.next
    return False

  # length of a linked list
  def Length(self):
    itr = self.head
    length = 0
    while itr is not None:
     itr = itr.next
     length+=1
    return length

  # check if the list  is sorted in ascended order
  def IsSorted(self):
    itr = self.head
    while itr.next is not None:
      if itr.data < itr.next.data:
        itr = itr.next
      else:
        print('list is not sorted')
        break
    print('list is sorted')
  
  # check if the list  is sorted in descended order
  def IsReversSorted(self):
    itr = self.head
    while itr.next is not None:
      if itr.data > itr.next.data:
        itr = itr.next
      else:
        print('list is not sorted')
        break
    print('list is sorted')
  
  def ReverseList(self):
    prev = None
    itr = self.head
    while itr is not None:
      next = itr.next
      itr.next = prev
      prev = itr
      itr = next
    self.head = prev
      
    


LL = LinkedList()
for i in range(6):
  LL.Push(i)
#LL.DeleteSpecificNode(1)
LL. ReverseList()
LL.DisplayList()
print(LL.Search(3))
print(LL.Search(31))
