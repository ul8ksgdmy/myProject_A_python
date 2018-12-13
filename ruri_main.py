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
from ruri_service import Crawling
from ruri_dao import CrwalingDAO

#크롤링
cr = Crawling()
cd = CrwalingDAO()
print('---- 크롤링 중 ----')
cd.insertone(cr.crawling(5)) #5page까지
