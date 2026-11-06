from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        if self.path == "/":
            html = Path("index.html").read_text()
            actualConversion = 'hi'
            html.replace("{ TEMPERATURE_CONVERSION_HERE }", actualConversion)
            self.wfile.write(html.encode())
        elif self.path == "/contact":
            html = Path("contact.html").read_text()
            self.wfile.write(html.encode())

server = HTTPServer(("localhost", 4000), Handler)
server.serve_forever()
