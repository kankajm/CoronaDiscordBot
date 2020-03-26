import discord
import api_func

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('!corona'):
            user = message.author
            data = api_func.api.overview_corona()
            await message.channel.send("{}, there's {} cases right now, {} deaths and {} people recovered from the COVID-19."
                                       .format(user, data[0], data[1], data[2]))

client = MyClient()
client.run('NjkyNTI1MDE1NjY4NjIxMzIx.XnvyPQ.HFPj6CgxTy26MDStmRaIyPzRPik')