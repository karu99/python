x,y=input().strip().split(" ")
y=int(y)
sum=0
while(sum<len(x)-1 and y):
  if(x[sum]>x[sum+1]):
    y-=1
    x=x[:sum]+a[sum+1:]
    if(sum!=0):
      sum-=1
  else:
    sum+=1
q1=x[:len(x)-y]
print(q1)
