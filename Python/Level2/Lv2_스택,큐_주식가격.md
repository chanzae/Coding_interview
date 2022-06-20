### 문제
초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.  
[`자세히 보기`](https://programmers.co.kr/learn/courses/30/lessons/42584)

### 나의 풀이
```python
# 효율성 문제
def solution(prices):
    answer = []
    for _ in range(len(prices)-1):
        x = prices.pop(0)
        if x <= min(prices):
            answer.append(len(prices))
        else:
            find_num = list(filter(lambda y: y < x, prices))[0]
            answer.append(prices.index(find_num)+1)

    answer.append(0)
    return answer
```

#############
```python
#효율성 문제
def solution(prices):
    answer = []
    for _ in range(len(prices)-1):
        x = prices.pop(0)
        if x <= min(prices):
            answer.append(len(prices))
        else:
            for i in prices:
                if i < x:
                    answer.append(prices.index(i) + 1)
                    break            

    answer.append(0)
    return answer
```
##################
```python
# 효율성 문제 66.7/100
def solution(prices):
    answer = sorted([i for i in range(len(prices))], reverse = True)

    for i in range(len(prices[:-1])):
        for p in prices[i+1:]:
            if prices[i] > p :
                answer[i] = prices[i+1:].index(p) + 1
                break
                
    return answer
```
###################
```python
#효율성문제 - 정확도에서 최대 0.45ms 나오고 있음
def solution(prices):
    answer = sorted([i for i in range(len(prices))], reverse = True)

    for i in range(len(prices)): 
        x = prices.pop(0)
        for p in prices:
            if x > p:
                answer[i] = prices.index(p) + 1
                break

    return answer
```
####################
```python
#효율성 문제
def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices[:-1])):
        x = prices.pop(0)
        for p in prices:
            if x > p:
                answer[i] = prices.index(p) + 1
                break
            else:
                answer[i] = len(prices)

    return answer
```
############
```python
# 효율성 문제
def solution(prices):
    answer = []
    for i in range(len(prices)-1):
        x = prices.pop(0)
        answer.append(len(prices))
        for p in prices:
            if x > p:
                answer[i] = prices.index(p) + 1
                break
                
    answer.append(0)
    
    return answer
```
#############
```python
# 효율성 문제
def solution(prices):
    answer = sorted([i for i in range(len(prices))], reverse = True)
    
    idx = 0
    while True:
        x = prices.pop(0)        
        for p in prices:
            if x > p:
                answer[idx] = prices.index(p) + 1
                break
                
        idx += 1
        if len(prices) == 1:
            break

    return answer
```
########################
```python
# 통과
def solution(prices): 
    from collections import deque
    answer = sorted([i for i in range(len(prices))], reverse = True)
    prices = deque(prices)
    
    for i in range(len(prices)): 
        x = prices.popleft()
        for p in prices:
            if x > p:
                answer[i] = prices.index(p) + 1
                break

    return answer
```