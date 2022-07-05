### 문제
트럭 여러 대가 강을 가로지르는 일차선 다리를 정해진 순으로 건너려 합니다. 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다. 다리에는 트럭이 최대 bridge_length대 올라갈 수 있으며, 다리는 weight 이하까지의 무게를 견딜 수 있습니다. 단, 다리에 완전히 오르지 않은 트럭의 무게는 무시합니다.  
[`자세히 보기`](https://school.programmers.co.kr/learn/courses/30/lessons/42583)

### 나의 풀이
```python
def solution(bridge_length, weight, truck_weights):
    from collections import deque
    
    bridge = deque([0] * bridge_length)
    sum_bridge = sum(bridge)
    truck = deque(truck_weights)
    cnt = 0

    for i in range(len(truck_weights)):
        x = truck.popleft()
        while True:
            y = bridge.popleft()
            sum_bridge -= y
            if sum_bridge + x > weight:
                bridge.append(0)
                cnt+= 1
            else:
                break
        sum_bridge += x
        bridge.append(x)
        cnt += 1
                
    return cnt + bridge_length
```

### 설명
스택/큐를 사용, 반복문을 돌려 트럭이 다리를 지나가는 것처럼 구현하였다. 이 문제에서 시간효율성을 줄이는 키는 sum()을 반복하지 않는 것이다. 매번 다리의 무게를 sum할 경우 시간복잡도가 올라가므로 따로 변수에 지정하여 +- 연산하는 방식으로 풀이하였다. 