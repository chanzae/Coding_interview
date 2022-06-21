### Task description
given three integers X, Y and D, returns the minimal number of jumps from position X to a position equal to or greater than Y.  
[`more`](https://app.codility.com/programmers/lessons/3-time_complexity/frog_jmp/)
  

### Solution
```python
def solution(X, Y, D):
    import math
    result = math.ceil((Y-X)/D)

    return result
```