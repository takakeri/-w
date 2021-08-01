import numpy as np
class OthelloSearch():
    def search(self):
        self.colornum = self.turn
        #置けるかどうかを見れるやつ
        self.canput_board = np.zeros((10,10),dtype=np.int8)
        for x in range(1,9):
            for y in range(1,9):
                canput=False

                #空白以外
                if self.board[x,y]!=0:
                    continue

                # 右
                if self.board[x,y+1] == -self.colornum: # 一個右に相手の色の石があれば

                    #右にスライドしていく
                    for i in range(y+1,9):
                        if self.board[x,i] == -self.colornum:
                            pass
                        #壁,空白なら停止
                        elif self.board[x,i] == 2 or self.board[x,i] == 0:
                            break
                        #自分の石があったら
                        elif self.board[x,i] == self.colornum:
                            canput = True
                            break
                            

                # 左
                if self.board[x,y-1] == -self.colornum: # 一個左に相手の色の石があれば
                    #左にスライドしていく
                    for i in range(y-1,0,-1):
                        if self.board[x,i] == -self.colornum:
                            pass
                        #壁なら停止
                        elif self.board[x,i] == 2 or self.board[x,i] == 0:
                            break
                        #自分の石があったら
                        elif self.board[x,i] == self.colornum:
                            canput = True
                            break
                
                # 上
                if self.board[x-1,y] == -self.colornum: # 一個上に相手の色の石があれば
                    #上にスライドしていく
                    for i in range(x-1,0,-1):
                        if self.board[i,y] == -self.colornum:
                            pass
                        #壁なら停止
                        elif self.board[i,y] == 2 or self.board[i,y] == 0:
                            break
                        #自分の石があったら
                        elif self.board[i,y] == self.colornum:
                            canput = True
                            break
                
                # 下
                if self.board[x+1,y] == -self.colornum: # 一個下に相手の色の石があれば
                    #下にスライドしていく
                    for i in range(x+1,9):
                        if self.board[i,y] == -self.colornum:
                            pass
                        #壁なら停止
                        elif self.board[i,y] == 2 or self.board[i,y] == 0:
                            break
                        #自分の石があったら
                        elif self.board[i,y] == self.colornum:
                            canput = True
                            break
                
                # 右下
                if self.board[x+1,y+1] == -self.colornum: # 一個右下に相手の色の石があれば
                    #下にスライドしていく
                    for (i,j) in zip(range(x+1,9), range(y+1,9)):
                        if self.board[i,j] == -self.colornum:
                            pass
                        #壁なら停止
                        elif self.board[i,j] == 2 or self.board[i,j] == 0:
                            break
                        #自分の石があったら
                        elif self.board[i,j] == self.colornum:
                            canput = True
                            break

                # 右上
                if self.board[x-1,y+1] == -self.colornum: # 一個右上に相手の色の石があれば
                    #下にスライドしていく
                    for (i,j) in zip(range(x-1,0,-1), range(y+1,9)):
                        if self.board[i,j] == -self.colornum:
                            pass
                        #壁なら停止
                        elif self.board[i,j] == 2 or self.board[i,j] == 0:
                            break
                        #自分の石があったら
                        elif self.board[i,j] == self.colornum:
                            canput = True
                            break

                # 左下
                if self.board[x+1,y-1] == -self.colornum: # 一個左下に相手の色の石があれば
                    #下にスライドしていく
                    for (i,j) in zip(range(x+1,9), range(y-1,0,-1)):
                        if self.board[i,j] == -self.colornum:
                            pass
                        #壁なら停止
                        elif self.board[i,j] == 2 or self.board[i,j] == 0:
                            break
                        #自分の石があったら
                        elif self.board[i,j] == self.colornum:
                            canput = True
                            break

                # 左上
                if self.board[x-1,y-1] == -self.colornum: # 一個左上に相手の色の石があれば
                    #下にスライドしていく
                    for (i,j) in zip(range(x-1,0,-1), range(y-1,0,-1)):
                        if self.board[i,j] == -self.colornum:
                            pass
                        #壁なら停止
                        elif self.board[i,j] == 2 or self.board[i,j] == 0:
                            break
                        #自分の石があったら
                        elif self.board[i,j] == self.colornum:
                            canput = True
                            break
                

                # 石が置けたら
                if canput==True:
                    self.canput_board[x,y] = 1


        # 一つも置けなかったら
        if np.count_nonzero(self.canput_board == 1) == 0:
            print("a")
            return False
        
        return True

        
    