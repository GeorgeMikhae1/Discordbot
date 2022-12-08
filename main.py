import keep_alive
import os
from discord.ui import Button, View
import requests
import asyncio
import discord
import random
from discord.ext import commands


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
    await ctx.send(
      "make sure to send 2 numbers separated with spaces like this: >rng 1 10")


@bot.command()
async def add(ctx, num1, num2):
  if num1.isdigit() and num2.isdigit():
    newnum = int(num1) + int(num2)
    await ctx.send(newnum)
  else:
    await ctx.send(
      "make sure to send 2 numbers separated with spaces like this: >add 1 10"
    )


@bot.command()
async def subtract(ctx, num1, num2):
  if num1.isdigit() and num2.isdigit():
    newnum = int(num1) - int(num2)
    await ctx.send(newnum)
  else:
    await ctx.send(
      "make sure to send 2 numbers separated with spaces like this: >subtract 1 10"
    )


@bot.command()
async def multiply(ctx, num1, num2):
  if num1.isdigit() and num2.isdigit():
    newnum = int(num1) * int(num2)
    await ctx.send(newnum)
  else:
    await ctx.send(
      "make sure to send 2 numbers separated with spaces like this: >multiply 2 10"
    )


@bot.command()
async def divide(ctx, num1, num2):
  if num1.isdigit() and num2.isdigit():
    newnum = int(num1) / int(num2)
    await ctx.send(newnum)
  else:
    await ctx.send(
      "make sure to send 2 numbers separated with spaces like this: >divide 4 2"
    )


listp = [
  'download (5).jpg', 'download (6).jpg', 'download (7).jpg',
  'download (8).jpg', 'download (9).jpg', 'download (10).jpg'
]


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
async def ball8(ctx, question):
  resp = random.randint(1, 8)
  if resp == 1:
    await ctx.send("don't count on it")
  elif resp == 2:
    await ctx.send("do it when pigs fly")
  elif resp == 3:
    await ctx.send("my sources say yes")
  elif resp == 4:
    await ctx.send("its a trap")
  elif resp == 5:
    await ctx.send("let me watch it")
  elif resp == 6:
    await ctx.send("thats crazy")
  elif resp == 7:
    await ctx.send("maybe")
  elif resp == 8:
    await ctx.send("try again")


@bot.command()
async def joke(ctx):
  url = 'https://official-joke-api.appspot.com/random_joke'
  req = requests.get(url)
  data = req.json()
  setup = data["setup"]
  await ctx.send(setup)
  punchline = data["punchline"]
  await asyncio.sleep(3)
  await ctx.send(punchline)


@bot.command()
async def weather(ctx, zip):
  _weather = os.environ['apikey']
  url = 'https://api.openweathermap.org/data/2.5/weather?zip=' + zip + ',us&appid=' + _weather
  req = requests.get(url)
  data = req.json()
  weather = data["weather"][0]["description"]
  temp = data["main"]["temp"]
  F = 1.8 * (temp - 273) + 32
  F = round(F, 1)
  await ctx.send(weather + " " + str(F) + " degrees F")


@bot.command()
async def copypasta(ctx):
  subreddit = 'copypasta'
  count = 1
  timeframe = 'hour'  #hour, day, week, month, year, all
  listing = 'top'  # controversial, best, hot, new, rising, top
  top_post = get_reddit(subreddit, count, timeframe, listing)
  title = top_post['data']['children'][0]['data']['title']
  text = top_post['data']['children'][0]['data']['selftext']
  await ctx.send(title)
  await ctx.send(text)


def get_reddit(subreddit, count, timeframe, listing):
  base_url = f'https://www.reddit.com/r/{subreddit}/{listing}.json?count={count}&t={timeframe}'
  request = requests.get(base_url, headers={'User-agent': 'yourbot'})
  return request.json()


@bot.command()
async def currency(ctx, currency2, amount):
  _currency = os.environ['apikey2']
  url = "https://api.apilayer.com/exchangerates_data/convert?to=" + currency2 + "&from=USD&amount=" + amount

  payload = {}
  headers = {"apikey": _currency}

  response = requests.request("GET", url, headers=headers, data=payload)

  status_code = response.status_code
  result = response.json()

  rate = result["info"]["rate"]

  rate *= int(amount)

  await ctx.send("$" + str(amount) + " is " + str(rate) + " in " + currency2 +
                 " from USD")






























































# def game3(ctx):
#   ctx.send("That's the spirit, just don't get cold feet on me. If you can't kill him **the world will end.**", view=choice3())

# class choice2(discord.ui.View):
#   @discord.ui.button(label="Refuse.", row=0, style=discord.ButtonStyle.primary)
#   async def first_button_callback(self, button, interaction):
#     game21()
#   @discord.ui.button(label="let the world end", row=0, style=discord.ButtonStyle.primary)
#   async def second_button_callback(self, button, interaction):
#     game22()

# def game2(ctx):
#   ctx.send("It is anything but stupid. If you don't kill Pikachu, this world will end. Now if you understand let's move, we have a lot of ground to cover. Please don't make this hard. Let's just go, you are the only one who can do this.", view=choice2())


# class choice1(discord.ui.View):
#   @discord.ui.button(label="Escape.", row=0, style=discord.ButtonStyle.primary)
#   async def first_button_callback(self, button, interaction):
#     game11()
#   @discord.ui.button(label="Proceed down the path.", row=0, style=discord.ButtonStyle.primary)
#   async def second_button_callback(self, button, interaction):
#     game12()
#   @discord.ui.button(label="World-Ending?!?!", row=0, style=discord.ButtonStyle.primary)
#   async def third_button_callback(self, button, interaction):
#     game13()


# def game1(ctx):
#   ctx.send("As difficult as this seems if we don't kill pikachu now this world will end. Now... I've explained enough, let's go.", view=choice1)



# class firstchoice(discord.ui.View):
#   @discord.ui.button(label="What do you MEAN?!?!", row=0, style=discord.ButtonStyle.primary)
#   async def first_button_callback(self, button, interaction):
#     game1()
#   @discord.ui.button(label="Why? That's just stupid.", row=0, style=discord.ButtonStyle.primary)
#   async def second_button_callback(self, button, interaction):
#     game2()
#   @discord.ui.button(label="Sure", row=0, style=discord.ButtonStyle.primary)
#   async def third_button_callback(self, button, interaction):
#     game3()

# def gamestart(ctx):
#   ctx.send("This is a decision based game. You will experience a story for which you give one of the few responses presented to you. All responses will affect the game in their own way. Type in '1', '2', or '3' when presented with your options to choose your response unless otherwise specified.")
#   ctx.send("Narrator: Now... Where were we?")
#   ctx.send("Ah... Welcome to a new adventure")
#   ctx.send("Narrator: Now... Where were we?")
#   ctx.send("You wake up on the cold hard rocks of a stony path, deep in the middle of a forest.")
#   ctx.send("Surrounded by a thicket of branches and large boulders, you stumble, but know you have to...")
#   ctx.send("              M U R D E R  P I K A C H U              ", view=firstchoice())



# class ply(discord.ui.View):
#   @discord.ui.button(label="start", row=0, style=discord.ButtonStyle.primary)
#   async def first_button_callback(self, button, interaction):
#     gamestart()

  



@bot.command()
async def game(ctx):
  button1=Button(label="start", style=discord.ButtonStyle.green, disabled=False)
  # button2=Button(label="start", style=discord.ButtonStyle.green)
  # button3=Button(label="start", style=discord.ButtonStyle.green)
  async def game1(interaction):
    button11=Button(label="What do you MEAN?!?!", style=discord.ButtonStyle.green, disabled=False)
    button12=Button(label="Why? That's just stupid.", style=discord.ButtonStyle.green, disabled=False)
    button13=Button(label="Sure", style=discord.ButtonStyle.green, disabled=False)

    async def game11(interaction):
      await ctx.send("w1")
    async def game12(interaction):
      await ctx.send("w2")
    async def game13(interaction):
      await ctx.send("w3")
    button11.callback=game11
    button12.callback=game12
    button13.callback=game13
    view1=View()
    view1.add_item(button11)
    view1.add_item(button12)
    view1.add_item(button13)
    
    await ctx.send("This is a decision based game. You will experience a story for which you give one of the few responses presented to you. All responses will affect the game in their own way. Type in '1' '2' or '3' when presented with your options to choose your response unless otherwise specified. Narrator: Now... Where were we? Ah... Welcome to a new adventure. You wake up on the cold hard rocks of a stony path, deep in the middle of a forest. Surrounded by a thicket of branches and large boulders. You stumble but know you have to...               M U R D E R  P I K A C H U              ", view=view1)
    
  button1.callback=game1
  # button2.callback=game1
  # button3.callback=game1
  view=View()
  view.add_item(button1)
  await ctx.send("click start to start the game", view=view)
    
  

    
  
@bot.command()
async def ghelp(ctx):
  ghelp = discord.Embed(
    title="menu",
    description=
    "**Current functions: ** \n**Help:** g>ghelp \n**Addition:** g>add (num1) (num2) \n**Subtraction:** g>subtract (num1) (num2)\n**Multiplication:** g>multiply (num1) (num2) \n**Division:** g>divide (num1) (num2) \n**Pictures:** g>pics \n**Rock, Paper, Scissors:** g>rps (Rock, Paper, or Scissors) \n**Random Joke:** g>joke \n**Random Number Generator:** g>rng (num1) (num2) \n**8Ball:** g>ball8 (question) \n**Weather:** g>weather (zipcode) \n**Copypasta:** g>copypasta \n**Currency Exchange:** g>currency (3 letter currency code) (amount of money)",
    color=0xFF5733)
  await ctx.send(embed=ghelp)


keep_alive.keep_alive()
my_secret = os.environ['token']
bot.run(my_secret)