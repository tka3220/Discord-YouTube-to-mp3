# インストールした discord.py を読み込む
import discord
import youtube_dl
# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'NzU3ODYzNDM0MDA3MjE2MTY5.X2mlUw.waZViDmt83u1gVw7N4aCg1DgEKY'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    #if message.content == '/neko':
    #await message.channel.send('にゃーん')
    naiyou=message.content
    if naiyou.find("!落とせ")!=-1:
        await message.channel.send("うい")
        url=naiyou[4:]
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl':  url + '.%(ext)s',
            'postprocessors': [
                {'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                 'preferredquality': '192'},
                {'key': 'FFmpegMetadata'},
            ],
        }
        ydl = youtube_dl.YoutubeDL(ydl_opts)
        info_dict = ydl.extract_info(url, download=True)
        await message.channel.send("うい")
        #await message.channel.send_file("music.mp3")
        await message.channel.send(file=discord.File(url+'.mp3'))
        naiyou=""
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
