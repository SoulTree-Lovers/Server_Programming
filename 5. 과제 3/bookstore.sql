-- 단축키
-- 1줄 실행: command + enter
-- 여러 줄 실행: shift + command + enter

CREATE DATABASE bookstore default CHARACTER SET UTF8;

USE bookstore;



select * from bookstore;
select * from bookitem;


-- 데이터 삽입
-- bookstore
INSERT INTO bookstore VALUES(1, '교보문고');
INSERT INTO bookstore VALUES(2, '영풍문고');
INSERT INTO bookstore VALUES(3, '알라딘 중고서점');


-- bookitem
INSERT INTO bookitem VALUES('축구의 역사', 1, 7000, 1);
INSERT INTO bookitem VALUES('축구아는 여자', 2, 13000, 1);
INSERT INTO bookitem VALUES('축구의 이해', 3, 22000, 1);
INSERT INTO bookitem VALUES('골프 바이블', 4, 35000, 2);
INSERT INTO bookitem VALUES('피겨 교본', 5, 8000, 2);
INSERT INTO bookitem VALUES('역도 단계별기술', 6, 6000, 2);
INSERT INTO bookitem VALUES('야구의 추억', 7, 20000, 3);
INSERT INTO bookitem VALUES('야구를 부탁해', 8, 13000, 3);
INSERT INTO bookitem VALUES('올림픽 이야기', 9, 7500, 3);
INSERT INTO bookitem VALUES('Olympic Champions', 10, 13000, 3);



COMMIT;
