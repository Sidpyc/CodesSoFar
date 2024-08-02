def push():
    x=int(input("enter the element to be inserted into the stack"))
    if x%5==0:
        s.append(x)
    else:
        print(x," cannot be inserted as it is not the multiple of 5")
def pop():
     
    if len(s)==0:
        print("Stack empty")
    else:
        print("Element deleted is :",s.pop())
def display():
    print(len(s))
    if len(s)==0:
        print("Stack empty")
    else:
        for i in range(len(s)):
            print(s[i],end=' ')
#main
con='y'
s=[]
while con=='y':
    print("STACK OPERATION ")
    print("1. PUSH")
    print("2. POP")
    print("3. DISPLAY")
    print("4. EXIT")
    ch=int(input("Enter your choice :"))
    if ch==1:
        push()
    elif ch==2:
        pop()
    elif ch==3:
        display()
    else:
        break
con=input("Do you want to continue (y/n) :")
