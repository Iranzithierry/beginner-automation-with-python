import http.server
import socketserver

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

# Create the server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Server started at localhost:{}".format(PORT))
    httpd.serve_forever()
