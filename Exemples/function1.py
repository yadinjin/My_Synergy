def fff(f):
    factorial = 1
    for i in range(2,f+1):
        factorial *= i
    return factorial
spisok = []
f = int(input()) 
print(fff(f))
for i in range(fff(f),0,-1):
    spisok.append(fff(i))
print(spisok)
