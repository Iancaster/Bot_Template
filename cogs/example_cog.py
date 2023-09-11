import discord
from discord.ext import commands#, tasks
#from discord.commands import SlashCommandGroup
#from discord.utils import get_or_fetch, get

class ExampleCogName(commands.Cog): #When renaming, also rename in Setup below

    def __init__(self, bot: discord.Bot):
        self.bot = bot
        # self.example_task.start()

    # def cog_unload(self):
    #     self.example_task.cancel()
    #
    # @tasks.loop(seconds = 5.0)
    # async def example_task(self):
    #     return

    @commands.slash_command(
        name = 'hello',
        description = 'Say hi!')
    async def hello(
        self,
        ctx: discord.ApplicationContext):

        await ctx.respond('Hey!')
        return

    # group = SlashCommandGroup(
    #     name = 'prefix',
    #     description = "As an example of neatly organized commands.",
    #     guild_only = True) # You can set all the params of the group at once.
    #
    # group.command(
    #     name = 'example',
    #     description = 'The actual command to invoke here.')
    # async def example(
    #     self,
    #     ctx: discord.ApplicationContext):
    #
    #     await ctx.respond('This command was organized neatly.')
    #     return



def setup(bot):

    bot.add_cog(ExampleCogName(bot), override = True)

