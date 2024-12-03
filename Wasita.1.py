def isEmpty (myStack):
    if len(myStack) == 0:
        print('Stack is empty')
        return 1
    else:
        return 0
    
def isFull (myStack):
    if len(myStack)== n:
        print('Stack is full')
        return 1
    else:
        return 0

def push_Stack (item, wasitaStack):
    test = isFull(wasitaStack)
    if test == 1:
        print('จัดเก็บข้อมูลไม่ได้เพราะ Stack เต็ม')
    else:
        wasitaStack.append(item)

def pop_Stack (wasitaStack):
    test = isEmpty(wasitaStack)
    if test == 1:
        print('ลบข้อมูลไม่ได้เพราะ Stack ว่าง')
    else:
        wasitaStack.pop()

def display_Stack (wasitaStack):
    test= isEmpty(wasitaStack)
    if test == 1:
        print('แสดงข้อมูลใน Stack ไม่ได้เพราะ Stack ว่าง')
    else:
        print(wasitaStack)

def average_Stack(wasitaStack):
    test= isEmpty(wasitaStack)
    if test == 1:
        print('แสดงข้อมูลใน Stack ไม่ได้เพราะ Stack ว่าง')
    else:
        avg = 0
        for w in wasitaStack :
            avg = avg + w
            average = avg / len(wasitaStack)
        txt = ' ค่าเฉลี่ยของข้อมูลใน Stack คือ{:.2f}'
        print(txt.format(average))


n = int(input('โปรดระบุขนาดของ Stack ที่มีขนาตั้งแต่ 6 ช่องขึ้นไป :'))
while   n < 6 :
    n = int(input('โปรดระบุขนาดของ Stack ที่มีขนาตั้งแต่ 6 ช่องขึ้นไป :'))
wasitaStack = []*n


print('โปรดระบุทางเลือกในการดำเนินการกับ Stack ')
print('1.เพิ่มข้อมูลใน Stack')
print('2.ลบข้อมูลจาก Stack')
print('3.แสดงข้อมูลทั้งหมดที่จัดเก็บใน Stack')
print('4.แสดงค่าเฉลี่ยของข้อมูลที่จัดเก็บใน Stack')
w = int(input('ทางเลือกในการดำเนินการ = '))


