### 문제
프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.  

또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.  

먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.  
[`자세히 보기`](https://programmers.co.kr/learn/courses/30/lessons/42586)

### 나의 풀이
```python
import math

def solution(progresses, speeds):
    fin = []
    for p,s in zip(progresses, speeds):
        avail_day = math.ceil((100 - p)/ s)
        fin.append(avail_day)
    
    answer = []
    cnt = 1
    for _ in range(len(fin)-1):
        if fin[0] < fin[1]:
            answer.append(cnt)
            fin = fin[1:]
            cnt = 1
        elif fin[0] >= fin[1]:
            cnt+=1
            del fin[1]
            
        if len(fin) == 1:
            answer.append(cnt)
            
    return answer
```

### 설명
첫번째로 배포하기까지 소요되는 기간을 구하기 위해 for문 + zip, math라이브러리의 ceil(올림)을 사용하였다. 두번째로 한번에 배포할 수 있는 작업물을 구하기 위해 조건문을 사용하였다.
