sum=int(input())
count=0
i=1
while True:
  if sum>i:
    sum-=i
    count+=1
    i+=1
  else:
    break
print(count)