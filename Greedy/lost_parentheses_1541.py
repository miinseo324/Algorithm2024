exp = input().split('-')

num = []

for i in exp:
  sum = 0
  tem = i.split('+')
  for j in tem:
    sum += int(j)
  num.append(sum)

total = num[0]

for i in range(1, len(num)):
  # range(1,2) -> 1만 포함
  # 끝번호 주의 !
  total -= num[i]
print(total)
