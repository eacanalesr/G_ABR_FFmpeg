from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

HOST = "0.0.0.0"
PORT = 8080

# Directory path
DIRECTORY = "/home/gstreamer/1_ABR_FFMPEG/output"

os.chdir(DIRECTORY)

server = HTTPServer((HOST, PORT), SimpleHTTPRequestHandler)

print(f"Serving {DIRECTORY} on port {PORT}")

server.serve_forever()
