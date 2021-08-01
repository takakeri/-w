from .othello import Othello
import cv2

class Session():
    def __init__(self):
        """
        'channel_id':
        {
            'board':numpy配列
            'turn':turn
            'user1':user1
            'user2':user2

        }
        """
        self.session_dict = {}

    #セッションを作成します(部屋id,誰対誰(id管理)の戦いか、どのチャンネルidでの戦いか)
    def create(self,channel_id,user1,user2):
        othello = Othello()
        othello.__init__()
        
        self.session_dict[str(channel_id)] = {
            "board": othello.board,
            "turn": 1,
            "user1": user1,
            "user2": user2
        }

        img = othello.img_update()
        cv2.imwrite(f"tmp/{channel_id}.png",img)
        return f"tmp/{channel_id}.png"


    #セッションを破棄します。
    def delete(self,channel_id):
        self.session_dict.pop(str(channel_id))



    #セッションに応じてゲームを進行します。
    def move(self,message,channel_id):
        othello = Othello()
        #セッションが存在するか
        x = message.content.split(" ")[1].split(",")[0]
        y = message.content.split(" ")[1].split(",")[1]
        if othello.turn == 1: t = 1
        else: t=2

        if str(message.author.id) != str(self.session_dict[str(channel_id)][f'user{t}']):
            return "あなたのターンではありません",None

        if channel_id not in self.session_dict:
            othello.turn = self.session_dict[str(channel_id)]["turn"]
            othello.board = self.session_dict[str(channel_id)]["board"]
            self.canput_continue = 0
            while True:
                othello.search()
                othello.img_update()
                self.canput_continue+=1
                turn="白"
                if othello.turn==1:
                    turn="黒"

                # 終了処理
                if self.canput_continue>=3:
                    img = othello.img_update()
                    cv2.imwrite(f"tmp/{channel_id}.png",img)
                    result = othello.gameend()
                    self.delete(channel_id)
                    return result,f"tmp/{channel_id}.png"

                # 正常な動き
                self.canput_continue=0

                if othello.play(int(x),int(y)) == False:
                    return "そこはおけないよ",None

                #置くところができないならターンスキップ(どちらも置けなかったら終了処理)
                if othello.search()==False:
                    othello.turn*=-1
                    if othello.search()==False:
                        img = othello.img_update()
                        cv2.imwrite(f"tmp/{channel_id}.png",img)
                        result = othello.gameend()
                        self.delete(channel_id)
                        return result,f"tmp/{channel_id}.png"
                
                neturn="白"
                if othello.turn==1:
                    neturn="黒"

                img = othello.img_update()
                cv2.imwrite(f"tmp/{channel_id}.png",img)

                self.session_dict[str(channel_id)]["turn"] = othello.turn
                self.session_dict[str(channel_id)]["board"] = othello.board
                return f"次は{neturn}の番です",f"tmp/{channel_id}.png"

        return "セッションが存在しません。[d!start <ユーザー1> <ユーザー2>] で対局を開始してください。"