### 문제
초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.  
[`자세히 보기`](https://programmers.co.kr/learn/courses/30/lessons/42584)

### 나의 풀이 + 설명
```python
# 풀이1 - 효율성 문제 발생
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
리스트 `pop()`을 사용하여 큐처럼 사용하였다. 이후 남아있는 리스트 값에 filter를 걸어 기준값보다 작은 요소를 찾으려고 하였다. 정확성 테스트에서는 모두 통과했으나 효율성 테스트에서 모두 실패하였다. filter 과정에서 리스트의 모든 요소를 거쳐 시간효율성이 떨어진다고 생각했다.  
<br>
<br>
```python
# 풀이2 - 효율성 문제 발생
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
풀이1의 문제를 보완하기 위해 for문+break를 사용하여 기준값보다 작은 요소를 찾자마자 리스트를 돌지 않도록 코드를 짰다. 하지만 이 역시 효율성 테스트에서 계속 실패하였고, 이중 for문의 문제가 아닐까 생각하였다.  
<br>
<br>
```python
# 풀이3 - 효율성 문제 발생
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
answer 리스트를 생성하여 시간에 대한 기본 세팅을 하였다. 이후 for문을 사용하여 조건에 부합하는 요소들은 시간을 갱신토록 하였다. 정확도 테스트에서 최대 0.45ms가 나와 효율성이 나쁘지 않다고 생각했다. 하지만 효율성 테스트에서 모두 실패하였다.  
<br>
<br>
```python
# 풀이4 - 효율성 문제 발생
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
이중 for문 때문에 자꾸 효율성 테스트에서 실패하는건 아닐가 생각하여 while문으로 변경해서 시도해보았으나 이 역시 효율성에서 번번히 실패하였다.  
<br>
<br>
```python
# 풀이5 - 통과
def solution(prices): 
    from collections import deque
    prices = deque(prices)
    answer = sorted([i for i in range(len(prices))], reverse = True)
    
    for i in range(len(prices)): 
        x = prices.popleft()
        for p in prices:
            if x > p:
                answer[i] = prices.index(p) + 1
                break

    return answer
```
이쯤되니 이중 for문의 문제는 아닌 것 같다는 생각이 들었다. 특히 풀이3의 속도가 나쁘지 않아 이중 for문이 문제라고 여겨지지 않았다. 스택/큐 문제인 것을 상기했고, 리스트를 큐로 바꾸어보았다. 풀이3과 진행은 똑같으나 리스트를 큐로 변환, pop()을 큐의 popleft()로 바꾸어 테스트해보니 드디어 통과되었다.  
리스트와 큐의 쓰임이 비슷하여 이렇게 큰 차이가 있는지 몰랐다. 참고로 리스트의 시간복잡도는 O(n)이고 큐는 O(1)이다.
