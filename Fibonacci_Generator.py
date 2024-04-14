def fib_n():
    l=int(input("Enter the n value : "))
    if l==1:
        print(0,end="")
    elif l==2:
        print(1,end="")
    else:
        k=[0,1] 
        for i in range(0,l-2,1):
                k.append(k[-1]+k[-2])
        print(k[-1],end="")      

def fib_num():
    l=int(input("Enter the n value : "))
    if l==1:
        print(0)
    elif l==2:
        print(0,1,sep="  ",end="  ")
    else:
        print(0,1,sep="  ",end="  ")
        k=[0,1] 
        for i in range(0,l-2,1):
            k.append(k[-1]+k[-2])
            print(k[-1],end="  ") 

def fib_ran():
    i=int(input("Enter the inclusive range : "))
    e=int(input("Enter the exclusive range : "))
    k=[i,i+1]
    print(i,i+1,sep="  ",end="  ")
    while((k[-1]+k[-2])<=e):
        k.append(k[-1]+k[-2])
        print(k[-1],end="  ") 

def fib_rang_num():
    i=int(input("Enter the inclusive range : "))
    e=int(input("Enter the exclusive range : "))
    n=int(input("Enter the n value :  "))
    k=[i,i+1]
    while(i<=e):
        k.append(k[-1]+k[-2])
        i=k[-1]+k[-2]
    if n<=len(k):
        print(k[n-1])
    else:
        print("The n you entered is exceeding the range..")

print("Enter 1 to get an nth number in fibonacci series. \nEnter 2 to get first n numbers in fibonacci series. \nEnter 3 to get the fibonacci series in specific range. \nEnter 4 to get nth number in specific range. \nEnter 0 to exit.")
k=int(input("Enter :  "))
while(k!=0):
    if k==0:
        exit()
    elif k==1:
        fib_n()
    elif k==2:
        fib_num()
    elif k==3:
        fib_ran()
    elif k==4:
        fib_rang_num()
    else:
        print("Enter a valid number..")
    k=int(input("\nEnter :  "))
