import os
import requests
import json
import asyncio
import discord
from discord.ext import commands
import random

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="g>", intents=intents)


@bot.event
async def on_connect():
  print("your bot is online")


@bot.command()
async def sus(ctx):
  await ctx.send(
    "I identify as amongsexual, that is my identity, my gender and also my entire personality. If you dare to oppose me, I shall summon IMPOSTOR from among us, he will protect me but also murder your entire family. I will kill all amongphobes, I am not a freak, I am a proud amongsexual, imagine being amongphobe like imagine. Today I came out as amongsexual to my parents, my little brother trolled me and showed me a pic of Pink, one of the crewmates, I couldn't resist when I saw the pic, so I opened my zipper and started wanking, damn Pink is so hot. The next day my mom gave my phone to my cousin, and then she brought me to the therapist, idk why, Pink is hot though. My mom said that my aunt died and that we are going to her funeral the next morning. As soon as she left the room crying I busted out laughing because it reminded me of among us a popular video game. So as we were riding in the car I was thinking about saying dead body reported at the funeral. When we finally arived I screamed dead body reported, everyone was looking me like if some sort of a weirdo. Then I remembered that my grandfather's sister fell in the vents and died when she was 2 years old. So I said grandpa's sister sus she vented. My grandfather started crying and everyone was screaming at me instead of laughing. My mom took my x box and said that I am going to therapist tommorow. Idk my mom is acting kinda sus."
  )
@bot.command()
async def libs(ctx):
  await ctx.send(
    "Now I got a message for all you liberals out there. You want my gun? My firearm?! Come take it from me. Just walk through my door! Come into my home, and take it from me! With your weak, soft... liberal, girlish hands... Just try to put those hands on me! Those soft liberal hands... Put them on me! On my body! Just slowly... gently... dragging your fingers up and down my arm giving me goosebumps. You want my gun?! Come kiss me for it! But not like right away, don't be too obvious with it. Let's do that thing where we- our faces get close to each other and you know what's gonna happen it's just a matter of time you just stare at each others lips but you're waiting for the right signal to give yourself over to them completely, like in a Walk To Remember... Come do that for my gun! Bite my lip and play with my hair... for my firearm! If you want my gun, come spank me for it! Not like-Not like too hard.. but like like.. still hard, you know? Li-Like-Like hurt me but make me feel safe at the same time. You pussy liberals!"
  )

@bot.command()
async def rng(ctx, lowerbound, upperbound):
  if lowerbound.isdigit() and upperbound.isdigit():
    x = random.randint(lowerbound, upperbound)
    await ctx.send(x)
  else:
    await ctx.send("make sure to send 2 numbers separated with spaces like this: >rng 1 10")


@bot.command()
async def add(ctx, num1, num2):
  if num1.isdigit() and num2.isdigit():
    newnum = int(num1) + int(num2)
    await ctx.send(newnum)
  else:
    await ctx.send("make sure to send 2 numbers separated with spaces like this: >add 1     10")


@bot.command()
async def subtract(ctx, num1, num2):
  if num1.isdigit() and num2.isdigit():
    newnum = int(num1) - int(num2)
    await ctx.send(newnum)
  else:
    await ctx.send("make sure to send 2 numbers separated with spaces like this: >subtract 1  10")


@bot.command()
async def multiply(ctx, num1, num2):
  if num1.isdigit() and num2.isdigit():
    newnum = int(num1) * int(num2)
    await ctx.send(newnum)
  else:
    await ctx.send("make sure to send 2 numbers separated with spaces like this: >multiply 2 10")


@bot.command()
async def divide(ctx, num1, num2):
  if num1.isdigit() and num2.isdigit():
    newnum = int(num1) / int(num2)
    await ctx.send(newnum)
  else:
    await ctx.send("make sure to send 2 numbers separated with spaces like this: >divide 4 2")


listp = ['download (5).jpg', 'download (6).jpg', 'download (7).jpg', 'download (8).jpg', 'download (9).jpg', 'download (10).jpg']


@bot.command()
async def pics(ctx):
  x = random.randint(0, 5)
  await ctx.send(file=discord.File(listp[x]))


@bot.command()
async def rps(ctx, rps):
  rorpors = random.randint(1, 3)
  if rps == "rock" and rorpors == 1:
    await ctx.send("its a tie, you picked rock and I picked rock")
  elif rps == "rock" and rorpors == 2:
    await ctx.send("you lost, you picked rock and I picked paper")
  elif rps == "rock" and rorpors == 3:
    await ctx.send("you win, you picked rock and I picked scissors")
  elif rps == "paper" and rorpors == 1:
    await ctx.send("you win, you picked paper and I picked rock")
  elif rps == "paper" and rorpors == 2:
    await ctx.send("its a tie, you picked paper and I picked paper")
  elif rps == "paper" and rorpors == 3:
    await ctx.send("you lost, you picked paper and I picked scissors")
  elif rps == "scissors" and rorpors == 1:
    await ctx.send("you lost, you picked scissors and I picked rock")
  elif rps == "scissors" and rorpors == 2:
    await ctx.send("you win, you picked scissors and I picked paper")
  elif rps == "scissors" and rorpors == 3:
    await ctx.send("its a tie, you picked scissors and I picked scissors")
  else:
    await ctx.send("type g>rps (rock/paper/scissors)")

@bot.command()
async def ball8(ctx):
  resp = random.randint(1, 8)
  if resp==1:
    await ctx.send("don't count on it")
  elif resp==2:
    await ctx.send("do it when pigs fly")
  elif resp==3:
    await ctx.send("my sources say yes")
  elif resp==4:
    await ctx.send("its a trap")
  elif resp==5:
    await ctx.send("let me watch it")
  elif resp==6:
    await ctx.send("thats crazy")
  elif resp==7:
    await ctx.send("maybe")
  elif resp==8:
    await ctx.send("try again")


@bot.command()
async def joke(ctx):
  url='https://official-joke-api.appspot.com/random_joke'
  req=requests.get(url)
  data=req.json()
  setup=data["setup"]
  await ctx.send(setup)
  punchline=data["punchline"]
  await asyncio.sleep(3)
  await ctx.send(punchline)

@bot.command()
async def weather(ctx, zip):
  _weather=os.environ['apikey']
  url='https://api.openweathermap.org/data/2.5/weather?zip='+zip+',us&appid='+_weather
  req=requests.get(url)
  data=req.json()
  weather=data["weather"][0]["description"]
  temp=data["main"]["temp"]
  F = 1.8*(temp-273) + 32
  F=round(F,1)
  await ctx.send(weather+" "+ str(F) +" degrees F")

@bot.command()
async def copypasta(ctx):
  subreddit = 'copypasta'
  count = 1
  timeframe = 'hour' #hour, day, week, month, year, all
  listing = 'top' # controversial, best, hot, new, rising, top
  top_post = get_reddit(subreddit,count,timeframe,listing)
  title = top_post['data']['children'][0]['data']['title']
  text = top_post['data']['children'][0]['data']['selftext']
  await ctx.send(title)
  await ctx.send(text)
 
def get_reddit(subreddit,count,timeframe,listing):
    base_url = f'https://www.reddit.com/r/{subreddit}/{listing}.json?count={count}&t={timeframe}'
    request = requests.get(base_url, headers = {'User-agent': 'yourbot'})
    return request.json()

@bot.command()
async def gender(ctx, name):
  _pic=os.environ['apikey2']
  url = "https://api.apilayer.com/gender/gender/by-first-name"

  payload = ("%7B%22first_name%22%3A%22"+name+"%22%7D").encode("utf-8")
  headers= {
    "apikey": "cmhb6ysHzWvDZZTgojeHzeZxuN1DFXUz"
  }

  response = requests.request("POST", url, headers=headers, data = payload)

  status_code = response.status_code
  result = response.text
  await ctx.send(result)

@bot.command()
async def george(ctx):
  await ctx.send("Current functions are g>add g>subtract g>multiply g>divide g>pics g>rps g>rng g>ball8 g>copypasta ")
  


my_secret = os.environ['token']
bot.run(my_secret)
