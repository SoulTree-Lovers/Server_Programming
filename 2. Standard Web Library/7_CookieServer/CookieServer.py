#!/usr/bin/env python3
#
# An HTTP server that remembers your name (in a cookie)

from http.server import HTTPServer, BaseHTTPRequestHandler
from http import cookies
from urllib.parse import parse_qs
from html import escape as html_escape

# http protocol: stateless (상태관리를 하지 않음(못함))

# 통신 전용 선: 기업에서 구매 (한 번 로그인하면 24시간 접속이 끊기지 않음.) -> 서버에서 관리할 수 있음.
# 인터넷 network(http protocol): 돈을 내지 않음. 모든 사람이 공용으로 쓰기 때문에 누가 독점할 수 없음. -> 서버에서 관리할 수 없음.

form = '''<!DOCTYPE html>
<title>I Remember You</title>
<p>
{}
<p>
<form method="POST">
<label>What's your name again?
<input type="text" name="yourname">
</label>
<br>
<button type="submit">Tell me!</button>
</form>
'''


class NameHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # How long was the post data?
        length = int(self.headers.get('Content-length', 0))

        # Read and parse the post data
        data = self.rfile.read(length).decode()

        # 여러 개의 yourname 중 첫 번째꺼 가져오기
        yourname = parse_qs(data)["yourname"][0]

        # Create cookie.
        # 쿠키는 수정할 수 없고 수정하려면 그냥 새로 생성하면 된다.
        c = cookies.SimpleCookie()  
        c['yourname'] = yourname    
        c['yourname']['domain'] = 'localhost'
        c['yourname']['max-age'] = 60

        # Send a 303 back to the root page, with a cookie!
        self.send_response(303)  # redirect via GET
        self.send_header('Location', '/')
        self.send_header('Set-Cookie', c['yourname'].OutputString())
        self.end_headers()

    def do_GET(self):
        # Default message if we don't know a name.
        message = "I don't know you yet!"

        # Look for a cookie in the request.
        if 'cookie' in self.headers:
            try:
                # Extract and decode the cookie.
                c = cookies.SimpleCookie(self.headers['cookie'])
                name = c['yourname'].value

                # Craft a message, escaping any HTML special chars in name.
                message = "Hey there, " + html_escape(name)
            except (KeyError, cookies.CookieError) as e:
                message = "I'm not sure who you are!"
                print(e)

        # First, send a 200 OK response.
        self.send_response(200)

        # Then send headers.
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        # Send the form with the message in it.
        mesg = form.format(message)
        self.wfile.write(mesg.encode())


if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, NameHandler)
    httpd.serve_forever()
