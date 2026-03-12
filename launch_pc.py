import http.server
import socketserver
import webbrowser
import os

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

print(f"Serving 3D Tank Game at http://localhost:{PORT}")
webbrowser.open(f"http://localhost:{PORT}")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
