#!/usr/bin/python

import os;
import shutil;
import json;

import web;

#from collections import defaultdict;
#from config import *;

urls = (
	"/(.*)", "ProxyController",

	)

from QuaintEgg.lib.Util import GenericUtil;
from QuaintEgg.lib.WebPyCustomizations  import QuaintEggApplication;
from QuaintEgg.lib.Proxy import Proxy;
from QuaintEgg.framework.controllers.ControllerUtil import *;

application = None;

options = None;
global proxyAddress;
proxyAddress = "";
if __name__ == "__main__":
	p = QuaintEggApplication.getParser()
	p.add_argument("-a", "--proxy", default="http://localhost:7000", help="Proxy address");
	options = p.parse_args();
	proxyAddress = options.proxy
	if proxyAddress[-1]=="/":
		proxyAddress = proxyAddress[:-1]

web.config.debug = False

app = QuaintEggApplication(urls, globals());


class ProxyController:

	def GET(self, path):
		#jsonHook();
		proxy = Proxy("%s/%s" %(proxyAddress, path));
		res, headers = proxy.response(web.input().items(), "get", web.ctx.env)
		for k,v in headers.items():
			web.header(k,v);
		return res

	def PUT(self, path):
		#jsonHook();
		proxy = Proxy("%s/%s" %(proxyAddress, path));
		res, headers = proxy.response(web.input().items(), "put", web.ctx.env)
		for k,v in headers.items():
			web.header(k,v);
		return res
	
	def DELETE(self, path):
		#jsonHook();
		proxy = Proxy("%s/%s" %(proxyAddress, path));
		res, headers = proxy.response(web.input().items(), "delete", web.ctx.env)
		for k,v in headers.items():
			web.header(k,v);
		return res

if __name__=="__main__":
	app.run(port=options.port, host=options.host);