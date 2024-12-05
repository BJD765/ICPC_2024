
n = int(input())
for i in range (n):
    rep = int(input())
    code = []
    for j in range (rep) :
        code.append(input())
        
    for j in range (rep) :
        print(code[rep - j - 1].rindex('#') + 1, end=' ')
    print("\n")

    
