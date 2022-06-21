### 문제
보호소에 돌아가신 할머니가 기르던 개를 찾는 사람이 찾아왔습니다. 이 사람이 말하길 할머니가 기르던 개는 이름에 'el'이 들어간다고 합니다. 동물 보호소에 들어온 동물 이름 중, 이름에 "EL"이 들어가는 개의 아이디와 이름을 조회하는 SQL문을 작성해주세요. 이때 결과는 이름 순으로 조회해주세요. 단, 이름의 대소문자는 구분하지 않습니다. [`자세히 보기`](https://programmers.co.kr/learn/courses/30/lessons/59047)  

### 나의 풀이
```sql
SELECT animal_id, name
 from animal_ins
 where lower(name) like '%el%'
  and animal_type = 'Dog'
 order by name asc;
```

### 설명
where절에 like+와일드카드 문자를 사용하여 이름에 el이 들어가는 동물을 조회, 이때 이름은 대소문자가 섞여있으므로 대문자 또는 소문자로 통일시켜 검색해야함. 또한 개만 조회해야 하므로 animal_type조건을 걸어주었음.