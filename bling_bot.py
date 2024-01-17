import discord

# 파일 r모드로 열기
f = open('token.txt', 'r')

# readline() 함수 이용해서 한 라인씩 읽어오기
token = f.readline()
# print(token)

intents=discord.intents.default()
bot = discord.Client(intents=intents)
