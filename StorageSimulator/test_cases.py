
import json

import urllib
import urllib.request

def test_create_lun():
    url = 'http://127.0.0.1:8888/api/lun/create'
    data = {
        'data': [
            {'name': 'lun0', 'size': 100},   
            {'name': 'lun1', 'size': 500},   
        ],
    }
    data_json = json.dumps(data).encode('utf-8')

    req = urllib.request.Request(url, data_json, {'Content-Type': 'application/json'})
    with urllib.request.urlopen(req) as f:
        buf = f.read()
        r = json.loads(buf.decode('utf-8'))
        print('create lun success, the LUNs is:')
        for lun in r['luns']:
            print('LUN: name - %s, size - %d' % (lun['name'], lun['size']))
    return

def test_list_lun():
    url = 'http://127.0.0.1:8888/api/lun/list'
    #req = urllib.request.Request(url, data_json, {'Content-Type': 'application/json'})
    with urllib.request.urlopen(url) as f:
        buf = f.read()
        r = json.loads(buf.decode('utf-8'))
        print('List LUNs success, the LUNs is:')
        for lun in r['luns']:
            print('LUN: name - %s, size - %d' % (lun['name'], lun['size']))
    return
def test_modify_lun():
    url = 'http://127.0.0.1:8888/api/lun/modify'
    data= {
    'data':{'name':'lun0','size':222}
    }
    data_json = json.dumps(data).encode('utf-8')
    req = urllib.request.Request(url,data_json,{'Content_Type':'application/json'})
    with urllib.request.urlopen(req) as f:
        buf = f.read()
        r=json.loads(buf.decode('utf-8'))
        print('Modify lun success, the LUN size is changed %d' % r['size'])
    return

def test_delete_lun():
    url ='http://127.0.0.1:8888/api/lun/delete'
    data ={
    'data':{'name':'lun0','size':222}
    }
    data_json= json.dumps(data).encode('utf-8')
    req = urllib.request.Request(url,data_json,{'Content_Type':'application/json'})
    with urllib.request.urlopen(req) as f:
        buf = f.read()
        r=json.loads(buf.decode('utf-8'))
        if r['result'] == 'success':
            print('Delete lun success, the LUN %s is deleted' % r['name'])
        else:
            print('failed')
    return
print('Test Case 1 - Create 2 LUNs')
test_create_lun()
print('Test Case 1 - finished\n\n')

print('Test Case 2 - Modify LUN Size')
test_modify_lun()
print('Test Case 2 - finished\n\n')

print('Test Case 3 - List all the LUNs')
test_list_lun()
print('Test Case 3 - finished\n\n')

print('Test Case 4 - Delete LUN')
test_delete_lun()
test_list_lun()
print('detele finished\n\n')
