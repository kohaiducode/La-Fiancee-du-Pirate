import http.server
import socketserver
import os
import sys

PORT = 8080
DIRECTORY = "dist"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def run_server():
    if not os.path.exists(DIRECTORY):
        print(f"Error: directory '{DIRECTORY}' does not exist. Please run compile/build first.")
        sys.exit(1)
        
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Local server started at: http://localhost:{PORT}")
        print("Press Ctrl+C to stop.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nStopping server.")
            sys.exit(0)

if __name__ == "__main__":
    run_server()
