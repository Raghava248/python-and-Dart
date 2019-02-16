x = []
class A:
    def m1(self):
        print('Enter list of elements you want in the stack')
        i = input().split(',')      
        for l in i:
            x.append(int(l))
a1 = A()
a1.m1()
class B(A):
    def stack(self):
        print("Enter 1 if you want to remove an element based on index")
        print("Enter 2 if you want to remove an element based on value")
        print("Enter 3 if you want to insert an element anywhere in the list")
        print("Enter 4 if you want to stop performing operations on the stack")
        while True:
            print('Enter a specific choice i.e, a specifed number given to perform a particular operation')    
            j = int(input())
            if j == 1:
                print("Enter index you want to remove")
                k = int(input())
                x.pop(k)
            if j == 2:
                print("Enter value you want to remove")
                k = int(input())
                x.remove(k)
            if j == 3:
                print("Here you need to enter an index and the value you want to insert in to the list")
                index = int(input())
                value = int(input())
                x.insert(index,value)
            if j == 4:
                break
b1 = B()
b1.stack()
print(x)
    
        
