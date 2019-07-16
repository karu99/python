a,b=input().strip().split(" ")
b=int(b)
sum=0
while(sum<len(a)-1 and b):
  if(a[sum]>a[sum+1]):
    b-=1
    a=a[:sum]+a[sum+1:]
    if(sum!=0):
      sum-=1
  else:
    sum+=1
q1=a[:len(a)-b]
print(q1)
