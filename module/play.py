class OthelloPlay():
    def play(self,y,x):
        self.x = x
        self.y = y
        
        self.colornum = self.turn

        # 置けなかったら 値がオーバーしてたら
        if y>9 or x>9 or x<0 or y<0:
            self.turn=self.turn # ターンのやり直し(見やすいように)
            return False

        if self.board[x,y]!=0:
            self.turn=self.turn
            return False
        


        """
        ひっくり返す処理
        """
        # 右
        if self.board[x,y+1] == -self.colornum: # 一個右に相手の色の石があれば
            memox = []
            memoy = []
            #右にスライドしていく
            for i in range(y+1,9):
                if self.board[x,i] == -self.colornum:
                    memox.append(x)
                    memoy.append(i)
                #壁,空白なら停止
                elif self.board[x,i] == 2 or self.board[x,i] == 0:
                    break
                #自分の石があったら
                elif self.board[x,i] == self.colornum:
                    self.board[memox[0]:memox[-1]+1  ,  memoy[0]:memoy[-1]+1] *= -1
                    self.board[x,y] = self.colornum
                    break

        # 左
        if self.board[x,y-1] == -self.colornum: # 一個左に相手の色の石があれば
            memox = []
            memoy = []
            #左にスライドしていく
            for i in range(y-1,0,-1):
                if self.board[x,i] == -self.colornum:
                    memox.append(x)
                    memoy.append(i)
                #壁なら停止
                elif self.board[x,i] == 2 or self.board[x,i] == 0:
                    break
                #自分の石があったら
                elif self.board[x,i] == self.colornum:

                    self.board[memox[-1]:memox[0]+1  ,  memoy[-1]:memoy[0]+1] *= -1
                    self.board[x,y] = self.colornum
                    break
        
        # 上
        if self.board[x-1,y] == -self.colornum: # 一個上に相手の色の石があれば
            memox = []
            memoy = []
            #上にスライドしていく
            for i in range(x-1,0,-1):
                if self.board[i,y] == -self.colornum:
                    memox.append(i)
                    memoy.append(y)
                #壁なら停止
                elif self.board[i,y] == 2 or self.board[i,y] == 0:
                    break
                #自分の石があったら
                elif self.board[i,y] == self.colornum:
                    self.board[memox[-1]:memox[0]+1  ,  memoy[-1]:memoy[0]+1] *= -1
                    self.board[x,y] = self.colornum
                    break
        
        # 下
        if self.board[x+1,y] == -self.colornum: # 一個下に相手の色の石があれば
            memox = []
            memoy = []
            #下にスライドしていく
            for i in range(x+1,9):

                if self.board[i,y] == -self.colornum:
                    memox.append(i)
                    memoy.append(y)
                #壁なら停止
                elif self.board[i,y] == 2 or self.board[i,y] == 0:
                    break
                #自分の石があったら
                elif self.board[i,y] == self.colornum:
                    self.board[memox[0]:memox[-1]+1  ,  memoy[0]:memoy[-1]+1] *= -1
                    self.board[x,y] = self.colornum
                    break
        
        # 右下
        if self.board[x+1,y+1] == -self.colornum: # 一個右下に相手の色の石があれば
            memox = []
            memoy = []
            #下にスライドしていく
            for (i,j) in zip(range(x+1,9), range(y+1,9)):
                if self.board[i,j] == -self.colornum:
                    memox.append(i)
                    memoy.append(j)
                #壁なら停止
                elif self.board[i,j] == 2 or self.board[i,j] == 0:
                    break
                #自分の石があったら
                elif self.board[i,j] == self.colornum:
                    for (xx,yy) in zip(memox,memoy):
                        self.board[xx,yy] *= -1
                    self.board[x,y] = self.colornum
                    break

        # 右上
        if self.board[x-1,y+1] == -self.colornum: # 一個右上に相手の色の石があれば

            memox = []
            memoy = []
            #右上にスライドしていく
            for (i,j) in zip(range(x-1,0,-1), range(y+1,9)):
                if self.board[i,j] == -self.colornum:

                    memox.append(i)
                    memoy.append(j)
                #壁なら停止
                elif self.board[i,j] == 2 or self.board[i,j] == 0:
                    break
                #自分の石があったら
                elif self.board[i,j] == self.colornum:
                    for (xx,yy) in zip(memox,memoy):
                        self.board[xx,yy] *= -1
                    self.board[x,y] = self.colornum
                    break

        # 左下
        if self.board[x+1,y-1] == -self.colornum: # 一個左下に相手の色の石があれば

            memox = []
            memoy = []
            #下にスライドしていく
            for (i,j) in zip(range(x+1,9), range(y-1,0,-1)):
                if self.board[i,j] == -self.colornum:

                    memox.append(i)
                    memoy.append(j)
                #壁なら停止
                elif self.board[i,j] == 2 or self.board[i,j] == 0:
                    break
                #自分の石があったら
                elif self.board[i,j] == self.colornum:
                    for (xx,yy) in zip(memox,memoy):
                        self.board[xx,yy] *= -1
                    self.board[x,y] = self.colornum
                    break

        # 左上
        if self.board[x-1,y-1] == -self.colornum: # 一個左上に相手の色の石があれば

            memox = []
            memoy = []
            #下にスライドしていく
            for (i,j) in zip(range(x-1,0,-1), range(y-1,0,-1)):
                if self.board[i,j] == -self.colornum:

                    memox.append(i)
                    memoy.append(j)
                #壁なら停止
                elif self.board[i,j] == 2 or self.board[i,j] == 0:
                    break
                #自分の石があったら
                elif self.board[i,j] == self.colornum:
                    for (xx,yy) in zip(memox,memoy):
                        self.board[xx,yy] *= -1
                    self.board[x,y] = self.colornum
                    break
        

        # 石が置けたら
        if self.board[x,y] != 0:
            self.turn *= -1 #ターンの入れ替え
            return True

        self.turn=self.turn # ターンのやり直し(見やすいように)
        return False