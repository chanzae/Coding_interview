### 문제
수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.  

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요  
[`자세히 보기`](https://programmers.co.kr/learn/courses/30/lessons/42576)

### 나의 풀이
```python
def solution(participant, completion):
    dict = {p: 0 for p in participant}
    for part in participant:
        dict[part] += 1
    for c in completion:
        dict[c] -= 1
        
    for k,v in dict.items():
        if v != 0:
            answer = k
    
    return answer
```

### 설명
딕셔너리를 쓰지 않고 리스트의 remove를 사용했다면 더 간결하게 풀어낼 수 있지만 효율성 문제가 발생하여 remove를 사용할 수 없었다. (리스트에 비해 딕셔너리는 매우 빠른 시간복잡도를 가지고 있다) 따라서 딕셔너리를 생성해 participant를 +1 카운팅,completion을 -1 카운팅하여 0이 아닌 key값을 리턴하는 방법으로 코드를 구성하였다.

### 다른 사람 풀이에서 배울 점
Collections 모듈을 사용하면 간단하게 문제를 해결할 수 있다.
```python
a = collections.Counter(participant) - collections.Counter(completion)
```
collections.Counter()를 사용해 리스트 요소와 갯수를 키와 값으로 변환 후 이를 연산하면 값이 있는 키만 남는다. 
