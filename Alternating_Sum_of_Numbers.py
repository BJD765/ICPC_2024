n = int(input())


while(n > 0) :
    i = int(input())
    numeric = input().split(" ")

    operator = 0
    result = 0

    while(operator < i) :
        
        if(operator % 2 == 0) :

            result += int(numeric[operator])
        
        elif (operator % 2 == 1) :

            result -= int(numeric[operator])
        operator += 1
    n -= 1
    print(result)

1