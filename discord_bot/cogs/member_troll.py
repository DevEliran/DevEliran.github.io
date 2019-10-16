import discord
import random
from discord.ext import commands

class member_troll(commands.Cog):

    def __init__(self,bot):
        self.bot=bot

    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'Pong! {round(self.bot.latency*1000)} ms')#Bot sends a message

    @commands.command(aliases=['ask1'])# all of the strings in this array can invoke the _8ball function
    async def ask(self,ctx,*,question):
        res=['combining the two. It’s really not as bad as it sounds.',
                'Friday; otherwise, he would have not passed the class.',
                'to spend two weeks there next year.',
                'movie alone.',
                'kite in the middle of the night and ended up sunburnt.',
                'Please wait outside of the house.',
                'Wednesday is hump day, but has anyone asked the camel if he’s happy about it?',
                'This is the last random sentence I will be writing and I am going to stop mid-sent',
                'Sixty-Four comes asking for bread.',
                'I checked to make sure that he was still alive.',
                'I love eating toasted cheese and tuna sandwiches.']
        await ctx.send(random.choice(res))

def setup(bot):
    bot.add_cog(member_troll(bot))
