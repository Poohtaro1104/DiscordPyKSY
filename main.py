import discord
import sys
import datetime
from discord.ext import commands


Token = 'ODkxNTY3NTMzMjA1ODk3MjQ2.YVAO-A.SaqEB5hzZrV1GQrp0nRqi-ZZq3c'

client = discord.Client()

@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('Botが起動しました')

@client.event
async def on_message(message): 
    if message.content.startswith('.SDB'):#.SDBが入力されたら強制終了
        if message.author.guild_permissions.administrator:
            await message.channel.send('Botを終了します')
            await client.logout()
            await sys.exit()
        else:
            await message.channel.send('管理者のみBotを終了することができます')
    
    #------------------
    
    if message.content.startswith('.g'):
        nowTime = datetime.datetime.today().hour
        if 0 <= nowTime < 3:
            await message.channel.send('深夜に失礼します')
        elif 3 <= nowTime < 6:
            await message.channel.send('おはよ～')
        elif 6 <= nowTime < 9:
            await message.channel.send('おはよう!')
        elif 9 <= nowTime < 12:
            await message.channel.send('ohayo-')
        elif 12 <= nowTime < 15:
            await message.channel.send('こんちには')
        elif 15 <= nowTime < 18:
            await message.channel.send('やあ、もしかしておやつ食べてた？')
        elif 21 <= nowTime < 24:
            await message.channel.send('夜遅くにごめんね')
    
    #------------------
    
    if message.content.startswith(".IP"):
        await message.channel.send(" \".IP help\" で詳細を表示\n")
    
    if message.content.startswith('.IP help'):
        msg = '#-------.IPコマンドの使い方-------#\n    .IP help                => IPコマンドの使い方の表示\n       ~ ours               => KSYサーバーのIPアドレスを表示\n       ~ Hypixel         => Hypixelのアドレスを表示\n       ~ セプルシオ => セプルシオサーバーのアドレスを表示'
        await message.channel.send(msg)
    
    if message.content.startswith('.IP ours'):
        #subprocess.run(["C:\\Users\\プーちゃん大統領\\OneDrive\\デスクトップ\\Discord\\Bot\\pybot_s_ip"])
        f = open("IP.txt","r")
        await message.channel.send("IPアドレス↓")
        for ip in f.read().split(",")[:-1]:
            await message.channel.send("\""+ip+"\"")
        #await message.channel.send(get_ip())
    
    if message.content.startswith('.IP Hypixel'):
        await message.channel.send("Hypixelサーバーアドレス↓")
        await message.channel.send("\"mc.hypixel.net\" | IP : 209.222.115.36")
    
    if message.content.startswith('.IP セプルシオ'):
        await message.channel.send("セプルシオサーバーアドレス↓")
        await message.channel.send("\"game.mcsvr.online:35725\"")
    
    #------------------
    
    def check(msg):
        return msg.author == message.author
    
    if message.content.startswith(".sover"):
        await message.channel.send("理由 : ")
        wait_message = await client.wait_for("message",check=check)
        await message.channel.send("ごめん！"+wait_message.content+"だから終わるね")
    
    if message.content.startswith(".help"):
        if message.author.bot:
            return
        msg = ".help\n=>コマンドのヘルプを表示\n.IP\n=>いろいろなサーバーのアドレスを表示\n.sover\n=>理由を入力して終わることを教える\n.g\n=>時刻にあった挨拶をする"
        await message.channel.send(msg)
    
    if message.content.startswith(".test"):
        await message.channel.send("てすとめっせーじ")

client.run(Token)