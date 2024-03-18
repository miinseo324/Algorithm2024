n, k = map(int,input().split())

coin_val = []
for i in range(n):
  coin_val.append(int(input()))

count = 0

while k>0:
  if k//coin_val[-1] > 0:
    count += k//coin_val[-1]
    k -= coin_val[-1]*(k//coin_val[-1])
    coin_val.pop()
  else:
    coin_val.pop()
print(count)
