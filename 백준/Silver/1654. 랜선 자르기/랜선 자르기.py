# 랜선자르기(결정알고리즘)
k, n = map(int, input().split())
lan = [int(input()) for _ in range(k)]
stdMin = 1
stdMax = max(lan)

while stdMin <= stdMax:
  cutCnt = 0
  stdMid = (stdMin+stdMax) // 2

  # 기준이 커질수록 토막 수는 줄어듦. 즉, 토막 수가 n보다 부족하면 토막 수를 늘려야 하므로 기준을 작게 지정.
  # stdMid의 최대값을 얻기 위해 반복문을 바로 탈출하지 않음. 
  for value in lan:
    cutCnt += value // stdMid
  
  if cutCnt >= n:
    # 오른쪽으로 이동 (기준을 크게) -> 기준 값의 최대값을 구할 수 있음.
    stdMin = stdMid + 1
  else:
    # 왼쪽으로 이동 (기준을 작게)
    stdMax = stdMid - 1
  
print(stdMax)