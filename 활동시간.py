import discord
from discord.ext import commands
from discord import app_commands
import time

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!", intents=intents)

# 음성 들어간 시간 저장
join_times = {}

# 총 활동시간 저장
voice_times = {}

@bot.event
async def on_ready():

    try:
        synced = await bot.tree.sync()
        print(f"{len(synced)}개 명령어 동기화 완료")

    except Exception as e:
        print(e)

    print(f"{bot.user} 온라인!")

# 음성채널 활동 감지
@bot.event
async def on_voice_state_update(member, before, after):

    # 들어갔을 때
    if before.channel is None and after.channel is not None:

        join_times[member.id] = time.time()

    # 나갔을 때
    elif before.channel is not None and after.channel is None:

        if member.id in join_times:

            joined = join_times[member.id]

            spent = time.time() - joined

            if member.id not in voice_times:
                voice_times[member.id] = 0

            voice_times[member.id] += spent

            del join_times[member.id]

# /활동시간
@bot.tree.command(name="활동시간", description="역할 활동시간 확인")
@app_commands.describe(역할="확인할 역할")
async def 활동시간(
    interaction: discord.Interaction,
    역할: discord.Role
):

    text = ""

    for member in 역할.members:

        seconds = int(voice_times.get(member.id, 0))

        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        secs = seconds % 60

        text += f"{member.display_name} : {hours}시간 {minutes}분 {secs}초\n"

    if text == "":
        text = "활동 기록 없음"

    await interaction.response.send_message(
        f":round_pushpin: {역할.name} 활동시간\n\n{text}"
    )

bot.run("MTUwNTA4MzA3NDI4NTc5NzQyNg.G5veE_.Q7PrIq17L1wIebJpD6D2CpM2lPI3wnZxcH-GAY")