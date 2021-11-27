import discord
import datetime

now = datetime.datetime.now()
time = f"{str(now.year)}년 {str(now.month)}월 {str(now.day)}일 {str(now.hour)}시 {str(now.minute)}분 {str(now.second)}초"

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("online")
    game = discord.Game("여행자와 함께")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.author.client:
        return None
    await client.process_commands(message)

@client.event
async def on_message(message):
    if message.content.startswith("디스코드"):
        await message.channel.send("https://tinyurl.com/Seoyul")

    if message.content.startswith("디코"):
        await message.channel.send("https://tinyurl.com/Seoyul")

    if message.content.startswith("안녕"):
        await message.channel.send(f'{message.author.mention}안녕')

    if message.content.startswith("비상식량"):
        await message.channel.send(f'{message.author.mention}뭐야! 마스코트보다 못하잖아!')

    if message.content.startswith("유미"):
        await message.channel.send(f'{message.author.mention}유도미사일')

    if message.content.startswith("피오라"):
        await message.channel.send(f'{message.author.mention}스플릿 빼면 시체 , 불리한 상성도 뒤집는 응수')

    if message.content.startswith("페이몬"):
        await message.channel.send(f'{message.author.mention}네')

    if message.content.startswith("q삭제"):
        if message.author.guild_permissions.manage_messages:
            try:
                amount = message.content[6:]
                await message.channel.purge(limit=int(amount))
                await message.channel.send(f"**{amount}**개의 메시지삭제")
            except ValueError:
                await message.channel.send("삭제하실 메시지의 **수**를 입력해 주세요.")
        else:
            await message.channel.send("너는 들어줄수 없어.")

    if message.content.startswith("고?"):
        await message.channel.send("어디로?")

    if message.content.startswith("AFK"):
        await message.channel.send("Away from keyboard의 약칭이다.")

@client.event
async def on_message_edit(before, after):
    channel = client.get_channel(913821198528438342)
    embed = discord.Embed(title=f"수정된 메시지", description=f"유저 : {before.author.mention} 채널 : {before.channel.mention}", color=0xFF9900)
    embed.add_field(name="수정 전", value=before.content, inline=True)
    embed.add_field(name="수정 후", value=after.content, inline=True)
    embed.set_footer(text=f"{before.guild.name} | {time}")
    await channel.send(embed=embed)

@client.event
async def on_message_delete(message):
    channel = client.get_channel(913821198528438342)
    embed = discord.Embed(title=f"삭제된 메시지", description=f"유저 : {message.author.mention} 채널 : {message.channel.mention}", color=0xFF0000)
    embed.add_field(name="삭제된 내용", value=f"내용 : {message.content}", inline=False)
    embed.set_footer(text=f"{message.guild.name} | {time}")
    await channel.send(embed=embed)


client.run(token)
