# Web server with index and access to blue, pink and error using http module

import socketserver
import termcolor  # allow terminal colors
import http.server  # module for http connections

# BASIC CONFIGURATIONS

PORT = 8081  # server's port


class TestHandler(http.server.BaseHTTPRequestHandler):


    def do_GET(self):
        """
        Called whenever client calls GET method.
        :return:
        """

        # RECEIVE AND PRINT REQUEST LINE
        termcolor.cprint(self.requestline, 'green')

        # SEND RESPOND MESSAGE (HTML PAGE)
        requests = self.requestline.split(' ')
        resource = requests[1]

        # Page options
        if resource == '/':
            filename = 'index.html'

        elif resource == '/blue':
            filename = 'blue.html'

        elif resource == '/green':
            filename = 'green.html'

        elif resource == '/pink':
            filename = 'pink.html'

        else:
            filename = 'error.html'

        with open(filename, 'r') as file:
            contents = file.read()
            file.close()

        # Send ok status
        self.send_response(200)

        # Define type and length of header
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()

        self.wfile.write(str.encode(contents))
        return


# -- Main program

Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print()
        print("Stopped by user.")
        httpd.server_close()

print()
print("Server stopped.")
