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

# def picturemake(prompt):
#   r = requests.post(
#   "https://api.deepai.org/api/text2img",
#     data={
#         'text': prompt,
#     },
#     headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
# )
#   return(r.json())

@bot.command()
async def game(ctx):
  button1=Button(label="start", style=discord.ButtonStyle.green, disabled=False)
  
  async def game1(interaction):
    button11=Button(label="What do you MEAN?!?!", style=discord.ButtonStyle.green, disabled=False)
    button12=Button(label="Why? That's just stupid.", style=discord.ButtonStyle.green, disabled=False)
    button13=Button(label="Sure", style=discord.ButtonStyle.green, disabled=False)

    async def game11(interaction):
      button111=Button(label="Escape", style=discord.ButtonStyle.green, disabled=False)
      button112=Button(label="Proceed down the path.", style=discord.ButtonStyle.green, disabled=False)
      button113=Button(label="World-Ending?", style=discord.ButtonStyle.green, disabled=False)

      async def game111(interaction):
        await ctx.send("-You run quickly back down the path you came, running through the brambles of trees deeper and deeper into the forest without a glance back. Suddenly you hear some say, 'We sholud keep running', you ask them who they are and they say 'I'm the voice of reason. I'm a product of your choices, here to guide you down this path. I'm here to help. Ah, finally caught up. You sure ran fast. I see you caught a stray... Well, I didn't expect you to try and escape for the least! Lets get this back on track. -In the blink of an eye you appear back on the stone path, once again where you started. Now, where were we... Ah, let's get back on track and kill Pikachu!'. You try to escape. -You run quickly back down the path you came, running through the brambles of trees deeper and deeper into the forest without a glance back. It seems oddly familiar... Are we back at the same place. HUFF HUFF! This HUFF has gone on HUFF... This has gone on long enough... I'm giving you one more chance! -In the blink of an eye you appear back on the stone path, once again where you started. -You sprint ever faster, and finally make it to a clearing in the woods... -Something is wrong. -Trees in the distance are disappearing, the earth shattering, and the sky turns black. -This world is ending. Ending 1: Escaped")
        #await ctx.send(picturemake("escaped"))
      async def game112(interaction):
        button1121=Button(label="Are we finally here?", style=discord.ButtonStyle.green, disabled=False)
        button1122=Button(label="I can't do this anymore!", style=discord.ButtonStyle.green, disabled=False)
        button1123=Button(label="Grab the Knife", style=discord.ButtonStyle.green, disabled=False)
        async def game1121(interaction):
          await ctx.send("No, still more to go. -You begin to lose your mind, and your legs begin to fail you -You cant stand anymore, but the trail still continues -You die. Ending 7: Endless Journey")
          #await ctx.send(picturemake("endless journey"))
        async def game1122(interaction):
          await ctx.send("What? Are you serious right now? You think we came all this way for a picnic... I'm done I'm done with this bullshit. I'm ending this adventure here. Ending 6: Weakling")
          #await ctx.send(picturemake("weakling"))
        async def game1123(interaction):
          button11231=Button(label="Stab Him", style=discord.ButtonStyle.green, disabled=False)
          button11232=Button(label="Run", style=discord.ButtonStyle.green, disabled=False)
          async def game11231(interaction):
            await ctx.send("- You stab Pikachu deep in the heart, and the creature starts morphing in impossible ways. - Your muscles start to contract against your will as millions of volts of energy pass through your body, reducing you to ashes. Ending 2: Thunderbolt")
            #await ctx.send(picturemake("thunderbolt"))
          async def game11232(interaction):
            await ctx.send("- As Pikachu morphs into a monsterous form, you make your escape - You don't look back until your spine shatters from the thunderous hit of Pikachu's tail. You Die. Ending 3: Iron Tail")
            #await ctx.send(picturemake("iron tail"))
          button11231.callback=game11231
          button11232.callback=game11232
          view1123=View()
          view1123.add_item(button11231)
          view1123.add_item(button11232)
          await ctx.send("Oh, that knife.. seems you found the right tool for the job. -A gust of wind blows the tall grass to the side revealing a deep pit in the middle of the clearing -You walk closer, and peer in, seeing Pikachu chained up in the center Now get in there and end him before the world ends. Don't get cocky. You know Pikachu has the moveset of zeus, I personally dont think we can win this fight. Ugh, another stray. I forgot to introduce myself, how silly. I'm the voice of fear. i'm here to help. -You hear a guttural screech from the pit below reminding you of Pikachu, or whatever it is, waiting for you. -Pikachu rises from the pit, and you see his monsterous fram, this is not the Pikachu you know KILL HIM QUICKLY!! We're so dead.", view=view1123)
        button1121.callback=game1121
        button1122.callback=game1122
        button1123.callback=game1123
        view112=View()
        view112.add_item(button1121)
        view112.add_item(button1122)
        view112.add_item(button1123)
        await ctx.send("-You walk down the winding path as time starts to melt, and seconds turn to minutes which turn to hours. -You don't know just how long you have been walking down the road, and your mind begins to go numb. -That is until, you reach a clearing in the woods.", view=view112)
      async def game113(interaction):
        button1131=Button(label="Proceed down the path", style=discord.ButtonStyle.green, disabled=False)
        button1132=Button(label="Sit and wait", style=discord.ButtonStyle.green, disabled=False)
        async def game1131(interaction):
          await ctx.send("-You walk wearily down the path until your mind goes numb. -You cant stop thinking about the end of the world, and it bring you the strength to keep treading -Through it all you maintain your sanity, and finally resolve to kill Pikachu -Regardless of why you are here, you have a job to do, so you choose to fight -You make it to the clearing with Pikachu, waiting for you deep in a pit. -You have arrived at your destination. -You fight with every last ounce of your being, kicking and punching through the endless shock sent into your body. -You start to lose your ability to move, and your bones begin to break from the numerous attacks. -You put up a worthy fight, but Pikachu still wins in the end. Ending 4: Fallen Hero")
          #await ctx.send(picturemake("fallenhero"))
        async def game1132(interaction):
          await ctx.send("Ha! Ha. Nice one, but we have a lot of ground to cover, so let's move! Fine. Goddammit. Hey could we get an ending in here! Ending 5: Stuck in place")
          #await ctx.send(picturemake("stuck in place"))
        button1131.callback=game1131
        button1132.callback=game1132
        view113=View()
        view113.add_item(button1131)
        view113.add_item(button1132)
        await ctx.send("This world has different rules than you're used to. All you have to do is put an end to him. I know this is hard to understand, but you only have one job here.", view=view113)
      button111.callback=game111
      button112.callback=game112
      button113.callback=game113
      view11=View()
      view11.add_item(button111)
      view11.add_item(button112)
      view11.add_item(button113)
    
      await ctx.send("As difficult as this seems if we don't kill pikachu now this world will end. Now... I've explained enough, let's go", view=view11)
    async def game12(interaction):
      button121=Button(label="Refuse", style=discord.ButtonStyle.green, disabled=False)
      button122=Button(label="Let the world end.", style=discord.ButtonStyle.green, disabled=False)

      async def game121(interaction):
        await ctx.send("You think I'm some sort of pushover. I don't need to wait for your permission. You're going to regret not answering me. -The ground begins to shake, and you see the yellowy mass of Pikachu rise from the ground -This is much more demonic version of Pikachu than you remember. -This is not part of any pokemon games you remember. -You cannot escape his hunger. Ending 8: Devoured (don't anger the narrator)")
        #await ctx.send(picturemake("devoured"))
      async def game122(interaction):
        button1221=Button(label="Ressist", style=discord.ButtonStyle.green, disabled=False)
        button1222=Button(label="Succumb", style=discord.ButtonStyle.green, disabled=False)
        async def game1221(interaction):
          await ctx.send("-You resist the control with every ounce of strength within your body. 'I'll help you. I'm the voice of strength!' With newfound strength, you wrench back control of your body Take that puppeteer! -You hear no response, and begin to feel chills. -The world begins to turn cold. We won... Right? Ending 9: Abandoned")
          #await ctx.send(picturemake("abandoned"))
        async def game1222(interaction):
          await ctx.send("-You let your body be taken control of, and it begins to move again -Your body begins to trudge down the path, step after step -However, the end never seems to come. -The path seems to continue on forever, and ever. Are you going to die here? -Your body collapses motionless on the floor Ending 10: Puppet")
          #await ctx.send(picturemake("puppet"))
        button1221.callback=game1221
        button1222.callback=game1222
        view122=View()
        view122.add_item(button1221)
        view122.add_item(button1222)
        await ctx.send("no. no. NO NO! This is MY GAME! These are MY RULES! Ah! I know! -Your body begins to move without your consent -You begin to trudge down the road.", view=view122)
      button121.callback=game121
      button122.callback=game122
      view12=View()
      view12.add_item(button121)
      view12.add_item(button122)
    
      await ctx.send("It is anything but stupid. If you don't kill Pikachu, this world will end. Now if you understand let's move, we have a lot of ground to cover. Please don't make this hard. Let's just go, you are the only one who can do this.", view=view12)
    async def game13(interaction):
      button131=Button(label="Grab it", style=discord.ButtonStyle.green, disabled=False)
      button132=Button(label="Leave it on the table", style=discord.ButtonStyle.green, disabled=False)

      async def game131(interaction):
        await ctx.send("-You grab the knife, and hear a 'PIKACHUUU' coming from the hole below followed by a lightning bolt. -You look over and see Pikachu wrench itself out of the hole. Kill him!. LET'S GET THIS LIGHTNING RAT! -You grip the knife with both hands and charge Pikachu, driving the knife deep into his shoulder. Before he has a chance to attack, AGAIN! -You slash and slash until Pikachu ceases his movement! Looks like you beat him, congratulations, you S@V3D the w0r1d Ending 11: Murderer!")
        #await ctx.send(picturemake("murder"))
      async def game132(interaction):
        await ctx.send("'Knife? You think I need a knife for a electric type pokemon.' you tell him You grab a great ball, and chuck it into the fray, summoning a earth type onix. Your onix slams into Pikachu, knocking him out instantly. You grab an empty great ball and use it to capture pikachu. You've won..... Ending 12: Capture")
        #await ctx.send(picturemake("capture"))
      button131.callback=game131
      button132.callback=game132
      view13=View()
      view13.add_item(button131)
      view13.add_item(button132)
    
      await ctx.send("That's the spirit. Just don't get cold feet on me, if you can't kill him, the world ends.Wonderful, now let's get a move on, there's no time to waste. -You walk farther and farther into the woods until the trees start to become scarce. -A clearing forms in the midst of the woods, and you see a table in front of a deep pit.Go grab the knife, you'll need it. A knife materialises on the table in front of you.", view=view13)
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