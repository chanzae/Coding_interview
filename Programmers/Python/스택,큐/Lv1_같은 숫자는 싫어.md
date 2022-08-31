### 문제
배열 arr가 주어집니다. 배열 arr의 각 원소는 숫자 0부터 9까지로 이루어져 있습니다. 이때, 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고 합니다. 단, 제거된 후 남은 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지해야 합니다.  
[`자세히 보기`](https://school.programmers.co.kr/learn/courses/30/lessons/12906)
<br>
<br>
### 나의 풀이
```python
def solution(arr):
    from collections import deque
    
    darr = deque(arr)
    answer = []
    for i in range(len(darr)-1):
        if darr[0] == darr[1]:
            darr.popleft()
        else:
            answer.append(darr[0])
            darr.popleft()
            
    answer.append(darr[0])
    return answer
            
```
<br>

### 설명
popleft()로 원소를 하나씩 선택/제거하였다. for문과 if문을 사용하여 원소를 비교, 연속적으로 나타나지 않는 수만 answer에 따로 append하였다.