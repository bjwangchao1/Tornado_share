import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
import json
import os
import torndb
import time

from tornado.web import RequestHandler, url, StaticFileHandler
from tornado.options import define, options
from tornado.httpclient import AsyncHTTPClient

define("port", default=8000, type=int)


class IndexHandler(RequestHandler):
    def get(self):
        client = AsyncHTTPClient()
        client.fetch("http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=json&ip=14.130.112.24",
                     callback=self.on_response)

    def on_response(self, resp):
        json_data = resp.body
        data = json.loads(json_data)
        self.write(data.get('city', ''))
        self.finish()
