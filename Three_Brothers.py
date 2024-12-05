str = input().strip()
num = str.split(" ")
a = int(num[0])
b = int(num[1])

if(a == 1) :
    if(b == 2) :
        print("3")
    elif (b == 3) : 
        print("2")

elif (a == 2) : 
    
    if(b == 1) :
        print("3")

    elif ( b == 3) :
        print("1")

elif (a == 3) : 
    
    if(b == 1) :
        print("2")

    elif ( b == 2) :
        print("1")      