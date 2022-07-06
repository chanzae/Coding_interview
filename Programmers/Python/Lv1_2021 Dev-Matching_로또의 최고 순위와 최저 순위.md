### 문제
민우가 구매한 로또 번호를 담은 배열 lottos, 당첨 번호를 담은 배열 win_nums가 매개변수로 주어집니다. 이때, 당첨 가능한 최고 순위와 최저 순위를 차례대로 배열에 담아서 return 하도록 solution 함수를 완성해주세요.  
[`자세히 보기`](https://school.programmers.co.kr/learn/courses/30/lessons/77484)

### 나의 풀이
```python
def solution(lottos, win_nums):
    from collections import Counter
    
    num_cnt = len(lottos) 
    match = {str(k):i for i,k in zip(range(num_cnt,-1,-1),range(1,num_cnt+1))}
    match['0'] = 6
                                
    check = Counter(lottos) - Counter(win_nums)
    min_winning = num_cnt - sum(check.values())
    max_winning = min_winning + check[0]

    answer = [match[str(max_winning)],match[str(min_winning)]]
    return answer
```

### 설명
Counter를 사용하여 로또 번호와 당첨번호가 맞는지 확인하였고, 이를 활용하여 최소 당첨/최대 당첨을 개수를 구하였다.
