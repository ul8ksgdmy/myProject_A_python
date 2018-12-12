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
#2까지 완료.


# import

# 웹페이지 접속과 파싱
import requests
import lxml.html
import cssselect

# 몽고DB
from pymongo import MongoClient
from pymongo import errors
import json

# 접속할 주소 및 기타 접속 정보
url = 'http://bbs.ruliweb.com/community/board/300148'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}

# for i in range(0, 10):
res = requests.get(url, headers=headers)
html = res.text
root = lxml.html.fromstring(html)

# 0. 매 페이지의 정보를 저장
## upper page
ruri_no_list = []
ruri_title_list = []
ruri_html_list = []
ruri_thumbup_list = []

## lower page
ruri_contents_part_list = [] #for adding all lists


# 1. 제목, 링크 및 기타 정보 추출
## 번호
for part_html in root.cssselect('tr.table_body td.id'):
    ruri_no_list.append(part_html.text_content())

## 링크 및 제목
for part_html in root.cssselect('tr.table_body div.relative a.deco'):
    ruri_html_list.append(part_html.get('href'))
    ruri_title_list.append(part_html.text_content())

## 추천수
for part_html in  root.cssselect('tr.table_body td.recomd'):
    ruri_thumbup_list.append(part_html.text_content())

# 2. 수집한 링크로 이동
for innerlink in ruri_html_list:
    inner_res = requests.get(innerlink, headers=headers)
    inner_html = inner_res.text
    inner_root = lxml.html.fromstring(inner_html)

    #게시물 & 내부링크
    main_content = ""
    # ruri_contents_list = []
    ruri_innerlink_list = []
    ruri_replies_list = []

    # 게시글
    for part_html in inner_root.cssselect('div.board_main_view div.view_content'):
        main_content = part_html.text_content() #게시글은 하나 밖에 없기 때문에 리스트가 아닌 일반 변수로 저장
        # ruri_contents_list.append(content) #게시물
    
    # 링크 - href만 긁으려고 했는데, 유튜브 등의 주소도 있음.
    for part_html in inner_root.cssselect('div.board_main_view div.view_content p a'):
        if part_html.get('href') is None:
            continue
        ruri_innerlink_list.append(part_html.get('href')) #내부링크

    #댓글
    for part_html in inner_root.cssselect('div.comment_view.normal table.comment_table tr.comment_element > td.comment > div.text_wrapper > span.text'):
        ruri_replies_list.append(part_html.text_content())

    #게시글마다 dictionary type을 생성
    ruri_content_dict = {
        'content' : main_content,
        'link' : ruri_innerlink_list,
        'reply' : ruri_replies_list
    }

    #list에 모든 dictionary type을 넣음
    ruri_contents_part_list.append(ruri_content_dict)

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

# for i in range(0, len(ruri_contents_part_list)):
#     print(ruri_contents_part_list[i])


for i in range(0, len(ruri_title_list)):
    ruri = {
        'no' : ruri_no_list[i],
        'html' : ruri_html_list[i],
        'title' : ruri_title_list[i],
        'thumbup' : ruri_thumbup_list[i],
        'content' : ruri_contents_part_list[i]
    }
    doc_id = collection.insert_one(ruri).inserted_id
    print('inserted id to mongodb : ', doc_id)




client.close()