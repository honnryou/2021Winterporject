#랜덤으로 날짜 정하는 프로그램
#from random import *
#a = randrange(4,28)
#print('오프라인 스터디 모임 날짜는 월 '+str(a)+' 일로 선정되었습니다.')
#사이트별로 비밀번호를 만들어 주는 프로그램
#ex http://naver.com
#규칙 http:// 부분은 제외
#규칙 처음 만나는 점 이후 부분은 제외 
#규칙 남은 글자중 (처음 세자리+ 글자내 e 갯수 +!) 로 구성
#1차 답안
#a = input()
#b = a.index(".")
#c = len("http://")
#d = a.count("e")
#e = a.find(".")
#print(str(a[c:c+3])+str(len(a[c:e]))+str(d)+"!")
#모법답안
#url = input()
#my_url = url.replace("http://","")#(http:// 삭제)
#print(my_url)
#my_url = my_url[:my_url.index(".")]#(.이하 버림)
#print(my_url)
#password = my_url[:3]+str(len(my_url))+str(my_url.count("e"))+"!"
#print(password)
