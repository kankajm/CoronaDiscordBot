import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

client = MyClient()
client.run('NjkyNTI1MDE1NjY4NjIxMzIx.XnvyPQ.HFPj6CgxTy26MDStmRaIyPzRPik')