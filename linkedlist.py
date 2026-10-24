class node:
  def __init__(self,value):
    self.data=value
    self.next=None

class linkedlist:
  def __init__(self):
    self.head=None
    self.n=0

  def __len__(self):
    return self.n

  def insert_head(self,value):
    new_node=node(value)
    new_node.next=self.head
    self.head=new_node
    self.n=self.n + 1

  def traverse(self):
    curr=self.head
    while curr!=None:
      print(curr.data)
      curr=curr.next


l=linkedlist()
l.insert_head(10)
l.insert_head(20)
l.insert_head(30)
l.insert_head(40)

print(l.traverse())