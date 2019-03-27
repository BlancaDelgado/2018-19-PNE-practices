# Server for buttons

import http.server
import socketserver
import termcolor

PORT = 8000

class TestHandler(http.server.BaseHTTPRequestHandler):  # whatever classed derived from the HTTP library

    def do_GET(self):  # DO NOT CHANGE NAME HERE

        # -- Printing the request line
        termcolor.cprint(self.requestline, 'green')

        # -- Read file
        f = open("form2.html", 'r')
        contents = f.read()

        # -- Print response message
        self.send_response(200)  # code when everything is okey
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()

        # -- Sending the body of the response message
        self.wfile.write(str.encode(contents))



# -- Main program

with socketserver.TCPServer(("", PORT), TestHandler) as httpd:  # if there is no IP, it will take the local one
    print("Serving at PORT: {}".format(PORT))

    try:
        httpd.serve_forever()

    except KeyboardInterrupt:
        httpd.server_close()
