n = int(input())
atm = list(map(int, input().split()))

atm.sort()
sum = 0

for i in range(n, 0, -1):
  sum += i * atm[n - i]

print(sum)