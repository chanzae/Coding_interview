### 문제
수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.  

1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...  
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...  
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...  

1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.  
[`자세히 보기`](https://programmers.co.kr/learn/courses/30/lessons/42840)
  
  
### 나의 풀이
```python
def solution(answers):
    import numpy as np
    
    num = len(answers)
    dict = {1: [1,2,3,4,5],
            2: [2,1,2,3,2,4,2,5],
            3: [3,3,1,1,2,2,4,4,5,5]}
    
    cnt = []
    for k in dict.values():      
        question = k * divmod(num,len(k))[0] + k[:divmod(num,len(k))[1]]
        answers = answers * divmod(num, len(answers))[0] + k[:divmod(num,len(answers))[1]]
        correct = sum(np.array(question) == np.array(answers))
        cnt.append(correct)
    
    result = []
    for k,i in enumerate(cnt == max(cnt)):
        if i:
            result.append(k+1)
    return result
```

### 설명
딕셔너리를 사용하여 수포자1,2,3의 답안을 생성하였고, divmod()를 사용하여 매개변수로 입력되는 answers의 갯수만큼 답안을 생성하여 question 변수에 담았다. 이어 question과 answers를 리스트에서 numpy array형태로 변환하여 sum()을 통해 True의 수를 반환받았다. 문제를 가장 많이 맞힌 사람(True의 수가 가장 많은 사람)의 번호를 출력할 수 있도록 for문과 enumerate를 사용하였다.
