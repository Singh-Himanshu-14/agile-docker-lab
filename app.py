# app.py
from http.server import SimpleHTTPRequestHandler, HTTPServer


class DevOpsLabHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        html_content = """
        <html>
        <head>
            <title>Agile & DevOps Lab</title>
        </head>

        <body style='text-align: center;
                     font-family: sans-serif;
                     padding-top: 100px;
                     background-color: #f4f6f9;'>

            <h1 style='color: #1e3a8a;'>
                Docker Experiment Successful!
            </h1>

            <p style='font-size: 1.2em; color: #334155;'>
                Application layer successfully isolated inside a Docker container.
            </p>

            <div style='display: inline-block;
                        padding: 10px 20px;
                        background: #10b981;
                        color: white;
                        border-radius: 5px;'>

                Continuous Deployment State: Active

            </div>

        </body>
        </html>
        """

        self.wfile.write(html_content.encode('utf-8'))


server = HTTPServer(('0.0.0.0', 8080), DevOpsLabHandler)

print("DevOps Lab Server listening on port 8080...")

server.serve_forever()
