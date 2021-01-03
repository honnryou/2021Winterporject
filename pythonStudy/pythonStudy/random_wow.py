#댓글 작성자 중에 추첨을 통해 1명은 치킨 3명은 커피 쿠폰을 받게 됩니다
#조건 댓글은 20명이작성하엿고 아이디는 1-20이라고 가정
#댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
#random모듈의 shuffle과 sample 활용
from random import *

users = range(1,21) #range로 선언
users = list(users)#선언된 range를  list로 변환
shuffle(users)

winners = sample(users, 4)
print("==당첨자발표==")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
 
