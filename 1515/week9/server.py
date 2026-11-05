from http.server import HTTPServer, BaseHTTPRequestHandler

# TODO: Create a function to handle the request
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello from BCIT")

server = HTTPServer(("localhost", 4000), Handler)
server.serve_forever()
