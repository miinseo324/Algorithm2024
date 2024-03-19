x = int(input())
num = []

a = list(map(int, input().split()))
a.sort()

b = list(map(int, input().split()))
b.sort(reverse=True)

for i in range(x):
  num.append(a[i] * b[i])

print(sum(num))
