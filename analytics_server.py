
import http.server
import socketserver

PORT = 9999

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/v2_dashboard.html'
        return super().do_GET()

try:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Analytics server running on port {PORT}")
        httpd.serve_forever()
except KeyboardInterrupt:
    print("Server stopped")
