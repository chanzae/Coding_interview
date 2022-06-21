### Task description
given an array A, returns the value of the missing element.  
[`more`](https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/)  


### Solution
```python
# 풀이1
def solution(A):
    base = [i for i in range(1,len(A)+2)]
    for b in base:
        if b not in A:
            return b
```
time complexity O(n2) : 60%  
for문을 사용했을 때 타임에러로 몇몇 테스트에서 실패하였다.   
  

```python
# 풀이2 - 통과
def solution(A):
    from collections import Counter
    
    lst = [i for i in range(1, len(A)+2)]
    diff = Counter(lst) - Counter(A)
    result = list(diff.keys())[0]

    return result
```
time complexity O(N) or O(N * log(N)) : 100%  
이를 보완하기 위해 collections 모듈을 임포트하여 시간복잡도를 줄였다.  
