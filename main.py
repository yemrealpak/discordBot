import discord
# import * - kütüphanedeki tüm dosyaları içe aktarmanın hızlı bir yoludur

intents = discord.Intents.default()
intents.message_content = True  
client = discord.Client(intents=intents)

import random


def sifre_olusturucu(sifre_uzunlugu):
    ogeler = "+-/*!&$#?=@<>"
    sifre = ""

    for i in range(sifre_uzunlugu):
        sifre += random.choice(ogeler)

    return sifre


def emoji_olusturucu():
    emoji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emoji)


def yazi_tura():
    para = random.randint(0, 2)
    if para == 0:
        return "YAZI"
    else:
        return "TURA"


# Bot hazır olduğunda adını yazdıracak!
@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık')


        

 # Bot bir mesaj aldığında, aynı kanalda mesaj gönderecek!
@client.event
async def on_message(message):
      if message.author == client.user:
          return
      if message.content.startswith('selam'):
          await message.channel.send('Selam! Ben bir botum!')
      elif message.content.startswith('b'):
          await message.channel.send(emoji_olusturucu())
      elif message.content.startswith('c'):
          await message.channel.send(yazi_tura())
      elif message.content.startswith('d'):
          password = sifre_olusturucu(10)
          await message.channel.send(password)
          await message.channel.send("Şifreniz özel mesaj olarak gönderildi.")
          await message.author.send(f"Rastgele Şifreniz: {password}")
      else:
          await message.channel.send("Bu komutu anlayamadım :(")

client.run('MTE1MzM3NjE1NTQ5MjE1OTQ4OA.G3g6BA.YjGymcoOfxio4Ywi9ruYT6tHpFS8Vr-PP5Fn-g')

#