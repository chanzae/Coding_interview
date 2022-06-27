### 문제
한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.  

각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.  
[`자세히 보기`](https://programmers.co.kr/learn/courses/30/lessons/42839)

### 나의 풀이
```python
def solution(numbers):
    from itertools import combinations,permutations
    import math
    
    num_list = []
    str_numbers = list(map(str, numbers))
    for i in range(1,len(str_numbers)+1):
        prod_list = list(set(permutations(str_numbers, r = i)))
        filter_list = list(filter(lambda x: x[0] != '0', map(lambda x: ''.join(x), prod_list)))
        for f in filter_list:
            fsqrt = int(math.sqrt(int(f)))
            cnt = 0
            for k in range(2, fsqrt+1):
                if int(f)%k == 0:
                    cnt += 1
            if (cnt == 0) & (f != '1'):
                num_list.append(f)
                    
    return len(num_list)
```

### 설명
numbers에서 제공되는 숫자로 조합을 만들기 위해 str로 변환하여 permutations을 사용하였다. 이후 소수를 찾기 위해 2부터 제곱근까지 for문을 돌려 나누어지지 않는 숫자를 선별하였다.
     