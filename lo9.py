s1=input()
s2=input()
l=[]
for i in s2:
    l.append(i)
if(len(s2)==len(s1)):
   for i in range(len(s1)):
       k=ord(s1[i])-ord('a')+1
       l[i]=ord(s2[i])+k
for i in l:
   if i>ord('z'):
       i=i-ord('z')+ord('a')-1
   print(chr(i),end="")      
