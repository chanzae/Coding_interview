### 문제
동물 보호소에 가장 먼저 들어온 동물의 이름을 조회하는 SQL 문을 작성해주세요. [`자세히 보기`](https://programmers.co.kr/learn/courses/30/lessons/59405)  

### 나의 풀이
```sql
SELECT name
 from animal_ins
 order by datetime fetch first 1 rows only;
```

### 설명
가장 먼저 들어온 동물의 이름을 조회하는데 order by 절에 `fetch first 1 rows only`를 사용해 정렬하여 첫번째 행만 출력하도록 검색함. 'fetch first' 기능은 오라클에서만 사용가능하므로 mysql에서는 서브쿼리를 사용하거나 `order by datetime limit 1` 사용하면 됨.