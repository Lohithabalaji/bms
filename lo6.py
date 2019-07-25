s2,e=input().split(" ")
s2=int(s2)
e=int(e)
for n in range(s2+1,e):
    f=1
    for i in range(2,n):
        if(n%i==0):
            f=0
            break
    if(f):
        print(n,end=" ")
