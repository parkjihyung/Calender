# My Calendar Project

사용자 별 스케쥴을 관리하는 시스템을 구축한다.



## 1. Main features

* 사용자 로그인 / 로그아웃  (Django Admin Login 사용)
* 사용자 별 스케쥴 관리
  * FullCalendar Library 활용하여 스케쥴 등록
  * 스케쥴 등록, 수정, 삭제
* 사용자 관리자 (Django Admin User 사용)
  * 사용자 등록, 수정, 삭제



## 2. Models

### Calendar

| Id          | Name            | Type     | Lengh | Default |
| ----------- | --------------- | -------- | ----- | ----- |
| userId     | 사용자 아이디   | IntegerField |     | 0 |
| title       | 스케쥴 제목 | CharField | 100 |  |
| start  | 시작일시        | DateTime |       |       |
| end   | 종료일시        | DateTime |       |       |
| allDay     | 종일 여부       | Boolean  |       | True |

* userId는 Django admin user Model의 PK(Primery Key)를 저장한다.



## Reference

* [명준 MJ Python & Django Tutorial 강좌](https://www.youtube.com/playlist?list=PLi4xPOplIq7d1vDdLBAvS5PmQR-p6KwUz) 
* https://djangoproject.com
* [Django 회원가입, 로그인, 로그아웃 구현하기](https://ssungkang.tistory.com/entry/Django-10-%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85%EB%A1%9C%EA%B7%B8%EC%9D%B8%EB%A1%9C%EA%B7%B8%EC%95%84%EC%9B%83-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0)
* [Django JSON Request, Response 구현하기](https://eunjin3786.tistory.com/133)
* https://fullcalendar.io/

