from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse


# HTTP request handler class
class RequestHandler(BaseHTTPRequestHandler):

    # Handle GET requests
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            # Serve the HTML form
            with open('pankaj.html', 'rb') as file:
                self.wfile.write(file.read())
        else:
            self.send_error(404, 'Page Not Found')

    # Handle POST requests
    def do_POST(self):
        if self.path == '/submit-form':
            # Read form data from request body
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            parsed_data = urllib.parse.parse_qs(post_data)

            # Get username and password from form data
            username = parsed_data.get('username', [''])[0]
            password = parsed_data.get('password', [''])[0]

            # Send response back to client
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            response = f'Username: {username}, Password: {password}'
            self.wfile.write(response.encode('utf-8'))
        else:
            self.send_error(404, 'Page Not Found')


# Main function to start the server
def main():
    try:
        # Create HTTP server
        server = HTTPServer(('localhost', 8000), RequestHandler)
        print('Server started on http://localhost:8000')
        # Run the server
        server.serve_forever()
    except KeyboardInterrupt:
        print('^C received, shutting down the server')
        server.socket.close()


if __name__ == '__main__':
    main()
