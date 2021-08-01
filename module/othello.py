"""
オセロクラス用
以下の操作をします
init - 初期盤面の多重配列を作成します。
turn_over_stone (x,y,color) - 石を設置して、盤面を更新します。

self.board = [8,8]の多重numpy配列    0(なにもなし), 1(黒) -1(白) 壁2
self.next = "white" or "black" 次の番を示します。

"""

import numpy as np
from .play import OthelloPlay
from .search import OthelloSearch
from .image_creater import BoardImg
import cv2


class Othello(OthelloPlay,OthelloSearch,BoardImg):
    def __init__(self):
        self.board = np.zeros((10,10),dtype=np.int8)
        
        self.board[4,4] = -1
        self.board[5,5] = -1
        self.board[4,5] = 1
        self.board[5,4] = 1

        self.board[0:10,0] = 2
        self.board[0:10,9] = 2
        self.board[0,0:10] = 2
        self.board[9,0:10] = 2

        self.turn = 1 # 1は黒だよ。最初は黒から。

        self.colornum = 1

        self.search()

        self.x,self.y = None,None
    
    def gameend(self):
        blackcount = np.count_nonzero(self.board == 1)
        whitecount = np.count_nonzero(self.board == -1)
        if blackcount<whitecount: return f'''黒: {blackcount}\n白: {whitecount}\n勝者: 白'''
        if blackcount>whitecount: return f'''黒: {blackcount}\n白: {whitecount}\n勝者: 黒'''
        if blackcount==whitecount: return f'''黒: {blackcount}\n白: {whitecount}\n引き分け'''




if __name__ == '__main__':
    othello = Othello()
    print(othello.board)
    canput_continue = 0
    while True:
        othello.search()
        othello.img_update()
        canput_continue+=1
        turn="白"
        if othello.turn==1:
            turn="黒"

        if canput_continue>=3:
            break

        # 置くことができなかったらターンをスキップする
        if othello.search()==False:
            print(f"{turn}の番がスキップされました")
            othello.turn = othello.turn*-1
            continue
        

        # 正常な動き
        canput_continue=0

        print(f"{turn}の番です")
        try:
            x = int(input("x:"))
            y = int(input("y:"))
            print(othello.play(int(x),int(y)))
        except ValueError:
            print("数字いれろカス")

    result = othello.gameend()
    print(result)