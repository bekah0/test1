

#a = int(input())
#l = list(input().split('.'))
#print(l)
#for i in range(len(l)):

while True:
    l=list(input())
    if len(l)==1 and l[0]=="." :
        break
    s=[]
  #  d=[]
    c=True
    for j in l :
        if j == "(" :
            s.append("(")
        elif j == ")" :
            if s[-1]=="(" and len(s)!=0 :
                s.pop()
        elif j == "[" :
            s.append("[")
        elif j == "]" :
            if s[-1]=="[" and len(s)!=0 :
                s.pop()
            
    if ((len(s)!=0)) :
        c=False
    
    #    print("YES")
    if (c==True):
        print("yes")
    else :
        print("no")
