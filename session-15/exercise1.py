# Echo server with forms

import http.server
import socketserver
import termcolor

PORT = 8080

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        # PRINT REQUEST LINE
        termcolor.cprint(self.requestline, 'green')

        # READ FILE
        f = open('exercise1_form.html', 'r')
        contents = f.read()

        # PRINT RESPONSE MESSAGE
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()

        # SEND BODY OF RESPONSE MESSAGE
        self.wfile.write(str.encode(contents))


# -- Main program

with socketserver.TCPServer(('', PORT), TestHandler) as httpd:
    print('Serving at PORT: {}'.format(PORT))

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Exit by user.')
        httpd.server_close()


