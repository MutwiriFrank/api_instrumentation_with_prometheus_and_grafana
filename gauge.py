import http.server
from prometheus_client import start_http_server, Counter, Gauge
import time


APP_PORT = 8000
METRICS_PORT = 8001
REQUEST_IN_PROGRESS =Gauge('app_request_in_progress', '- count of application requests in progress')
REQUEST_LAST_SERVED =Gauge('app_last_served',  'Time the application was last served')

class HandleRequests(http.server.BaseHTTPRequestHandler):
    
    def do_GET(self):
        REQUEST_IN_PROGRESS.inc()
        time.sleep(5)
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes("<html>  <head>     <title>First Application</title>  </head> <body> <h2>Welcom to prometheus</h2></body></html>", "utf-8"))
        self.wfile.close()
        REQUEST_LAST_SERVED.set(time.time())
        REQUEST_IN_PROGRESS.dec()
        
        
if __name__ == "__main__":
    start_http_server(METRICS_PORT)
    server = http.server.HTTPServer(('localhost', APP_PORT), HandleRequests)
    server.serve_forever()