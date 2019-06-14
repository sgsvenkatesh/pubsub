from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write(b'Hello, world!')

    def do_POST(self):
        print("post handling here")

        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        message = self.rfile.read(content_length).decode("utf-8")  # <--- Gets the data itself
        self._set_headers()

        # send the message back
        self._set_headers()

        file = open("messages.txt", "w")
        file.write(message)
        file.close()


httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
print("Server listening at port 8000")
httpd.serve_forever()