import discord
import random
import datetime
from discord.ext import commands
from discord.ext.commands import bot
from mytalkingtoken import token
from discord.utils import get
bad_words = [' сука, блять, ебаный, ебать, мразь, дебил ']

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
    emb = discord.Embed(title='Здравствуйте, я bot slitiy!',description=helpdata,color=discord.Color.green())
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
async def clear( ctx, amount = 999999): # Создаём функцию в команде, в скобочках аргументы (то слова/цифры после названия команды)
    await ctx.channel.purge( limit = amount)


@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def spam(ctx,skolko,bukvi):
    for mogus in range(int(skolko)):
        await ctx.channel.purge(limit=0)
        await ctx.send(bukvi)


@client.command(pass_context = True) # Создаём команду
@commands.has_permissions(administrator = True) # Пишем какие права нужны для использования команды
async def kick(ctx, member: discord.Member, *, reason = None): # Создаём функцию в команде, в скобочках аргументы (то слова/цифры после названия команды)
    await ctx.channel.purge(limit = 1)
    await member.send(f'{member.name}, тебя кикнул {ctx.author.name}')
    await member.kick(reason = reason)
    emb = discord.Embed(title="Участник кикнут.",description=f"Участник {member} был кикнут {ctx.author}",colour=discord.Color.dark_red())
    await ctx.send(embed=emb)

@client.command(pass_context = True) # Создаём команду
@commands.has_permissions(administrator = True) # Пишем какие права нужны для использования команды
async def ban(ctx, member: discord.Member, *, reason = None): # Создаём функцию в команде, в скобочках аргументы (то слова/цифры после названия команды)
    await member.send(f'{member.name}, тебя забанил {ctx.author.name}')
    await ctx.channel.purge(limit = 1)
    emb = discord.Embed(title="Участник забанен.",description=f"Участник {member} был забанен {ctx.author}",colour=discord.Color.dark_red())
    await member.ban(reason = reason)
    await ctx.send(embed=emb)


@client.command(pass_context = True) # Создаём команду
@commands.has_permissions(administrator = True) # Пишем какие права нужны для использования команды
async def unban(ctx, *, member): # Создаём функцию в команде, в скобочках аргументы (то слова/цифры после названия команды)
    banned_users = await ctx.guild.bans()
    for ban_entry in banned_users:
        user = ban_entry.user
        await ctx.guild.unban( user )
    emb = discord.Embed(title="Участник разбанен.", description=f"Участник {member} был разбанен {ctx.author}",colour=discord.Color.green())
    await ctx.send(embed=emb)

@client.command(pass_context=True)  # Создаём команду
@commands.has_permissions(administrator=True)  # Пишем какие права нужны для использования команды
async def user_mute(ctx, member: discord.Member):  # Создаём функцию в команде, в скобочках аргументы (то слова/цифры после названия команды)
    mute_role = discord.utils.get( ctx.message.guild.roles, name = 'mute')
    await member.add_roles( mute_role )
    await ctx.send( f'держи язык за зубами!{member.mention}')


@client.command(pass_context=True)  # Создаём команду
@commands.has_permissions(administrator=True)  # Пишем какие права нужны для использования команды
async def send_m(ctx, member: discord.member):  # Создаём функцию в команде, в скобочках аргументы (то слова/цифры после названия команды)
    await member.send(f'{member.name}, привет от {ctx.author.name}')

@client.event
async def on_mess( message ):
    await client.process_commands( message )

    msg = message.content.lower()

    if msg in bad_words:
        await message.delete()
        await message.author.send(f'{message.author.name}, акурратнее с выражениями')

@client.command(name="role")
@commands.has_permissions(administrator=True)
async def role(ctx, role: discord.Role):
    if role in ctx.author.roles:
        await ctx.author.remove_roles(role)
    else:
        await ctx.author.add_roles(role)
        #смена ролей от Иры, отредактированно

@client.command()
async def join(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild = ctx.guild)


    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        await ctx.send(f'бот в канаве {channel}')


@client.command(pass_context=True)
async def nick(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    await ctx.send(f'Ник был изменен для {member.mention} ')

@client.command()
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)


    if voice and voice.is_connected():
        await voice.disconnect()
    else:
        voice = await channel.connect()
        await ctx.send(f'бот вышел из канавы {channel}')


players = {}
queues = {}


def check_queue(id):
    if queues[id] != []:
        player = queues[id].pop(0)
        players[id] = player
        player.start()


@client.command(pass_context=True)
async def play(ctx, url):
    server = ctx.message.server
    voice_client = bot.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))
    players[server.id] = player
    player.start()


@client.command(pass_context=True)
async def queue(ctx, url):
    server = ctx.message.server
    voice_client = bot.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))

    if server.id in queues:
        queues[server.id].append(player)
    else:
        queues[server.id] = [player]
    await bot.say('Video queued.')


@client.command(pass_context=True)
async def pause(ctx):
    id = ctx.message.server.id
    players[id].pause()


@client.command(pass_context=True)
async def stop(ctx):
    id = ctx.message.server.id
    players[id].stop()


@client.command(pass_context=True)
async def resume(ctx):
    id = ctx.message.server.id
    players[id].resume()

    return


client.run(f"{token}") # Вставляем токен в кавычки

