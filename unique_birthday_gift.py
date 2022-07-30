from itertools import permutations
n=int(input())
k=int(input())
#array of numbers upto n
a=[x+1 for x in range(n)]

#permutations of array
lis=[]
for i in permutations(a,k):
    lis.append(list(i))
lis+=[[x]*k for x in range(1,n+1)]

#removing arrays that are not divisible
div=[]
for i in lis:
    flag=0
    for j in range(k-1):
        if(i[j+1]%i[j]!=0):
            flag=1
            break
    if(flag==0 and i not in div):
        div.append(i)



print(len(div))
