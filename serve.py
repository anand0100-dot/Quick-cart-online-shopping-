from http.server import HTTPServer
from http.server import SimpleHTTPRequestHandler

PORT = 8080

server = HTTPServer(("localhost", PORT), SimpleHTTPRequestHandler)

print("=" * 50)
print("QuickCart Server Started")
print(f"Open Browser : http://localhost:{PORT}")
print("=" * 50)

server.serve_forever()