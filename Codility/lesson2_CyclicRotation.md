### Task description
that, given an array A consisting of N integers and an integer K, returns the array A rotated K times.  
[`more button`](https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/)

### Solution
```python
def solution(A, K):
    if len(A) > 0 :
        for _ in range(K) :
            x = A.pop(-1)
            A.insert(0,x)
        return A
```