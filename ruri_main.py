#계획요약
#1. 루리웹의 게시판 제목을 모두 긁어
#2. 몽고DB에 저장 후 
#3. 제목의 링크로 접속하여 위의 몽고 DB에 추가
#4. 약 10000여 건의 게시물 크롤링 시도
#5. 최다빈도 단어를 통해 정치적 성향을 가진 단어를 추출하여
#6. 해당 단어를 가진 제목을 필터링 한 이후
#7. 해당게시물 중 www.chosum.com 등 언론사의 주소가 링크된 게시물의 반응을 선정하여
#8. 해당 사이트의 정치적 성향을 지정 => 통계적 과정

#현재 상황
#3까지 완료.


# import

# 웹페이지 접속과 파싱
import requests
import lxml.html
import cssselect

# 크롤링
from ruri_crawling import crawling

# 몽고DB
from pymongo import MongoClient
from pymongo import errors
import json

# 크롤링
## 크롤링에 쓸 css태크 호출
with open('./myProject_A_python/mycrawling.json') as f:
    cdata = json.load(f)

## 순서대로 번호, 게시글 링크, 제목, 추천, 게시글 내 링크, 댓글
cr = crawling(
        cdata['cno'],
        cdata['clink'],
        cdata['ctitle'],
        cdata['cthumb'],
        cdata['ccontent'],
        cdata['clinks'],
        cdata['creplies'],
        )

# DB에 저장 (클래스 화)
with open('./myProject_A_python/myinfo.json') as f:
    data = json.load(f)

j_host = data['host']
j_port = data['port']
j_database = data['database']
j_collection = data['collection']

client = MongoClient(j_host, j_port)
database = client[j_database]
collection = database[j_collection]

### 자료를 얼마나 모았을까? ###
print('titles this crawler have collected till now : ', len(cr[2]))

for i in range(0, len(cr[2])):
    ruri = {
        'no' : cr[0][i],
        'html' : cr[1][i],
        'title' : cr[2][i],
        'thumbup' : cr[3][i],
        'content' : cr[4][i]
    }
    doc_id = collection.insert_one(ruri).inserted_id
    print('no. : ', i, 'inserted id to mongodb : ', doc_id)

client.close()