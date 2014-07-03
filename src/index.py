#coding:utf-8

import tornado.web
import tornado.httpserver
import tornado.ioloop

from weixinInterface import WeixinInterface

app = tornado.web.Application([
    (r"/weixin", WeixinInterface),
])

http_server = tornado.httpserver.HTTPServer(app)
http_server.listen(8888)
tornado.ioloop.IOLoop.instance().start()
