### 문제
신입사원 무지는 게시판 불량 이용자를 신고하고 처리 결과를 메일로 발송하는 시스템을 개발하려 합니다.  

이용자의 ID가 담긴 문자열 배열 id_list, 각 이용자가 신고한 이용자의 ID 정보가 담긴 문자열 배열 report, 정지 기준이 되는 신고 횟수 k가 매개변수로 주어질 때, 각 유저별로 처리 결과 메일을 받은 횟수를 배열에 담아 return 하도록 solution 함수를 완성해주세요.  
[`자세히 보기`](https://programmers.co.kr/learn/courses/30/lessons/92334)

### 나의 풀이
```python
def solution(id_list, report, k):
    dict = {x: 0 for x in id_list}
    report = list(set(report))
    answer = [0] * len(id_list)
    
    for r in report:
        dict[r.split()[1]] += 1
        
    for r in report:
        if dict[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1
        
    return answer
```

### 설명
딕셔너리를 사용해서 신고당한 유저와 신고당한 횟수를 카운팅하였다. 리스트의 값이 주어졌을때, 값의 인덱스를 찾는게 관건이었다.