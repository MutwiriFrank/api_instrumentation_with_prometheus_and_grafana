import http.server
from prometheus_client import start_http_server, Counter

REQUEST_COUNT= Counter('app_request_count', 'total http request count', ['app_name', 'endpoint']) # WILL BE EPOSED AS app_request_count_total

APP_PORT = 8000
METRICS_PORT = 8001


class HandleRequests(http.server.BaseHTTPRequestHandler):
    
    def do_GET(self):
        REQUEST_COUNT.labels('Pthon_app',  self.path).inc()
        # REQUEST_COUNT.inc()
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes("<html>  <head>     <title>First Application</title>  </head> <body> <h2>Welcom to prometheus</h2></body></html>", "utf-8"))
        self.wfile.close()
        
        
if __name__ == "__main__":
    start_http_server(METRICS_PORT)
    server = http.server.HTTPServer(('localhost', APP_PORT), HandleRequests)
    server.serve_forever()