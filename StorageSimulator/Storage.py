import traceback

class Storage:
    total_size = 10000
    used_size = 0
    available_size = 10000

    LUNs = {}

    def __init__(self):
        return
    def create_lun(self, name, size):
        try:
            rv = {}
            rv['result'] = 'failed'

            if size > self.available_size:
                rv['msg'] = 'No Available Space to Create LUN'
                return rv

            lun = {}
            lun['size'] = size
            lun['name'] = name

            self.LUNs[name] = lun
            self.used_size += size
            self.available_size -= size

            rv['result'] = 'success'
            return rv
        except:
            return rv

    def list_lun(self):
        try:
            rv = {}
            rv['result'] = 'failed'
            if len(self.LUNs) == 0:
                rv['msg'] = 'No Available LUNs'
                rv['result'] = 'success'
                return rv
            rv['result'] = 'success'
            rv['luns'] = list(self.LUNs.values())
            return rv
        except:
            return rv
    def modify_lun(self,name,size):
        try:
            rv={}
            rv['result'] = 'failed'
            if size > self.available_size:
                return rv
            self.used_size=self.used_size - self.LUNs[name]['size']+ size
            self.available_size=self.available_size + self.LUNs[name]['size']- size
            self.LUNs[name]['size'] = size
            rv['lun'] = self.LUNs[name]
            rv['result'] = 'success'
            return rv
        except:
            return rv

            rv['result']
    def delete_lun(self,name):
        try:
            rv={}
            rv['result']='failed'
            if name in self.LUNs:
                self.used_size-=self.LUNs[name]['size']
                self.available_size += self.LUNs[name]['size']
                self.LUNs.pop(name)
                rv['result']='success'
                rv['lun']= name
                return rv
            return rv
        except:
            err = traceback.format_exc()
            print(err)
            return rv
