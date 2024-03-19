# 문제에서는 B 배열은 재배열을 하면 안된다고 했음
# A 배열은 오름차순으로 정렬시킨 후,
# B 배열에서의 max와 A 배열 요소를 차례로 곱한 후,
# B 배열에서 찾은 max는 한번 사용하면 pop으로 제거

x = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

sum = 0
for i in range(x):
  sum += min(a) * max(b)
  a.pop(a.index(min(a)))
  b.pop(b.index(max(b)))

print(sum)
