### 문제
어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.  

어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.  
[`자세히 보기`](https://programmers.co.kr/learn/courses/30/lessons/42747)

### 나의 풀이
```python
def solution(citations):
    lennum = len(citations)
    hidx = 0
    citations.sort()
    
    for c in range(lennum+1):
        upper = len(list(filter(lambda x: x >= c, citations)))
        if upper >= c :
            hidx = c
    return hidx
```
