s1=input()
j=0
for i in range(len(s1)):
    if(s1[j]<s1[i]):
        print(s1[i:])
        break
