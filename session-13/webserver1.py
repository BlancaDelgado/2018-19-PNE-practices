# First example of python handlers

import http.server
import socketserver

# Define the Server's port
PORT = 8000

# -- Use the http.server Handler
Handler = http.server.SimpleHTTPRequestHandler

# NOTE: The Handler is the object called when a client is connected
# and needs to be attended.

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    # NOTE: Server socket created, bound to IP:PORT and changed to listen mode.

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    httpd.serve_forever()

    # NOTE: Serve forever makes server wait until a client is connected.
    # When client is connected, the handler function is called.



