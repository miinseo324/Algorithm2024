t = int(input())
coin_list = [25, 10, 5, 1]
total = [0, 0, 0]
for j in range(t):
  n = int(input())
  change = []
  for i in range(4):
    change.append(n // coin_list[i])
    n %= coin_list[i]
  print(*change)
