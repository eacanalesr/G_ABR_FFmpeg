from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

HOST = "0.0.0.0"
PORT = 8080

# Use the same output path for the DIRECTOTY as you used for the abr-basic.sh file 
DIRECTORY = "path where the HLS chunks have been stored"

os.chdir(DIRECTORY)

server = HTTPServer((HOST, PORT), SimpleHTTPRequestHandler)

print(f"Serving {DIRECTORY} on port {PORT}")

server.serve_forever()
