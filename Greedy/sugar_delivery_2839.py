N = int(input())
result = 0

while N >= 0:
  if N % 5 == 0:
    result += N // 5
    break
  N -= 3
  result += 1
else:
  result = -1

print(result)
'''
최소 봉지를 구하려면?
5키로 봉지를 사용할수록,
3키로 봉지를 사용할수록,

5로 나누어 본 후,
나누어 떨어진다면 바로 result
5로 나누어지지 않는다면,
3을 한번씩 빼면서 5로 나누어질 때까지 반복
끝까지 나누어지지 않는다면, -1 출력
'''
