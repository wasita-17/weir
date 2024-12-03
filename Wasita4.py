class Node:
    def __init__(self):
        self.data = None
        self.leftChild = None
        self.rightChild = None

    def insert(self,data):
        self.data = data 
        data = int(input(f'โปรดป้อนหมายเลขของโหนด Left child ของ {self.data} (ถ้าไม่มีให้ป้อนจำนวนเต็มที่มีค่าน้อยกว่าหรือเท่ากับ 0) : '  ))
        if data > 0 :
            self.leftChild = Node()
            self.leftChild.insert(data)
        
        data = int(input(f'โปรดป้อนหมายเลขของโหนด Right child ของ {self.data} (ถ้าไม่มีให้ป้อนจำนวนเต็มที่มีค่าน้อยกว่าหรือเท่ากับ 0) : ' ))
        if data > 0 :
            self.rightChild = Node()
            self.rightChild.insert(data)
    
    def PreOrder(self,tree):
        if tree:
            if tree.data % 2 == 0:
                print(tree.data , end = " " )
                self.PreOrder(tree.leftChild)
                self.PreOrder(tree.rightChild)
                 
    def InOrder(self,tree):
        if tree:
            if tree.data < 150 :
                self.InOrder(tree.leftChild)
                print(tree.data , end = " ")
                self.InOrder(tree.rightChild)
           
    def PostOrder(self,tree):
        if tree:
            if tree.data % 7 == 0 :

                self.PostOrder(tree.leftChild)        
                self.PostOrder(tree.rightChild)
                print(tree.data, end = " ")

tree = Node()

data = int(input('โปรดป้อนจำนวนเต็มเพื่อจัดเก็บที่ root node : '))

tree.insert(data)

print('ทางเลือกดำเนินการ')
print('1. ท่องไปในต้นไม้ทวิภาคแบบ Pre-order และแสดงจำนวนเต็มที่เก็บในแต่ละโหนดที่เป็นเลขคู่ทางจอภาพ')
print('2. ท่องไปในต้นไม้ทวิภาคแบบ In-order และแสดงจำนวนเต็มที่เก็บในแต่ละโหนดทีมีค่าน้อยกว่า 150 ทางจอภาพ')
print('3. ท่องไปในต้นไม้ทวิภาคแบบ Podt-order และแสดงจำนวนเต็มที่เก็บในแต่ละโหนดทีหารด้วย 7 ลงตัวทางจอภาพ')

num = int(input('ทางเลือกในการดำเนินการ : '))

if num == 1 :
    print('Pre-oder = ' , end = " ")
    tree.PreOrder(tree) 
elif num == 2 :
    print('In-oder = ' , end = " ")
    tree.InOrder(tree)
elif num == 3 :
    print('Post-oder = ' , end = " ")
    tree.PostOrder(tree)