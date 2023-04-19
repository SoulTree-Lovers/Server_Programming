#!/usr/bin/env python3
#
# An HTTP server that's a message board.
# PRG(Post-Redirect-Get) design pattern : HTTP application의 매우 자주 사용되는 패턴임
# 실행 순서
# 1. localhost:8000/ 접속하면 do_GET을 call => html form내용이 화면에 보여짐
#    ==> web browser에서 server를 call할 때 method의 default값은 GET 방식임
# 2. textarea에 데이터 입력하고 submit button누르면 do_POST가 불러지고,
#    textarea에서 입력된 데이터가 memory에 저장됨 => redirect (303)을 통해 다시 do_GET이 불리어짐
#    ==> redirect할 때 default method가 GET이기 때문에 do_GET call함
# 3. do_GET이 불려지면 textarea에서 입력되고 submit된 데이터 리스트가 보여짐

# 순서 설명
# 1. Get: login 입력 화면을 나타냄.
# 2. login 입력화면에서 id, pw 입력 -> 전송 버튼 누르면 POST 방식으로 전달
# 3. 서버에서는 id, pw(DBMS table)를 체크하고 
#    -> 맞다면 main 화면으로 GET 방식으로 redirect
#    -> 틀리다면 틀렸다는 내용을 포함한 login 입력화면이 redirect를 사용하여 다시 display됨




from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs

memory = []

form = '''<!DOCTYPE html>
  <title>Message Board</title>
  <form method="POST">
    <textarea name="message"></textarea>
    <br>
    <button type="submit">Post it!</button>
  </form>
  <pre>
{}
  </pre>
'''


class MessageHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # How long was the message?
        length = int(self.headers.get('Content-length', 0))

        # Read and parse the message
        data = self.rfile.read(length).decode()
        message = parse_qs(data)["message"][0]

        # Escape HTML tags in the message so users can't break world+dog.
        # <를 &lt로 처리하여 html tag로 인식하지 않음. -> 해킹 방지를 위함.
        message = message.replace("<", "&lt;") 

        # Store it in memory. memory 변수의 data type : list
        memory.append(message)

        # Send a 303 back to the root page
        # 303의 의미 : redirect via GET,
        # 1. server가 303을 인식하면, client인 web browser로 보내는 것이 아니라
        #    Location으로 지정된 server 주소로 다시 재전송됨
        # 2. redirect할 때는 response body에 데이터를 넣지 않음
        self.send_response(303) # do_Get을 다시 실행

        # Location이 '/'라는 의미는 root 주소를 말함, 즉 localhost:8000/을 말함
        self.send_header('Location', '/')
        self.end_headers()

    def do_GET(self):
        # First, send a 200 OK response.
        self.send_response(200)

        # Then send headers.
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        # Send the form with the messages in it.
        # format 메소드는 string instance안에 있는 것으로
        # form 문자열 안에 { } 자리에, "\n".join(memory)결과값이 들어감
        mesg = form.format("\n".join(memory))
        self.wfile.write(mesg.encode())

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MessageHandler)
    httpd.serve_forever()
