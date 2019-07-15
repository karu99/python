ab=int(input())
cd=list(map(int,input().split()))
g=[]
for i in cd:
  if(ab.count(i)<2):
    if i not in g:
      g.append(i)
print(*g)
