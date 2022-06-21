### Task description
given an array A consisting of N integers fulfilling the above conditions, returns the value of the unpaired element.  
[`more button`](https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/)

### Solution
```python
def solution(A):
    from collections import Counter
    result = Counter(A)

    for k,v in result.items():
        if v%2 == 1:
            return k
```
