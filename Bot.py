Import discord
Import asyncio


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
  
  @client.even
  arguments = ' '.join(message.content.strip().split(' ')[1:])
async def on_message(message):
	prefix = '-'
	cmd_string_bool = message.content.startswith(prefix)
	cmd_string = message.content
	if cmd_string_bool:
		print('Command: {0} with arguments: {1}'.format(cmd_string, arguments))
	command = message.content
	if command.startswith(prefix + "shutdown"):
		await reply(channel, 'turning off...')
		await client.logout()
	elif command.startswith(prefix + 'ping'):
		ts = message.timestamp
		new_msg = await client.send_message(channel, 'PONG!')
		latency = new_msg.edited_timestamp - ts
		if latency.microseconds >= 1000000:
			await client.edit_message(message, 'PONG! It took {} miliseconds, or {} seconds to respond!'.format(latency.microseconds // 1000, latency.microseconds / 1000000))
		else:
      await client.edit_message(message, 'PONG! It took {} miliseconds to respond!'.format(latency.microseconds // 1000))
