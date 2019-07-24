n,q=map(int,input().split())
d=list(map(int,input().split()))
count=0
for i in range(len(m)):
  for j in range(i+1,len(m)):
    if(m[i]+m[j]==q):
        count=1
        break
if(count):
   print("yes")
else:
   print("no")    
