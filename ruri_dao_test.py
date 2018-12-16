from pymongo import MongoClient
from ruri_connect import ConnectTo
import json

class CrwalingDAO:
    #load db info
    def setdbinfo(self):
        with open('./myProject_A_python/myinfo.json') as f:
            print('서버에 접속하기 위해 %s파일을 호출합니다 : ' % f.name)
            data = json.load(f)
            #접속호출
            #함수에 아래의 내용 넣기
            connectto = ConnectTo(data['host'], data['port'], data['database'], data['collection'])
            
            #현재는 mongoDB만 가능하지만 추후 다른 DB도 선택할 수 있도록 변경
            connectto.MongoDB()

            return connectto

    def insertone(self, cr):
        ### 자료를 얼마나 모았을까? ###
        print('titles this crawler has collected till now : ', len(cr[2]))
        with open('./myProject_A_python/mysave.json', 'w') as f:
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
                
                #mongodb
                doc_id = self.setdbinfo().m_collection.insert_one(ruri).inserted_id
                print('no.', i+1, 'inserted id in mongodb : ', doc_id)

        self.setdbinfo().m_client.close()