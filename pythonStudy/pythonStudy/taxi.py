#50명의 승객과 매칭 기회가 있을때 총 탑승 승객 수를 구하라
#승객별 운행소요시간은 5분에서 50분의 난수로 정해짐
#소요시간 5분 15분 사이만 매칭해야 한다
#출력 예제 1번째손님 소요시간 15분 ....... 총 탑승 승객은 2분

from random import *
cnt = 0
for i in range(1,51):
    time = randrange(5,50)
    if 5<= time <=15:
        cnt+=1
    if i<10:
         print("0{0}번째 손님 (소요시간 : {1}분)".format(i,time))
         continue
    print("{0}번째 손님 (소요시간 : {1}분)".format(i,time))
print(" 총 탑승 승객은 {0}분".format(cnt))



