
### 나의 풀이
```python
def solution(answers):
    import numpy as np
    
    num = len(answers)
    dict = {1: [1,2,3,4,5],
            2: [2,1,2,3,2,4,2,5],
            3: [3,3,1,1,2,2,4,4,5,5]}
    
    cnt = []
    for k in dict.values():      
        question = k * divmod(num,len(k))[0] + k[:divmod(num,len(k))[1]]
        answers = answers * divmod(num, len(answers))[0] + k[:divmod(num,len(answers))[1]]
        correct = sum(np.array(question) == np.array(answers))
        cnt.append(correct)
    
    result = []
    for k,i in enumerate(cnt == max(cnt)):
        if i:
            result.append(k+1)
    return result
```
