### 문제
ANIMAL_INS 테이블에 등록된 모든 레코드에 대해, 각 동물의 아이디와 이름, 들어온 날짜를 조회하는 SQL문을 작성해주세요. 이때 결과는 아이디 순으로 조회해야 합니다. [`자세히 보기`](https://programmers.co.kr/learn/courses/30/lessons/59414)

### 나의 풀이
```sql
SELECT animal_id, name, to_char(datetime,'RRRR-MM-DD')
 from animal_ins
 order by 1 asc;
```

### 설명
to_char를 사용하여 날짜형 데이터를 문자형으로 변환하였음.