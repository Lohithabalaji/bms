s,l=map(int,input().split())
m=list(map(int,input().split()))
s=[]
for i in range(l):
    s.append(list(map(int,input().split())))
for i in s:
  su=0
  for j in range(i[0]-1,i[1]):
      su=su+m[j]
  print(su) 
