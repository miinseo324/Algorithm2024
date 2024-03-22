# 도시의 개수
n=int(input())
# 각각의 도로의 길이
road=list(map(int,input().split()))
# 기름 가격
g_price=list(map(int,input().split()))
g_price.pop(-1)
total=0
count=n-1
while count!=0:
  if g_price[0] == min(g_price):
    total+=g_price[0]*sum(road)
    break
  else:
    total+=g_price[0]*road[0]
    road.pop(0)
    g_price.pop(0)
    count-=1
print(total)