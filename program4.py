class listnode:

  def __init__(self,data):

    self.data=data
    self.next=None

def addtwonumbers(l1,l2):
  dummy=listnode(-1)
  current=dummy
  carry=0
  temp1=l1
  temp2=l2

  while temp1!=None or temp2!=None:
    total=0
    if temp1!=None:
      total=total+temp1.data
      temp1=temp1.next

    if temp2!=None:
      total=total+temp2.data
      temp2=temp2.next

    total=total+carry

    newnode=listnode(total%10)
    carry=total//10

    current.next=newnode
    current=current.next

  if carry:
      newnode=listnode(carry)
      current.next=newnode

  return dummy.next




l1=listnode(2)
l1.next=listnode(4)
l1.next.next=listnode(3)
l2=listnode(5)
l2.next=listnode(6)
l2.next.next=listnode(4)

answer=addtwonumbers(l1,l2)
current=answer
while current!=None:
  print(current.data,end=" -> ")
  current=current.next
print("NULL")
print(answer.data,end=" ")
print(answer.next.data,end=" ")
print(answer.next.next.data)
