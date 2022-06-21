### Task description
given a non-empty array A of N integers, returns the minimal difference that can be achieved.  
[`more`](https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/)

### Solution
```python
# 풀이1
def solution(A):
    answer = []
    for i in range(1,len(A)):
        result = abs(sum(A[:i]) - sum(A[i:]))
        answer.append(result)
    return min(answer)
```
time complexity O(N * N) : 53%  
리스트의 슬라이싱을 사용하여 파트별 합계를 구하였다. 이때 파트별 합계 차이의 절댓값을 answer 리스트에 append시켜 가장 작은 값을 출력시키도록 하였다.  
<br>
<br>
```python
# 풀이2
def solution(A):
    answer = []
    x = A.pop(0)
    for i in range(1,len(A)+1):
        result = abs(x - sum(A))
        answer.append(result)
        x += A.pop(0)

    return min(answer)
```
time complexity O(N * N) : 53%  
풀이1을 보완하기 위해 리스트 슬라이싱 대신 pop을 사용하여 리스트의 요소를 빼냈고, 이후 합계 차를 구하도록 하였다.  
<br>
<br>
```python
# 풀이3
def solution(A):
    from collections import deque
    A = deque(A)
    
    answer = []
    x = A.popleft()
    for i in range(1,len(A)+1):
        result = abs(x - sum(A))
        answer.append(result)
        x += A.popleft()

    return min(answer)
```
time complexity O(N * N) : 53%  
풀이2를 보완하기 위해 리스트 대신 큐를 사용하였지만 시간복잡도는 동일했다.  
<br>
<br>
```python
# 풀이4
def solution(A):
    sum_a = sum(A)
    answer = []
    y = 0
    for i in range(len(A)-1):
        x = A.pop(0)
        y += x
        sum_a -= x
        result = abs(y - sum_a)
        answer.append(result)

    return min(answer)
```
time complexity O(N * N) : 69%  
for문을 돌때마다 sum()을 해줄 필요가 없다는 것을 발견하였다. 먼저 리스트 전체 합계를 구한 후 for문을 돌때마다 해당 요소값을 파트별로 +- 해주는 방식으로 코드를 구성하였다. 성능이 향상되었다.  
<br>
<br>
```python
# 풀이5
def solution(A):
    from collections import deque
    A = deque(A)
    sum_a = sum(A)
    answer = []
    y = 0
    for i in range(len(A)-1):
        x = A.popleft()
        y += x
        sum_a -= x
        result = abs(y - sum_a)
        answer.append(result)

    return min(answer)
```
time complexity O(N) : 100%  
풀이4를 보완하기 위해 리스트를 큐로 변환하였다. 시간복잡도가 개선되었다.  
  

