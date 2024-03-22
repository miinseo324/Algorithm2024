# 서로 다른 N개의 자연수의 합 = S
# 자연수 N의 최댓값?

sum = int(input())
list_num = []
count = 1

while True:
  if sum == 0:
    break
  else:
    if count in list_num:
      sum += list_num[-1]
      list_num.pop(list_num[-1])
      count += 1
    else:
      sum -= count
      list_num.append(count)
      count += 1
print(len(list_num))

# 틀림 - 출력이 안됨
