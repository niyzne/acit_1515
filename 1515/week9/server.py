from http.server import HTTPServer, BaseHTTPRequestHandler

# TODO: Create a function to handle the request
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        # self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        # self.wfile.write(b"Hello from BCIT")
        self.wfile.write(b"<h1>Hello from BCIT</h1>")

server = HTTPServer(("localhost", 4000), Handler)
server.serve_forever()
