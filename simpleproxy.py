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

application = None;

options = None;
global proxyAddress;
proxyAddress = "";
if __name__ == "__main__":
	p = QuaintEggApplication.getParser()
	p.add_argument("-a", "--proxy", default="http://localhost:7000/", help="Proxy address");
	options = p.parse_args();
	proxyAddress = options.proxy

web.config.debug = False

app = QuaintEggApplication(urls, globals());


class ProxyController:

	def GET(self, path):
		proxy = Proxy("%s/%s" %(proxyAddress, path));
		res = proxy.response(web.input().items())
		return json.dumps(res)

if __name__=="__main__":
	app.run(port=options.port, host=options.host);