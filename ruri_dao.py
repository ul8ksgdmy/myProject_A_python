from pymongo import MongoClient
import json

import platform

class CrwalingDAO:
    #load db info
    def setdbinfo(self):
        innerurl = ""
        host = ""
        if platform.system() != "Linux":
            innerurl = './myProject_A_python/myinfo.json'
            host = 'host'
        else:
            innerurl = '/home/pythonuser/project/myinfo.json'
            host = 'lhost'
        # with open() as f:
        with open(innerurl) as f:
            print('서버에 접속하기 위해 %s파일을 호출합니다 : ' % f.name)
            data = json.load(f)
            
            j_host = data[host] #linux구분
            j_port = data['port']
            j_database = data['database']
            j_collection = data['collection']

            client = MongoClient(j_host, j_port)
            database = client[j_database]
            collection = database[j_collection]
            return client, database, collection

    def insertone(self, cr):
        innerurl = ""
        if platform.system() != "Linux":
            innerurl = './myProject_A_python/mysave.json'
        else:
            innerurl = '/home/pythonuser/project/mysave.json'
        conn = self.setdbinfo()
        ### 자료를 얼마나 모았을까? ###
        print('titles this crawler has collected till now : ', len(cr[2]))
        with open(innerurl, 'w') as f:
            print('데이터 백업을 위해 %s파일을 호출합니다 : ' % f.name)
            for i in range(0, len(cr[2])):
                ruri = {
                    'no' : cr[0][i],
                    'html' : cr[1][i],
                    'title' : cr[2][i],
                    'thumbup' : cr[3][i],
                    'content' : cr[4][i]
                }
                json.dump(ruri, f)
                doc_id = conn[2].insert_one(ruri).inserted_id
                print('no.', i+1, 'inserted id in mongodb : ', doc_id)

        conn[0].close()