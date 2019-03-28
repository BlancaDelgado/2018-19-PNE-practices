# Web server for performing operations on a sequence

import http.server
import socketserver
import termcolor

from P1.Seq import Seq

PORT = 8002

def attend_seq(seq):
    """
    Checks sequence submitted to see if it is valid or not.
    If it is valid, it capitalizes it.
    :param seq: sequence submitted in form
    :return: False ---> if not valid
    :return: seq------> if valid
    """

    # CHECK FOR EVERY CHARACTER IN POSSIBLE ACGT
    for i in seq.upper():
        if i not in 'ACGT':
            return False

    # IF ALL OF THEM WORK OUT
    seq = seq.upper()
    return seq


class SeqHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        # PRINT REQUEST LINE
        termcolor.cprint(self.requestline, 'green')

        # READ FILE DEPENDING ON PATH
        # If we are starting program
        if self.path == '/' or 'favicon' in self.path:
            f_200 = open('main.html', 'r')
            contents = f_200.read()

        # If sequence is sent
        elif 'seq' in self.path:

            path = self.path.replace('/seq?', '').replace(' HTTP/1.1', '')
            inputs = path.split('&')

            input_seq = inputs[0].split('=')[1]

            # CHECK SEQUENCE SUBMITTED
            seq = attend_seq(input_seq)

            if not seq:  # if there IS NOT sequence, error
                f_error = open('error.html', 'r')
                contents = f_error.read()

            # ANALYZE INPUTS
            else:  # if there IS sequence, continue with inputs

                SeqClass = Seq(seq)

                for i in inputs:
                    i_type = i[0]
                    i_value = i[1]

                    # 1.- CHECK LENGTH
                    len = ""  # in case it is not selected
                    if i_type == 'chk':
                        len = SeqClass.len()
                        len = "<p>· Sequence length: {len}<p>".format(len=len)

                    # 2.- CHECK OPERATIONS
                    count = False
                    perc = False
                    elif i_type == 'operation':
                        if i_value == 'count':
                            count = True
                        elif i_value == 'perc':
                            perc = True

                    # 3.- CHECK BASE
                    elif i_type == 'base':
                        base = i_value

                # CALCULATE OPERATIONS
                if count:
                    count = SeqClass.count(base)
                    count = "<p>·Operation count on the {base}: {count}".format(base=base, count=count)

                elif perc:
                    perc = SeqClass.perc(base)
                    perc = "<p>·Operation percentage on the {base}: {perc}".format(base=base, perc=perc)


                contents = """
                <html>
                <header>
                    <meta charset="UTF-8">
                    <title>Result</title>
                </header>
                
                <body>
                    <h1><u><RESULTS</u></h1>
                    <p>· Sequence given by user: {seq}</p><br>
                    
                """ + len + """
                </body>
                
                
                </html>
                """


        # If the resource doesn't exist
        else:
            f_error = open('error.html', 'r')
            contents = f_error.read()

        # PRINT RESPONSE MESSAGE
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()

        # SEND BODY OF RESPONSE MESSAGE
        self.wfile.write(str.encode(contents))


# -- Main program
with socketserver.TCPServer(('', PORT), SeqHandler) as httpd:
    print('Serving at PORT: {}'.format(PORT))

    try:
        httpd.serve_forever()

    except KeyboardInterrupt:
        print('Exit by user.')
        httpd.server_close()
