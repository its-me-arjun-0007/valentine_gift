import http.server
import socketserver
import os

PORT = 8080
DIRECTORY = "."

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

print(f"❤️  Valentine Site Running at: http://localhost:{PORT}")
print("Press CTRL+C to stop.")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()

