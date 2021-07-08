#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author:Sh4d0w_小白

import http.server
import socketserver
import sys

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

class OptHandler(Handler):
    def log_message(self, format, *args):
        sys.stderr.write("%s - - [%s] %s\n" %
                         (self.address_string(),
                          self.log_date_time_string(),
                          format%args))
        with open("out.txt","a+") as f:
            f.write("%s - - [%s] %s\n" %
                         (self.address_string(),
                          self.log_date_time_string(),
                          format%args))

Handler = OptHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
