### 문제
스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.  

1. 속한 노래가 많이 재생된 장르를 먼저 수록합니다.  
2. 장르 내에서 많이 재생된 노래를 먼저 수록합니다.  
3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.  

노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.  
[`자세히 보기`](https://programmers.co.kr/learn/courses/30/lessons/42579)

### 나의 풀이
```pyhon
def solution(genres, plays):
    import numpy as np
    plays = np.array(plays)
    
    dict_plays = {i:[] for i in list(set(genres))}
    for i,k in zip(genres, plays):
        dict_plays[i].append(k)

    lst = sorted(dict_plays, key = lambda x: sum(dict_plays[x]), reverse = True)
    answer = []
    for i in lst:
        song = sorted(dict_plays[i], reverse = True)
        for s in song[:2]:
            idx = int(np.where(plays == s)[0][0])
            answer.append(idx)
            plays[idx] = -1

    return answer
```

### 설명
sort()를 사용하여 딕셔너리 value를 기준으로 키를 정렬하는 것이 관건이었다. 특정 조건에 맞는 값의 인덱스를 뽑기 위해 넘파이를 사용하였다.