"""
8x8の配列から、オセロの盤面画像を作成します。
"""
import numpy as np
import cv2

class BoardImg():
    def img_update(self):
        # 盤面の画像(空)
        self.boardimg = np.zeros((374*2,374*2,3)) # 盤面33*8 + 線2*9 + 外白線100 = 382
        self.boardimg[100:374*2,100:374*2] = [0,231,0]
        self.boardimg[0:100, 0:374*2] = [255,255,255]
        self.boardimg[0:374*2, 0:100] = [255,255,255]
        self.boardimg[0:374*2, 332*2:382*2] = [255,255,255]
        self.boardimg[332*2:374*2, 0:382*2] = [255,255,255]
        for linenum in range(0,9):
            self.boardimg[(0+(linenum*2) + (linenum*33))*2 + 100: (2+(linenum*2) + (linenum*33))*2 + 100,  100:332*2] = [0,0,0]
            self.boardimg[100:332*2, (0+(linenum*2) + (linenum*33))*2 + 100: (2+(linenum*2) + (linenum*33))*2 + 100] = [0,0,0]
            if linenum!=8:
                cv2.putText(self.boardimg, f"X{linenum+1}", (110 + ((linenum*2) + (linenum*33))*2,100),cv2.FONT_HERSHEY_PLAIN, 3,(0, 0, 0), 2, cv2.LINE_AA)
                cv2.putText(self.boardimg ,f"Y{linenum+1}", (40,155 + ((linenum*2) + (linenum*33))*2),cv2.FONT_HERSHEY_PLAIN, 3,(0, 0, 0), 2, cv2.LINE_AA)
        cv2.imwrite("gomi.png",self.boardimg)

        for x in range(1,9):
            for y in range(1,9):
                if self.board[x,y] == 1:
                    cv2.circle(self.boardimg, (    ((y-1)*35+17)*2+100,  ((x-1)*35+17)*2+100  ), 12*2, (0, 0, 0),thickness=-1)
                elif self.board[x,y] == -1:
                    cv2.circle(self.boardimg, (  ((y-1)*35+17)*2+100,((x-1)*35+17)*2 + 100), 12*2, (255,255,255),thickness=-1)

                if self.canput_board[x,y] == 1:
                    self.boardimg[(x-1)*66+(4*x)+100 : x*66 + (4*x)+100, (y-1)*66+(4*y)+100 : y*66 + (4*y) + 100] = [200,255,200]

                if self.x == x and self.y == y:
                    cv2.circle(self.boardimg, (    ((y-1)*35+17)*2+100,  ((x-1)*35+17)*2+100  ), 4*2, (0, 0, 255),thickness=-1)


        blackcount = np.count_nonzero(self.board == 1)
        whitecount = np.count_nonzero(self.board == -1)
        
        cv2.putText(self.boardimg, f"Black: {blackcount}", (100,350*2),cv2.FONT_HERSHEY_PLAIN, 2,(0, 0, 0), 3, cv2.LINE_AA)
        cv2.putText(self.boardimg, f"White: {whitecount}", (100,370*2),cv2.FONT_HERSHEY_PLAIN, 2,(0, 0, 0), 3, cv2.LINE_AA)

        if self.turn==-1: cv2.putText(self.boardimg, f"Turn: White", (550,370*2),cv2.FONT_HERSHEY_PLAIN, 2,(0, 0, 0), 3, cv2.LINE_AA)
        else: cv2.putText(self.boardimg, f"Turn: Black", (550,370*2),cv2.FONT_HERSHEY_PLAIN, 2,(0, 0, 0), 3, cv2.LINE_AA)

        return self.boardimg