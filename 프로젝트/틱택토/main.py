from functions import *         # functions.py 기능들 불러오기

trycnt=3
for _ in range(trycnt):
    id=input("아이디를 입력해주세요: ")
    pw=input("패스워드를 입력해주세요:")
    if login(id,pw):
        print(f"{id}님 환영합니다.")
        break
    else:
        print("아이디와 패스워드를 다시 확인해주세요.")
else:
    print("시도 횟수를 모두 소진하였습니다. 종료합니다.")
    exit()

# 틱택토
board= ['*'] * 9
# 1. 사용자가 O나 X중 하나 선택
while True:
    player=input("O나 X중 하나를 선택하시오: ")
    if player == "O" or player == 'o':
        computer="X"
        break
    elif player in "Xx" :
        computer="O"
        break
    else:
        print("잘못된 문양을 선택하셨습니다. 다시 입력해주세요.")
print(player, computer)
display_board(board)

# 2. 게임 실행
while True:
#    2-1. 사용자가 놓을 좌표 입력: input_pos()사용 => 좌표 반환
    pos = input_pos(board)
#    2-2. 입력된 좌표에 사용자 문양 삽입
    board[pos] = player
    display_board(board)
#    2-3. 우승 조건 확인, 무승부 조건 확인
    if VICTORY(board,player):
        print("PLAYER WIN!")
        break
    elif '*' not in board:
        print("draw")
        break
#    2-4. 컴퓨터가 놓을 좌표 생성
    pos = random_pos(board)
#    2-5. 생성된 좌표에 컴퓨터 문양 삽입
    board[pos] = computer
    display_board(board)
#    2-6. 우승 조건 확인
    if VICTORY(board,computer):
        print("COMPUTER WIN!")
        break

