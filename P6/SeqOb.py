# Web server for performing operations on a sequence

import http.server
import socketserver
import termcolor

from P1.Seq import Seq

PORT = 8004


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
            print('INITIAL PATH...')
            f_200 = open('main.html', 'r')
            contents = f_200.read()

        # If sequence is sent
        elif 'seq' in self.path:
            print('ANALYZING SEQUENCE...')

            path = self.path.replace('/seq?', '').replace(' HTTP/1.1', '')
            inputs = path.split('&')
            print('- Inputs: ', inputs)

            input_seq = inputs[0].split('=')[1]

            # CHECK SEQUENCE SUBMITTED
            seq = attend_seq(input_seq)

            if not seq:  # if there IS NOT sequence, error
                f_error = open('error.html', 'r')
                contents = f_error.read()
                print('- Sequence not valid.')

            # ANALYZE INPUTS
            else:  # if there IS sequence, continue with inputs
                print('- Sequence valid.')

                SeqClass = Seq(seq)

                # SAVE ALL OPTIONS

                # In case options are not selected...
                seq_len = "---"
                count = False
                perc = False

                for i in inputs:
                    element = i.split('=')
                    i_type = element[0]
                    i_value = element[1]

                    # 1.- CHECK LENGTH
                    if i_type == 'chk':
                        seq_len = SeqClass.len()

                    # 2.- CHECK OPERATIONS
                    elif i_type == 'operation':

                        if i_value == 'count':
                            operation = '"counter"'
                            count = True
                        elif i_value == 'perc':
                            operation = '"percentage"'
                            perc = True

                    # 3.- CHECK BASE
                    elif i_type == 'base':
                        base = i_value

                # CALCULATE OPERATIONS
                if count==True:
                    result = SeqClass.count(base)

                elif perc==True:
                    perc = SeqClass.perc(base)
                    result = "{}%".format(perc)

                else:
                    result = '---'

                contents = """
                        <html>
                            <header>
                                <meta charset="UTF-8">
                                <title>Result</title>
                            </header>
        
                            <body>
                                <h1><u>RESULTS</u>:</h1>
                                <br>
                                <p>· <b>SEQUENCE:</b> {seq}</p>
                                <p>· Sequence length: {seq_len}<p>
                                <p>· Operation {operation} on {base}: {result}</p>
                                
                                
                                <br>
                                <a href="/">[Main page]</a>
                                
                            </body>
        
        
                        </html>
                        """.format(seq=seq, seq_len=seq_len, operation=operation, base=base, result=result)

        # If the resource doesn't exist
        else:
            print('ERROR...')
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
