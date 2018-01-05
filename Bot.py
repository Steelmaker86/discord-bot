import discord
import asyncio
import time
import config
client = discord.Client()

def reply(x):
  client.send_message(x)

@client.event
async def on_ready():
	startup = time.ctime()
	print('Signed in as:')
	print(client.user.name)
	print(client.user.id)
	print('~~~~~~~~~~~')
	print(client)
	print('Startup at: ' + startup)
	embed.clear_fields()
  
  @client.event
  arguments = ' '.join(message.content.strip().split(' ')[1:])
async def on_message(message):
	prefix = config.prefix
	cmd_string_bool = message.content.startswith(prefix)
	cmd_string = message.content
	if cmd_string_bool:
		print('Command: {0} with arguments: {1}'.format(cmd_string, arguments))
	command = message.content
	if command.startswith(prefix + "shutdown"):
    if message.author != config.creator:
      return
    else:
        await reply(channel, 'turning off...')
		await client.logout()


client.run(TOKEN)
