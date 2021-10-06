import discord
import random
import datetime
from discord.ext import commands
from mytalkingtoken import token

# Импортируем

client = commands.Bot(command_prefix="!!") # Делаем префикс боту (префикс - то что перед названием команды)
client.remove_command('help') # Удаляем уродскую предустановленную команду help (сделаем потом новую)
time = datetime.datetime.now().time() # Время
print(f"[{time}] bot started")
time = datetime.datetime.now().time() # Время
print(f"[{time}] bot runs at",client.guilds,"guilds")
helpdata = "помогите" #open("help.txt",mode='r').read() # В файл закидываем то что будет отправляться при команде help


@client.command(pass_context = True) # Создаём команду
@commands.has_permissions(administrator = True) # Пишем какие права нужны для использования команды
async def help(ctx): # Создаём функцию в команде, в скобочках аргументы (то слова/цифры после названия команды)
    time = datetime.datetime.now().time() # Время для логов
    emb = discord.Embed(title='Здравствуйте, я MfBot! Я сейчас нахожусь в разработке поэтому данный перечень команд может быть неполным.',description=helpdata,color=discord.Color.green())
    # Про эмбеды посмотрите видеоролик на канале Фсоки
    await ctx.send(embed=emb) # Отправляем эмбед
    print(f"[{time}] help command used") # Сообщение в лог

@client.command(aliases = ["8ball"]) # Ещё команда
async def magicball(ctx): # Суть - отправляем рандомную фразу
    time = datetime.datetime.now().time()
    choice = random.randint(1,8)
    if choice == 1:
        emb = discord.Embed(title='Что сказал вам Волшебный шар... ', description="Совершенно нет! :negative_squared_cross_mark:",color=discord.Color.purple())
        await ctx.send(embed = emb)
    elif choice == 2:
        emb = discord.Embed(title='Что сказал вам Волшебный шар... ', description="Вероятность крайне мала! :question:",color=discord.Color.purple() )
        await ctx.send(embed=emb)
    elif choice == 3:
        emb = discord.Embed(title='Что сказал вам Волшебный шар... ', description="Возможно... :question:",color=discord.Color.purple() )
        await ctx.send(embed=emb)
    elif choice == 4:
        emb = discord.Embed(title='Что сказал вам Волшебный шар... ', description="50 на 50. :crystal_ball:",color=discord.Color.purple() )
        await ctx.send(embed=emb)
    elif choice == 5:
        emb = discord.Embed(title='Что сказал вам Волшебный шар... ', description="Наверное да. :crystal_ball:",color=discord.Color.purple() )
        await ctx.send(embed=emb)
    elif choice == 6:
        emb = discord.Embed(title='Что сказал вам Волшебный шар... ', description="У тебя все шансы! :stars:",color=discord.Color.purple() )
        await ctx.send(embed=emb)
    elif choice == 7:
        emb = discord.Embed(title='Что сказал вам Волшебный шар... ', description="Крайне высокие шансы. :stars:",color=discord.Color.purple() )
        await ctx.send(embed=emb)
    elif choice == 8:
        emb = discord.Embed(title='Что сказал вам Волшебный шар... ', description="Совершенно да! :white_check_mark:",color=discord.Color.purple() )
        await ctx.send(embed=emb)
    print(f"[{time}] 8ball command used {ctx.author} with answer {choice}")


@client.command(pass_context = True) # Создаём команду
@commands.has_permissions(administrator = True) # Пишем какие права нужны для использования команды
async def clear( ctx, amount = 100): # Создаём функцию в команде, в скобочках аргументы (то слова/цифры после названия команды)
    await ctx.channel.purge( limit = amount)
@client.command(pass_context = True)
async def spam(ctx,skolko,bukvi):
    for mogus in range(int(skolko)):
        await ctx.send(bukvi)

client.run(token) # Вставляем токен в кавычки

#это я, ира. так же полезна как физ чича