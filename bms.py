n=int(input())
m=[]
for i in range(n):
    l=[]
    l=list(map(int,input().split()))
    m.append(l)
 
k=[]   
for i in m:
    for j in i:
        k.append(j)
k.sort()
for i in k:
    print(i,end=" ")    
