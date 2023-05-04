# import cx_oracle: oracle DBMS를 사용하는 경우 라이브러리
import pymysql # MySQL DBMS를 사용하는 경우에 전용 라이브러리

# MySQL Connection 연결
# connect 명령어를 정상적으로 실행이 되면, madang database와 접속한 상태가 됨.
conn = pymysql.connect(host='localhost', user='root', password='root',
                       db='madang', charset='utf8')

# Connection 으로부터 Cursor 생성
# curs : array based cursor (default)
curs = conn.cursor()

# SQL문 실행
sql = "select * from customer"

# execute(): MySQL DBMS와 통신하여 실행 결과값을 curs에 저장한다.
curs.execute(sql)

# 데이타 Fetch
rows = curs.fetchall()

# 실행 결과는 2차원 튜플로 나온다.
print(rows)  # 전체 rows

# 한 행씩 출력하기
# print(rows[0])  # 첫번째 row: (1, '박지성', '영국 맨체스타', '000-5000-0001')
# print(rows[1])  # 두번째 row: (2, '김연아', '대한민국 서울', '000-6000-0001')


# Connection 닫기
conn.close()