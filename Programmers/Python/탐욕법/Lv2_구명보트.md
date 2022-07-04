### 문제
무인도에 갇힌 사람들을 구명보트를 이용하여 구출하려고 합니다. 구명보트는 작아서 한 번에 최대 2명씩 밖에 탈 수 없고, 무게 제한도 있습니다.  

사람들의 몸무게를 담은 배열 people과 구명보트의 무게 제한 limit가 매개변수로 주어질 때, 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 return 하도록 solution 함수를 작성해주세요.  
[`자세히 보기`](https://programmers.co.kr/learn/courses/30/lessons/42885)

### 나의 풀이
```python
def solution(people, limit):
    from collections import deque
    
    pp = deque(sorted(people))
    cnt = 0
    while pp:
        if len(pp) <= 1:
            cnt += 1
            break
            
        if pp[0] + pp[-1] > limit:
            pp.pop()
            
        else:
            pp.popleft()
            pp.pop()
    
        cnt += 1
    return cnt
```

### 설명
deque의 pop(),popleft()를 사용하여 제거하였다. 한번에 최대 2명씩밖에 못타는게 문제의 포인트이다.