n8,S8=map(int,input().split())
m8=list(map(int,input().split()))
m8.sort()
m8.reverse()
s7=S8
t7=0
for i in m8:
    if(s7>=i):
        no=int(s7/i)
        t7=t7+no
        s7=s7-no*i
    if s7==0:
        break
if(s7==0):
   print(t7)
else:
   print("it's not posiible to select coins in such a way that they sum upto",S8)      
