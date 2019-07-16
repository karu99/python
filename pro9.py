x=int(input())
y=[]
z=0
for i in range(0,x):
    y.append(i)
for j in range(len(y)):
    for k in range(j+1,len(y)):
        z+=1
print(z)
