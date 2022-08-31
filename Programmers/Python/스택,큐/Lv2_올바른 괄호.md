### 문제
'(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.  
[`자세히 보기`](https://school.programmers.co.kr/learn/courses/30/lessons/12909)
<br>

### 나의 풀이
```python
def solution(s):
    lst = ''
    for i in range(len(s)):
        lst += s[i]
        if lst[-2:] == '()':
            lst = lst[:-2]
    if len(lst) >0 :
        return False
    return True
```

### 설명
처음에는 replace를 사용하여 풀이했을 때 효율성 문제로 통과되지 못함. 문자열을 하나씩 스택하여 마지막 2개를 비교하는 방법으로 풀이하였다.