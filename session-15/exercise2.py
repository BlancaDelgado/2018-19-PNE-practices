# Echo server with forms

import http.server
import socketserver
import termcolor

PORT = 8083


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        # PRINT REQUEST LINE
        termcolor.cprint(self.requestline, 'green')

        # READ FILE DEPENDING ON PATH
        if self.path == '/' or 'favicon' in self.path:
            f200 = open('exercise2_form.html', 'r')
            contents = f200.read()

        elif 'echoserver' in self.path:

            # DIVIDE COMMANDS OF PATH
            if 'chk' in self.path:
                echo_input = self.path.split('&')[0]  # select echo input
                echo = echo_input.split('=')[1].upper()  # capitalize echo

            else:
                echo = self.path.replace('+', ' ').split('=')[1]

            contents = """
            <html lang="en" dir="ltr">
    
            <head>
                <meta charset="utf-8">
                <title>Echo</title>
            </head>
            
            <body>
                <h1>ECHO:</h1>
                <p>{echo}</p>
                <br><br>
                
                <a href='/'>[Main page]</a>
            </body>
            
            </html>
            """.format(echo=echo)

        else:
            f0 = open('exercise1_error.html', 'r')
            contents = f0.read()

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
