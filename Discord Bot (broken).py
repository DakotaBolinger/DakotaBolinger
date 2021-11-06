import discord
import requests
import json

client = discord.Client()

def get_quote():
  response = requests.get
  ("https://zenquotes.io/api/random")
  json_data= json.loads(response.text)
  quote = json_data [0] ['q'] + " _" +
  json_data [0] ['a']
  return(quote)



@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author==client.user:
      return
    
    if message.content.startswith('$inspire'):
      quote = get_quote()
      await message.channel.send(quote)

client.run('OTA2NDEyNzY0MTYyMDYwMjk4.YYYQqw.1amTMei4NimIKWf7ESWL6fAoLKo')