 n1=int(input())
flag=1
for i in range(2,n1):
    if(n1%i==0):
        flag=0
        break
if(flag):
    print("yes")
else:
    print("no") 
