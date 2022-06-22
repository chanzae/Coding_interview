### Task description
A small frog wants to get to the other side of a river. The frog is initially located on one bank of the river (position 0) and wants to get to the opposite bank (position X+1). Leaves fall from a tree onto the surface of the river.  

You are given an array A consisting of N integers representing the falling leaves. A[K] represents the position where one leaf falls at time K, measured in seconds.  

The goal is to find the earliest time when the frog can jump to the other side of the river. The frog can cross only when leaves appear at every position across the river from 1 to X (that is, we want to find the earliest moment when all the positions from 1 to X are covered by leaves). You may assume that the speed of the current in the river is negligibly small, i.e. the leaves do not change their positions once they fall in the river.  
[`more`]()  


### Solution
```python
# 풀이1
def solution(X, A):
    xlist = [i for i in range(1,X+1)]
    
    for a in A:
        if a in xlist:
            xlist.pop(xlist.index(a))

        if len(xlist) == 0:
            answer = A.index(a)
            break
        else:
            answer = -1
            
    return answer
```
time complexity O(N ** 2) : 63%  
1~X로 구성된 xlist를 만들어 놓고, A를 for문으로 돌려 해당 요소가 xlist안에 들어 있으면 pop()으로 xlist의 요소를 제거하는 방식으로 구성하였다.
<br>
<br>
```python
# 풀이2
def solution(X, A):
    from collections import deque
    xlist = []
    adeque = deque(A)

    for i in range(len(A)):
        x = adeque.popleft()
        if x not in xlist:
            xlist.append(x)

        if len(xlist) == X:
            answer = i
            break
        else:
            answer = -1
            
    return answer
```
time complexity O(N ** 2) : 54%  
풀이1의 시간복잡도를 개선시키기 위해 큐를 사용했지만 시간복잡도가 더 떨어졌다.
<br>
<br>
```python
# 풀이3
def solution(X, A):
    from collections import Counter
    xlist = Counter([i for i in range(1,X+1)])

    for idx in range(len(A)):
        a = A.pop(0)
        if a in xlist:
            xlist.pop(a)

        if len(xlist) == 0:
            answer = idx
            break
        else:
            answer = -1
            
    return answer
```
time complexity O(N) : 81%  
xlist를 Counter로 구성하였더니 시간복잡도가 개선되었다.
<br>
<br>
```python
# 풀이4 - 통과
def solution(X, A):
    from collections import Counter, deque
    xlist = Counter([i for i in range(1,X+1)])
    adeque = deque(A)

    for idx in range(len(adeque)):
        a = adeque.popleft()
        if a in xlist:
            xlist.pop(a)

        if len(xlist) == 0:
            answer = idx
            break
        else:
            answer = -1
            
    return answer
```
time complexity O(N) : 100%  
풀이3에서 힌트를 얻어 A를 큐로 변환하였다. 
