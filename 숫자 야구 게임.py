# 숫자야구게임
# 추측한 수가 정답에 있으나 자리가 다르면 BALL
#                    고 자리도 같으면 STRIKE
# 추측한 세 개의 수가 하나도 정답에 없다면 OUT!
# 위 과정을 정답을 맞출때 까지 반복
# 정답을 맞췄을 땐, "축하합니다. 총 00회 시도만에 맞추었습니다." 출력
# 만약에 0 0 0이 입력으로 주어진다면, 게임을 종료하면서 "정답은 0 0 0이었습니다." 출력

# 1. 사용자가 추측값을 입력한다.
#    0 0 0 입력시 게임 종료,
#    정답하고 같은 값을 입력했으면 바로 게임종료
#    실행 횟수 카운팅
# 2. 입력된 추측값과 정답을 비교하여 BALL, STRIKE, OUT!을 판별한다.
# 3. 판별된 내용을 출력한다.
# 위 과정을 정답을 맞출때 까지 반복한다.
# BALL: 2, STRIKE: 1

import random
random.randint(0, 9)
answer= []

while len(answer) < 3:
    x= random.randint(0, 9)
    if x not in answer:
        answer.append(x)


try_count=0
while True:
    user = list(map(int,input("정답을 입력하시오(ex: 1 2 3): ").split()))
    try_count += 1
    if user == [0, 0, 0]:
        print(f"땡! 정답은 {' '.join(map(str,answer))} 이었습니다. 실행횟수: {try_count}")
        break
    elif user == answer:
        print(f"축하합니다! 총 {try_count}회 시도만에 맞추었습니다.")
        break

    BALL = 0
    STRIKE = 0

    for i in range(3):
        for x in range(3):
            if user[i] == answer[x]:
                if i == x:
                    STRIKE += 1
                else:
                    BALL += 1

    if BALL == 0 and STRIKE == 0:
        print("OUT!")
    else:
        print(f"{BALL} BALL, {STRIKE} STRIKE")





