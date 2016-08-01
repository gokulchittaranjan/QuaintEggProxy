# QuaintEggProxy
A proxy server that translates REST API requests to another server; useful for UI development
  
Usage:
```
$ cd ~
$ mkdir qstools
$ cd qstools
$ git clone https://github.com/gokulchittaranjan/PythonUtils.git
$ git clone https://github.com/gokulchittaranjan/QuaintEgg.git
$ git clone https://github.com/gokulchittaranjan/QuaintEggProxy.git
$ sudo apt-get install python-pip
$ sudo pip install web.py requests
$ export PYTHONPATH=$PYTHONPATH:$HOME/qstools
$ cd QuaintEggProxy
$ python simpleproxy.py --proxy http://youractualserver.com -p 8080 
```

This should start a server that routes all requests to youractualserver.com

Now, you can place your HTML and JS files in the `~/qstools/QuaintEggProxy/static` directory.
They should be accessible under `http://localhost:8080/static/`

Distributed under Apache-2.0 License (see LICENCE for details)
