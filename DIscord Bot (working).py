import discord


client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author==client.user:
      return
    
    if message.content.startswith('$hello'):
      await message.channel.send('Hello Fellow King')
    if message.content.startswith('$I am feeling down'):
      await message.channel.send('Dont feel down papa poob loves ya')
  
client.run('OTA2NDEyNzY0MTYyMDYwMjk4.YYYQqw.1amTMei4NimIKWf7ESWL6fAoLKo')