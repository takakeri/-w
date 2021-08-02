# インストールした discord.py を読み込む
import discord
from module.session_control import Session
import io
from config import TOKEN

session = Session()

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    if message.author.bot:
        return 0

    # help
    if message.content == "d!help":
        await message.channel.send(open("./help.txt",encoding="utf-8").read())
    # "dothello"を含むチャンネル以外では使えない
    if "dothello" not in message.channel.name:
        return 0

    if message.content.startswith("d!stop") and ((message.author.guild_permissions.administrator) or str(message.author.id) == str(session.session_dict[str(message.channel.id)]["user1"]) or str(message.author.id) == str(session.session_dict[str(message.channel.id)]["user2"])):
        await message.channel.send("対局を中止しました")
        session.delete(message.channel.id)
    
    if message.content.startswith("d!start"):
        # チャンネルにすでにセッションがある場合実行できない
        if str(message.channel.id) in list(session.session_dict.keys()):
            await message.channel.send("この部屋は今つかわれてるから使えないよ。対局が終わるか、対局中の二人か権限者が[d!stop]と打つと使えるようになります。")
            return 0
        texts = message.content.split(" ")
        if len(texts) >= 3:
            try:
                user1 = await client.fetch_user(int(texts[1].replace("<","").replace(">","").replace("@!","")))
                user2 = await client.fetch_user(int(texts[2].replace("<","").replace(">","").replace("@!","")))
            except:
                user1,user2=None,None
            if user1==None or user2 == None:
                await message.channel.send("ユーザーを二人メンションしてね")
                return 0
            await message.channel.send(f"""{user1} {user2} の対局開始\n\n黒: {user1}\n白: {user2}\n\n先行: 黒\n\n自分の番の時に[set x座標,y座標]と打ち込んで石を置けます""")
            user1 = texts[1].replace("<","").replace(">","").replace("@!","")
            user2 = texts[2].replace("<","").replace(">","").replace("@!","")
            imgpath = session.create(message.channel.id,user1,user2)
            await message.channel.send(file=discord.File(imgpath))

    if message.content.startswith("set "):
        res,imgpath = session.move(message,message.channel.id)
        if imgpath!=None:
            await message.channel.send(file=discord.File(imgpath))
        await message.channel.send(res)
            
        

        

# Botの起動とDiscordサーバーへの接続
print("aaa")
client.run(TOKEN)