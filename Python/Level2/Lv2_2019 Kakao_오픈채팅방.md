### 문제
채팅방에 들어오고 나가거나, 닉네임을 변경한 기록이 담긴 문자열 배열 record가 매개변수로 주어질 때, 모든 기록이 처리된 후, 최종적으로 방을 개설한 사람이 보게 되는 메시지를 문자열 배열 형태로 return 하도록 solution 함수를 완성하라.  
[`자세히 보기`](https://programmers.co.kr/learn/courses/30/lessons/42888?language=python3)

### 나의 풀이
```python
def solution(record):
    dict = {}
    result = []

    for rec in record:
        state = rec.split(' ')[0]
        user_id = rec.split(' ')[1]

        if state == 'Enter':
            dict[user_id] = rec.split(' ')[2]
            result.append(f'{user_id}님이 들어왔습니다.')

        elif state == 'Leave':
            result.append(f'{user_id}님이 나갔습니다.')

        else:
            dict[user_id] = rec.split(' ')[2]

    for i,re in enumerate(result):
        idx = re.find('님')
        uid = re[:idx]
        result[i] = re.replace(re[:idx],dict[uid])

    return result
```

### 설명
split()을 사용해서 문자열을 구분한뒤 if조건문을 사용하여 결과를 result리스트에 담았다. result에서 user_id를 닉네임으로 바꾸기 위해 replace를 사용하였다.


### +) 다른 사람 풀이
다른 사람의 풀이를 참고해 다시 풀어봄.
```python
def solution(record):
    printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
    answer = []
    dict = {}
        
    for rec in record:
        r = rec.split(' ')
        if r[0] in ['Enter', 'Change']:
            dict[r[1]] = r[2]
    
    for rec in record:
        r = rec.split(' ')
        if r[0] != 'Change':
            answer.append(dict[r[1]]+printer[r[0]])
    
    return answer
```
딕셔너리를 활용해서 푸는 방법이 매우 간결했다. 또한 split()할 경우 여러개의 요소가 반환되는데 이 때 각 요소별로 변수를 지정하지 말고 `r = rec.split(' ')` 간단하게 변수를 하나만 지정하여 인덱싱으로 코딩하면 깔끔하다.
