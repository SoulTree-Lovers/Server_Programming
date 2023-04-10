#!/usr/bin/env python3
#
# The *hello server* is an HTTP server that responds to a GET request by
# sending back a friendly greeting.  Run this program in your terminal and
# access the server at http://localhost:8000 in your browser.

from http.server import HTTPServer, BaseHTTPRequestHandler


class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 1. response의 결과로 status line 정보 입력
        # First, send a 200 OK response.
        self.send_response(200)

        # text/plain: 일반 문자로 보냄
        # text/html: html 문서로 보냄
        # content-type: 데이터 타입을 해석할 때 사용

        # 2. Then send headers. (html 문서 형식으로 보냄)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        
        # 3. response header 입력 종료
        self.end_headers()

        # Now, write the response body.
        # self.wfile.write 메소드는 bytes data만 전송
        # encode() : string data를 utf-8 방식의 bytes로 변환하는 것을 말함
        #            (한글, 일본어, 중국어 등의 문자를 utf-8 방식의 bytes 체제로 변환)
        # encoding 방식 : utf-8(1~3 bytes), utf-16, ISO-8859 등,
        #                 python은 utf-8이 default encoding 방식임
        # encode의 목적은 web은 국제 표준이므로 browser와 web server가 영문이외에
        #                모든 language를 지원하기 위해서임
        # encode 예 : len('안녕') => 2 출력, len('안녕'.encode()) => 6 출력
        # cf : decode() : encode의 반대로, bytes data를 문자열로 변환
        
        # 4. response의 본문 data 입력
        self.wfile.write("<h1>Hello, HTTP!</h1>\n".encode())

if __name__ == '__main__':
    # ''는 모든 IP adress에 대해 수신한다는 뜻.
    # 8000은 포트 번호이다.
    server_address = ('', 8000)  # Serve on all addresses, port 8000. 
    
    # server_address에 HelloHandler를 사용한다.
    # HelloHandler의 내용을 수정하여 콘텐츠 생성
    httpd = HTTPServer(server_address, HelloHandler)
    

    httpd.serve_forever()

# 실행 후 크롬에서 localhost:8000 을 입력하면 Hello, HTTP! 출력

# 아래 두 줄은 터미널에 출력되는데, 
# 127.0.0.1 - - [30/Mar/2023 09:50:52] "GET / HTTP/1.1" 200 - 
# 127.0.0.1 - - [30/Mar/2023 09:50:52] "GET /favicon.ico HTTP/1.1" 200 - 아이콘 설정 기능?