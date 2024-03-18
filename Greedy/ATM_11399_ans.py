n = int(input())
atm = list(map(int, input().split()))

atm.sort()
sum_atm = 0

for i in range(0, n):
  sum_atm += sum(atm[0:i + 1])

print(sum_atm)
