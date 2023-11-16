from http.server import HTTPServer, BaseHTTPRequestHandler
from threading import Thread


class Test(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        filename = 'index.html'
        with open(filename, 'rb') as file:
            self.wfile.write(file.read())
        # self.wfile.write(b'Hello, world!')

    def do_POST(self):
        pass


server = HTTPServer(('localhost', 5353), Test)
server_thread = Thread(target=server.serve_forever())
server_thread.start()