n=int(input())
e=int(input())

count=0;

p=[]
b=[]

for i in range(n):
    p.append(int(input()))
for i in range(n):
    b.append(int(input()))


#for each monster
i=n-1
while(i>=0):
    if(p[i]<=e):
        count+=1
        e+=b[i]
        p.pop(i)
        b.pop(i)
        i=len(p)-1
    else:
        i-=1


print(count)