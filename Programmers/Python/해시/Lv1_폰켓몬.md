### 문제
N마리 폰켓몬의 종류 번호가 담긴 배열 nums가 매개변수로 주어질 때, N/2마리의 폰켓몬을 선택하는 방법 중, 가장 많은 종류의 폰켓몬을 선택하는 방법을 찾아, 그때의 폰켓몬 종류 번호의 개수를 return 하도록 solution 함수를 완성해주세요.  
[`자세히 보기`](https://school.programmers.co.kr/learn/courses/30/lessons/1845?language=python3)
<br>
<br>
### 나의 풀이  
```python
def solution(nums):
    cnt = len(set(nums))
    halfnum = len(nums) / 2
    
    if halfnum <= cnt :
        return halfnum
    else:
        return cnt
```
<br>

### 설명
if조건문을 사용해 풀이하였다. 하지만, min()을 사용하면 더 간결하게 풀 수 있다.
