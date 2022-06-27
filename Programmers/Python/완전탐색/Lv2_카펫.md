### 문제
Leo는 카펫을 사러 갔다가 아래 그림과 같이 중앙에는 노란색으로 칠해져 있고 테두리 1줄은 갈색으로 칠해져 있는 격자 모양 카펫을 봤습니다.  

Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.  
[`자세히 보기`](https://programmers.co.kr/learn/courses/30/lessons/42842)

### 나의 풀이
```python
def solution(brown, yellow):
    import math
    
    x = yellow + brown
    result =[]
    for i in range(2, int(x//2),+1):
        if (x%i == 0) & (x//i >= i) :
            if ((x//i)-2)*(i-2) == yellow:
                answer = [x//i,i]
    return answer
```

### 설명
brown과 yellow 갯수의 합은 카펫의 가로길이x세로길이와 같다. 따라서 brown과 yellow 갯수 합의 약수를 구했고, 약수 중 yellow가 카펫 가운데 들어갈 수 있는 수를 구하였다.