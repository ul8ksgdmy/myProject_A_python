# 텍스트 마이닝
# 트위터에서 데이터 수집하기
# twitterscapper install

from twitterscraper import query_tweets
import datetime as dt
from time import sleep

# # 1
i = 0
if __name__ == '__main__':
    for tweet in query_tweets('워마드',10):
        # print(tweet.timestamp) # 작성시간
        i += 1
        print(i) # 트윗내용

# twitterscraper 테스트 : 수집결과 파일저장, 수집일자 설정.


# 2
# if __name__ == '__main__':
#     #수집한 트위터를 저장할 경로지정.
#     fname = r'C:/Users/HOME/Desktop/bigdata/test/bf'+str(dt.date.today())+'.txt'

#     file = open(fname, 'ab') #지정한 파일객체 생성
#     for tweet in query_tweets('블랙프라이데이', begindate=dt.date(2018, 11, 1), enddate=dt.date(2018, 11, 28),limit=10):
#         file.write(str(tweet.timestamp).encode())
#         file.write(tweet.text.encode('utf-8'))
#     file.close()


# 3
# if __name__ == '__main__':
#     fname = r'C:/Users/HOME/Desktop/bigdata/test/bf'+str(dt.date.today())+'.txt'
#     total = 0 #수집한 트윗 건 수

#     size = 0
#     file = open(fname, 'ab') #지정한 파일객체 생성
#     for tweet in query_tweets('블랙프라이데이', begindate=dt.date(2018, 11, 1), enddate=dt.date(2018, 11, 28)):
#         file.write(str(tweet.timestamp).encode())
#         file.write(tweet.text.encode('utf-8'))
#         size += 1 #수집한 트윗을 파일에 저장할 때마다 카운트를 하나씩 증가.

#         file.close()
#         total += size
#         print('수집한 트윗 총 갯수', total)

#         sleep(5)