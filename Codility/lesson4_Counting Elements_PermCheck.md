### Task description
A non-empty array A consisting of N integers is given.  

A permutation is a sequence containing each element from 1 to N once, and only once.  
[`more`](https://app.codility.com/programmers/lessons/4-counting_elements/perm_check/)
<br>

### Solution
```python
#풀이1
def solution(A):
    from collections import deque

    adeque = deque(A)
    alist = [i for i in range(1,len(A)+1)]
    for i in range(len(A)):
        a = adeque.popleft()
        if a in alist:
            alist.pop(alist.index(a))

    if len(alist) == 0:
        return 1
    else:
        return 0
```
 time complexity O(N ** 2) : 50%  
1~N까지의 순열을 갖는 alist를 만들고, for문을 돌려 얻은 A리스트의 요소를 대응시켜 값이 있으면 alist의 해당 요소값을 제거하는 방식으로 코드를 구성하였다.  
<br>
<br>
```python
# 풀이2
def solution(A):
    from collections import Counter

    result = Counter([i for i in range(1,len(A)+1)]) - Counter(A)
    if len(result) == 0:
        return 1
    else:
        return 0
```
time complexity O(N) or O(N * log(N)) : 100%
for문을 사용할 경우 모든 요소에 대해 일일이 대응시켜야하므로 계산이 오래 걸린다. 따라서 counter를 사용하여 리스트 연산이 가능토록 하였다. 
