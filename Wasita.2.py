class CircularQueue:
    def __init__(self,n):
        self.n = n
        self.queue = [ ] * n
        self.front = -1
        self.rear = -1

    def enqueue(self,data):
        if ((self.rear+1)%self.n == self.front):
            print('เพิ่มข้อมูลไม่ได้เพราะคิววงกลมเต็ม')
        elif (self.front == -1):
            self.front = 0
            self.rear  = 0
            self.queue.append(data)
        else:
            self.rear = (self.rear+1)%self.n
            self.queue.append(data)

    def dequeue(self):
        if(self.front == -1):
            print('ลบข้อมูลไม่ได้เพราะคิววงกลมว่าง')
        elif (self.front == self.rear):
            self.front = -1
            self.rear  = -1
        else:
            self.front = (self.front + 1)%self.n

    def display(self):
        if(self.front == -1):
            print('แสดงข้อมูลไม่ได้เพราะคิววงกลมว่าง')
        elif(self.rear >= self.front):
            for i in range(self.front,self.rear +1):
                if self.queue[i] > 150: 
                    print(self.queue[i])
        else:
            for i in range(self.front,self.n):
                if self.queue[i] > 150: 
                    print(self.queue[i])
   
n = int(input('โปรดระบุขนาดของคิววงกลมที่มีขนาดตั้งแต่ 5 ช่อง : '))
while   n < 5 :
    n = int(input('โปรดระบุขนาดของคิววงกลมที่มีขนาดตั้งแต่ 5 ช่อง : '))

q = CircularQueue(n)


print('โปรดระบุทางเลือกในการดำเนินการ')
print('1.รับข้อมูลตัวเลขจำนวนเต็มเพื่อจัดเก็บในคิววงกลม')
print('2.ลบข้อมูลที่จัดเก็บในคิววงกลม 1 ตัว')
print('3.แสดงตัวเลขจำนวนเต็มที่มีค่าน้อยกว่า 150 ที่จัดเก็บในคิววงกลม')


num = int(input('โปรดระบุทางเลือกในการดำเนินการ : '))

while num == 1 or num == 2 or num == 3 :
    if num == 1 :
        data = int(input('ป้อนข้อมูลตัวเลข : '))
        q.enqueue(data)

    elif num == 2 :
        q.dequeue()

    elif num == 3 :
        q.display()

    else :
        print('ทางเลือกไม่ถูกต้อง ลองใหม่อีกครั้ง')




