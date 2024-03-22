n=int(input())
cards=[]
for i in range(n):
  cards.append(int(input()))
cards.sort # 오름차순 정렬
cnt=0
for i in range(n-1):
  cards[i+1]=cards[i]+cards[i+1]
  cnt+=cards[i+1]
print(cnt)

# 틀렸음