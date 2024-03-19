money = [500, 100, 50, 10, 5, 1]
change = 1000 - int(input())
sum = 0
for i in money:
  if change != 0:
    sum += change // i
    change = change % i
print(sum)
