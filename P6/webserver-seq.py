# Web server for performing operations on a sequence

# PREDESIGNED OPERATIONS ON SEQUENCES
from P1.Seq import Seq

# LIBRARIES FOR WEB SERVERS
import http.server
import socketserver
import termcolor

PORT = 8003


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        # Print request line
        termcolor.cprint(self.requestline, 'green')

        # Select file
        request = self.requestline.split(" ")[1]

        if request == "/":
            filename = 'main.html'


# -- main program

with socketserver.TCPServer(("", PORT), TestHandler) as httpd:
    print("Serving at PORT: {}".format(PORT))

    try:
        httpd.serve_forever()

    except KeyboardInterrupt:
        print("Exit by user.")
        httpd.server_close()







