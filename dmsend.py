
# 봉순#4888 : MASS DM BOT SOURCE
# 오픈소스 이용하여 제작되었습니다


import discord
import asyncio
import datetime

client = discord.Client()

@client.event
async def on_ready():
    print("봇이 정상적으로 실행되었습니다.")
    game = discord.Game('유저분들에게 디엠 보내기')
    await client.change_presence(status=discord.Status.online, activity=game)

#/dm {할말}로 전체DM 전송
@client.event
async def on_message(message):
    if message.content.startswith('!dm'):
        for i in message.guild.members:
            if i.bot == True:
                pass
            else:
                try:
                    msg = message.content[4:]
                    if message.author.id == 547643059068862464:
                        embed = discord.Embed(colour=0x1DDB16, timestamp=message.created_at, title="🌸엑스트라서버 공지🌸")
                        embed.add_field(name="공지가 필요없으신분들은 차단을 해주세요(필요하실겁니다)", value=msg, inline=True)
                        embed.set_footer(text=f"discord.gg/CFupCbJ")
                        await i.send(embed=embed)
                except:
                    pass


client.run('NzI5MjkwMjM1MzIxNzc4MjE2.XwG5-Q.eMOMsLN41lK34oOrgSJMhvizmnE')
