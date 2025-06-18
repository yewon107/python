import random


def display_board(board):
    for i in range(3):
        print("-------------")
        print(f"| {board[i*3]} | {board[i*3+1]} | {board[i*3+2]} |")
    print("-------------")
    pass


def input_pos(board):
    while True:
        pos= input("1~9중 위치를 입력하세요: ")
        if pos.isdigit():
            pos = int(pos)
            if pos in range(1,10):
                pos -= 1
                if board[pos] == '*':
                    return pos
                else:
                    print("이미 입력된 자리입니다. 다시 확인해주세요.")
            else:
                print("1~9까지 정수 형태로 입력해주세요.")
        else:
            print("정수 형태로 입력해주세요.")



def random_pos(board):
   while True:
        s= random.randint(0,8)
        if board[s] == '*':
            return s


def VICTORY(board,user):
    coords = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for a,b,c in coords:
        if board[a] == board[b] == board[c] == user :
            return True

    return False

def login(id,pw):
    # 입력받은 아이디 패스워드를 db.txt에서 가져온 아이디 패스워드와 비교하여 일치하는 경우에 TRUE 반환
    with open('DB.txt', 'r', encoding='utf8') as file:
        line = file.readlines() #['id: abcd\n', 'pw: 1234\n', 'id: qwer\n', 'pw: 5678\n', 'id: yewon\n', 'pw: 0107\n', 'id: 가나다라\n', 'pw: 7890']
        for i in range(0,len(line),2):
            DBid= line[i].split()[1]
            DBpw= line[i+1].split()[1]
            if id == DBid and pw == DBpw:
                return True
    return False



if __name__=='__main__':
    id=input()
    pw=input()
    print(login(id,pw))