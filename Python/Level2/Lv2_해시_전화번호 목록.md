### 문제
전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.  
[`자세히 보기`](https://programmers.co.kr/learn/courses/30/lessons/42577)

### 나의 풀이
```python
# 풀이1
def solution(phone_book):
    pb = sorted(phone_book, key = lambda x:len(x))
    dict = {p:0 for p in pb}
    
    for i in pb:
        dict[i] = list(map((lambda x:x[:len(i)] if (x!=i) & (len(x) >= len(i)) else -1), pb))
        if i in dict[i]:
            return False
    return True
```
```python
# 풀이2
def solution(phone_book):
    pb = sorted(phone_book, key = lambda x:len(x))
    
    for i,k in enumerate(pb[:-1]):
        for num in pb[i+1:]:
            if num.startswith(k):
                return False
    return True
```
```python
#풀이3 - 통과
def solution(phone_book):
    pb = sorted(phone_book)

    for i,k in enumerate(pb[:-1]):
        if k == pb[i+1][:len(k)]:
            return False
            
    return True
```

### 설명
**풀이1** : 딕셔너리를 사용해 접두사가 되는 번호는 키로 설정, 이 키와 길이가 같게 전화번호를 슬라이싱하여 값 리스트로 넣었다. 이를 for문을 사용, 같은 값이 있을 경우 false가 출력되도록 하였다.  
정확성 테스트에서는 모두 통과를 받았으나 효율성 테스트에서 실패((2/4)하고 있다.  

**풀이2**: startswith()를 사용해서 접두사인 번호를 찾았다. 하지만 이 또한 정확성 테스트에서는 모두 통과를 받았으나 효율성 테스트에서 실패(2/4)하고 있다.  

**풀이3**: 이 문제의 키는 sort()정렬을 제대로 이해하고 있느냐를 묻는 문제였다. 앞선 풀이에서는 문자열의 length를 기준으로 정렬했다. 이 경우 모든 문자열을 비교해야하는 번거로움이 있다. sort()정렬 default는 오름차순으로 문자를 비교할 때는 길이에 상관없이 문자열의 시작부터 오름차순으로 정렬한다.
이 문제에서 전화번호는 string형식으로 주어지고 있다. 따라서 오름차순 정렬을 해주어 앞에서부터 2개의 전화번호만 비교해주면 된다.
```python
# 오름차순 정렬 예시
# 리스트 요소가 숫자일 때
sort_number = [ 1, 20, 5, 2, 100]
sort_number.sort() # [1, 2, 5, 20, 100]

# 리스트 요소가 문자일 때
sort_str = [ '1', '20', '5', '2', '100']
sort_str.sort() #['1', '100', '2', '20', '5']
```


 
