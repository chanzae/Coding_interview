### 문제
현재 대기목록에 있는 문서의 중요도가 순서대로 담긴 배열 priorities와 내가 인쇄를 요청한 문서가 현재 대기목록의 어떤 위치에 있는지를 알려주는 location이 매개변수로 주어질 때, 내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 return 하도록 solution 함수를 작성해주세요.  
[`자세히 보기`](https://programmers.co.kr/learn/courses/30/lessons/42587)

### 나의 풀이
```python
def solution(priorities, location):
    answer = []
    while True:
        for i,p in enumerate(priorities):
            find_max = max(priorities)
            if (p == find_max) & (find_max != 0) :
                answer.append(i)
                priorities[i] = 0
                
        if sum(priorities) == 0:
            break
            
    result = answer.index(location) + 1
    return result
```

### 설명
무한루프문을 사용하여 리스트에 방향성을 주었다. 
