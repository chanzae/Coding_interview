### 문제
점심시간에 도둑이 들어, 일부 학생이 체육복을 도난당했습니다. 다행히 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주려 합니다. 학생들의 번호는 체격 순으로 매겨져 있어, 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다. 예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다. 체육복이 없으면 수업을 들을 수 없기 때문에 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 합니다.  

전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때, 체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.  
[`자세히 보기`](https://programmers.co.kr/learn/courses/30/lessons/42862?language=python3)

### 나의풀이
```python
def solution(n, lost, reserve):
    lst = [1]*n
    for l in lost:
        lst[l-1] -= 1
    for r in reserve:
        lst[r-1] += 1
    
    for idx in range(len(lst)-1):
        nex = lst[idx+1]
        curr = lst[idx]
        if (curr==2)&(nex==0):
            lst[idx] = 1
            lst[idx+1] = 1
        elif (curr==0)&(nex==2):
            lst[idx] = 1
            lst[idx+1] = 1
            
    answer = len(lst) - lst.count(0)
    return answer
```

### 설명
리스트에서 요소 2개를 뽑아 값을 비교한 후 리스트 인덱스를 활용해 리스트 요소 값을 변경하였다.
