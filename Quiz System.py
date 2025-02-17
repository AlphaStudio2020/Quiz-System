import discord
from discord.ext import commands, tasks
from discord.utils import get

# Setze deinen Token hier ein
TOKEN = 'TOKEN_HIER'

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Beispiel-Fragen und Antworten
questions = [
    {"question": "Frage 1", "answer": "1"},
    {"question": "Frage 2", "answer": "2"},
    {"question": "Frage 3", "answer": "3"},
    {"question": "Frage 4", "answer": "4"},
    {"question": "Frage 5", "answer": "5"},
    {"question": "Frage 6", "answer": "6"},
    {"question": "Frage 7", "answer": "7"},
    {"question": "Frage 8", "answer": "8"},
    {"question": "Frage 9", "answer": "9"},
    {"question": "Frage 10", "answer": "10"},
]

signup_users = []
user_channels = {}
quiz_duration = 60  # Dauer bis zur Erstellung der Chats in Sekunden
announcement_channel_id = ID_CHAT # Ersetze dies mit der ID deines Ankündigungskanals


@bot.event
async def on_ready():
    print(f'Bot ist bereit und eingeloggt als {bot.user.name}')


@bot.command(name="anmelden")
async def signup(ctx):
    user = ctx.author

    if user in signup_users:
        await ctx.send("Du bist bereits für das Quiz angemeldet!")
    else:
        signup_users.append(user)
        await ctx.send(f"{user.mention} hat sich erfolgreich für das Quiz angemeldet!")


@tasks.loop(seconds=quiz_duration)
async def start_quiz():
    if signup_users:
        for user in signup_users:
            await create_private_channel(user)
        signup_users.clear()


@bot.command(name="start")
async def start_quiz_timer(ctx):
    start_quiz.start()
    await ctx.send(f"Der Quiz wird in {quiz_duration} Sekunden gestartet!")


async def create_private_channel(user):
    guild = user.guild

    if user.id in user_channels:
        return

    # Erstelle einen privaten Kanal nur für den Benutzer
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        user: discord.PermissionOverwrite(read_messages=True)
    }
    channel = await guild.create_text_channel(f"quiz-{user.name}", overwrites=overwrites)

    user_channels[user.id] = {
        "channel": channel,
        "question_index": 0
    }

    await channel.send(f"Willkommen zu deinem privaten Quiz, {user.mention}!")
    await ask_question(user)


async def ask_question(user):
    user_data = user_channels[user.id]
    channel = user_data["channel"]
    question_index = user_data["question_index"]

    if question_index < len(questions):
        question = questions[question_index]["question"]
        await channel.send(question)
    else:
        await announce_winner(user)


async def announce_winner(winner):
    guild = winner.guild
    announcement_channel = get(guild.text_channels, id=announcement_channel_id)

    if announcement_channel:
        await announcement_channel.send(f"Herzlichen Glückwunsch {winner.mention}, du hast das Quiz gewonnen!")

    # Schließe alle Quiz-Kanäle
    for user_id, user_data in user_channels.items():
        channel = user_data["channel"]
        await channel.delete()

    user_channels.clear()


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    user = message.author
    if user.id in user_channels:
        user_data = user_channels[user.id]
        channel = user_data["channel"]
        question_index = user_data["question_index"]

        if message.channel == channel:
            correct_answer = questions[question_index]["answer"]

            if message.content.lower() == correct_answer.lower():
                await message.channel.purge(limit=100)
                user_data["question_index"] += 1
                await ask_question(user)
            else:
                await channel.send("Das ist leider nicht korrekt. Versuche es nochmal!")

    await bot.process_commands(message)


# Startet den Bot
bot.run(TOKEN)
