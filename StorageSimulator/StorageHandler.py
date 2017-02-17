import tornado.ioloop
import tornado.web
import json
import logging
import traceback
import datetime

from tornado import gen
from tornado.escape import json_encode
from tornado.httpclient import HTTPRequest
from tornado.httpclient import HTTPClient,AsyncHTTPClient

class CreateLUN(tornado.web.RequestHandler):
    def get(self):
        rv = {}
        rv['result'] = 'failed'
        rv['msg'] = 'Method Not Supported'
        self.write(json.dumps(rv))
        return
    @gen.coroutine
    def post(self):
        try:
            rv = {}
            rv['result'] = 'failed'

            data = tornado.escape.json_decode(self.request.body)['data']
            print(data)

            storage = self.settings['storage']

            size_to_use = sum([int(lun['size']) for lun in data])
            if size_to_use > storage.available_size:
                rv['msg'] = 'No Enough Space to Create LUNs'
                return rv

            luns = []
            for lun in data:
                name = lun['name']
                size = int(lun['size'])
                print('create lun, name - %s, size - %d' % (name, size))
                r = storage.create_lun(name, size)
                if r['result'] == 'success':
                    luns.append(lun)
                else:
                    break

            rv['result'] = 'success'
            rv['luns'] = luns
            self.write(json.dumps(rv))
            return
        except:
            err = traceback.format_exc()
            print(err)
            self.write(json.dumps(rv))
            return

class ListLUN(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        try:
            rv = {}
            rv['result'] = 'failed'

            storage = self.settings['storage']
            r = storage.list_lun()
            print(r)
            if r['result'] == 'success':
                rv['luns'] = r['luns']
            else:
                self.write(json.dumps(r))
                return

            self.write(json.dumps(rv))
            return
        except:
            self.write(json.dumps(rv))
            return
class ModifyLUN(tornado.web.RequestHandler):
    @gen.coroutine
    def post(self):
        try:
            rv={}
            rv['result']='failed'

            data = tornado.escape.json_decode(self.request.body)['data']
            #print(data)

            storage = self.settings['storage']
            name =data['name']
            size=data['size']
            r = storage.modify_lun(name, size)
            if r['result'] == 'success':
                rv['result']= 'sucesss'
                rv['size']=size
            self.write(json.dumps(rv))
            return
        except:
            self.write('failed')
            return
class DeleteLUN(tornado.web.RequestHandler):
    def post(self):
        try:
            rv={}
            rv['result']='failed'
            data = tornado.escape.json_decode(self.request.body)['data']
            storage = self.settings['storage']
            name=data['name']
            r= storage.delete_lun(name)
            print('del')
            print(r)
            if r['result']== 'success':
                rv['result']= 'success'
                rv['name']=name
            self.write(json.dumps(rv))
            return
        except:
            self.write(json.dumps(rv))
            return

