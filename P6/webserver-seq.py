# Web server for performing operations on a sequence

# PREDESIGNED OPERATIONS ON SEQUENCES
from P1.Seq import Seq

# LIBRARIES FOR WEB SERVERS
import http.server
import socketserver
import termcolor

PORT = 8014


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        def response(client_msg):
            # MAKE A LIST WITH THE ELEMENTS OF THE MESSAGE
            client_msg = client_msg.replace('GET /myserver?', '').replace(' HTTP/1.1', '').split("&")

            if len(client_msg) == 4 or len(client_msg) == 3:

                # MAKE A DOUBLE LIST OF THE MESSAGE (TYPE/COMMAND)
                queries = []
                for i in client_msg:
                    query = i.split('=')
                    command_type = query[0]
                    command = query[1]

                    i = [command_type, command]
                    queries.append(i)

                # ATTEND ALL QUERIES
                for pair in queries:

                    if pair[0] == 'msg':
                        seq = pair[1].upper()
                        Seq_Class = Seq(seq)

                        for i in seq:
                            if i not in ['ACGT']:
                                error = """
                                        <html lang="en" dir="ltr">
                                            <head>
                                                <meta charset="UTF-8">
                                                <title>Error Page<title>
                                            </head>

                                            <body>
                                                <br><h3>ERROR PAGE:</h3>
                                                <p>Sorry, your sequence could not be identified.</p>
                                            </body>

                                        </html>

                                        """
                                return error



                        return error



                print(queries)



            else:
                pass


        # PRINT REQUEST LINE FROM CLIENT
        termcolor.cprint(self.requestline, 'green')

        # SELECT FILE ACCORDING TO REQUEST
        # request = self.requestline.split(" ")[1]

        filename = 'main.html'

        # READ SELECTED FILE
        file = open(filename, 'r')
        contents = file.read()

        # PRINT RESPONSE MESSAGE ON TERMINAL
        self.send_response(200)  # OK
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content_Length', len(str.encode(contents)))
        self.end_headers()

        # TAKE CARE OF RESPONSE
        response(self.requestline)

        contents = response(self.requestline)
        # Send body of response message to client
        self.wfile.write(str.encode(contents))


# -- main program

with socketserver.TCPServer(("", PORT), TestHandler) as httpd:
    print("Serving at PORT: {}".format(PORT))

    try:
        httpd.serve_forever()

    except KeyboardInterrupt:
        print("Exit by user.")
        httpd.server_close()
