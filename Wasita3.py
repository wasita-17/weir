class Node:
    def __init__(self, info = None):
       self.info = info
       self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def AtTheBegining(self, data):
        if self.head != None:
            NewNode = Node(data)
            NewNode.next = self.head
            self.head = NewNode
        else:
            NewNode = Node(data)
            NewNode.next = None
            self.head = NewNode
            self.tail = NewNode
    
    def AtTheEnd(self, data):
        if self.head == None:
            NewNode = Node(data)
            NewNode.next = None
            self.head = NewNode
            self.tail = NewNode
        else:
            NewNode = Node(data)
            NewNode.next = None
            self.tail.next = NewNode
            self.tail = NewNode
    
    def AtDisplay(self):
        print("ข้อมูลใน Singly linked list คือ")
        current = self.head
        total = 0
        count = 0
        while current :
            print(current.info)
            total += current.info
            count += 1
            current = current.next
        average = total / count
        print(f'ข้อมูลที่จัดเก็บในตำแหน่งที่พอยเตอร์ head ชี้ คือ ', self.head.info )
        print(f'ข้อมูลที่จัดเก็บในตำแหน่งที่พอยเตอร์ tail ชี้ คือ ', self.tail.info )
        print(f'ค่าเฉลี่ยของข้อมูลที่เก็บใน Singly linked list คือ {average:.2f} ')

      

SLink = SLinkedList()

print('โปรดระบุทางเลือกในการดำเนินการกับ Singly link list')
print('B : เพิ่มข้อมูลที่จุดเริ่มต้นของ Singly linked list')
print('E : เพิ่มข้อมูลแบบต่อจากโหนดสุดท้ายของ Singly linked list')


while True :
    S = input('ทางเลือกในการดำเนินการ = ')
    if S == 'B' :
        data = int(input('ตัวเลขที่ต้องการเพิ่ม : '))
        SLink.AtTheBegining(data)

    elif S == 'E' :
        data = int(input('ตัวเลขที่ต้องการเพิ่ม : '))
        SLink.AtTheEnd(data)
    
    else :
        break
              
SLink.AtDisplay()



