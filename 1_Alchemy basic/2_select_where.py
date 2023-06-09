# 에이전트 라이브러리 설치 후 불러오기
import pymysql

# MySQL Connection 연결
conn = pymysql.connect(host='localhost', user='root', password='root',
                       db='madang', charset='utf8')

# Connection 으로부터 Dictionary Cursor 생성
# pymysql.cursors.DictCursor는 curs가 dictionary based cursor라는 의미임
# 결과값이 딕셔너리 형태로 나옴! (원래는 튜플 형태)
curs = conn.cursor(pymysql.cursors.DictCursor) # 데이터를 이터레이터 형식으로 받기

# SQL문 실행, %s : 문자열이든 숫자이든 %s 사용
sql = "select * from book where publisher=%s and price>=%s"
curs.execute(sql, ('이상미디어', 13000))

# 데이타 Fetch
rows = curs.fetchall()
# print(rows) # rows: 리스트에 딕셔너리 인자들이 여러 개 들어있는 형태

for row in rows:
    print(row)
    # 출력 : {'bookid': 7, 'bookname': '야구의 추억', 'publisher': '이상미디어', 'price': 20000}
    print(row['bookid'], row['bookname'], row['publisher'], row['price'])
    # 7 야구의 추억 이상미디어 20000

# Connection 닫기
conn.close()