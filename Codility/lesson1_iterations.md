### Task description
that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.  
[`more button`](https://app.codility.com/programmers/lessons/1-iterations/)

### Solution
```python
def solution(N):
    lst = []
    while True:
        N, rmd = divmod(N,2)
        lst.append(rmd)
        if N == 1 :
            lst.append(1)
            break

    lst.reverse()
    cnt = 0
    bi_gap = []
    for i in lst:
        if i == 0:
            cnt += 1
        elif i == 1:
            bi_gap.append(cnt)
            cnt = 0   

    return max(bi_gap)
```
