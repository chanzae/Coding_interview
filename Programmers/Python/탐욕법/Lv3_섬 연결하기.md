### 문제
n개의 섬 사이에 다리를 건설하는 비용(costs)이 주어질 때, 최소의 비용으로 모든 섬이 서로 통행 가능하도록 만들 때 필요한 최소 비용을 return 하도록 solution을 완성하세요.  
[`자세히 보기`](https://programmers.co.kr/learn/courses/30/lessons/42861)

### 나의 풀이
```python
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, costs):
    v = n
    parent = [i for i in range(v+1)]
    result = 0
    edges = costs
    edges.sort(key = lambda x: x[2])

    for edge in edges:
        a, b, cost = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost

    return result
```

### 설명
크루스칼 알고리즘을 참고하여 풀이하였다.
