import sys
input = sys.stdin.readline 

s=[]

a = int(input())

for i in range (a) :

    l = list(input().split())

    if l[0] == "push" :
        s.append(l[1])

    elif l[0] == "pop" :
        try:
            print(s.pop())
        except:
            print(-1)
    elif l[0] == "size" :
        print(len(s))
    
    elif l[0] == "empty" :
        if (len(s)>0) :
            print(0)
        else :
            print(1)

    elif l[0] == "top" :
        try:
            print(s[-1])
        except:
            print(-1)

    
        
