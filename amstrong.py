num=int(input())
temp=int(num)
sum=0
while(temp!=0):
  a=temp%10
  sum=sum+(a*a*a)
  temp=temp//10
if(num==sum):
   print("yes")
else:
  print("no")
