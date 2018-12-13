from pymongo import MongoClient
from pymongo import errors
import json

class CrwalingDAO:
    #load db info
    def setdbinfo(self):
        with open('./myProject_A_python/myinfo.json') as f:
            data = json.load(f)
            j_host = data['host']
            j_port = data['port']
            j_database = data['database']
            j_collection = data['collection']

            client = MongoClient(j_host, j_port)
            database = client[j_database]
            collection = database[j_collection]
            # return client, database, collection

    def insertone(self, cr):
        ### 자료를 얼마나 모았을까? ###
        print('titles this crawler has collected till now : ', len(cr[2]))
        with open('./myProject_A_python/mysave.json', 'w') as f:
            for i in range(0, len(cr[2])):
                ruri = {
                    'no' : cr[0][i],
                    'html' : cr[1][i],
                    'title' : cr[2][i],
                    'thumbup' : cr[3][i],
                    'content' : cr[4][i]
                }
                json.dump(ruri, f)
                doc_id = self.setdbinfo()[2].insert_one(ruri).inserted_id
                print('no. : ', i, 'inserted id in mongodb : ', doc_id)

        self.setdbinfo()[0].close()