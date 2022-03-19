import diskord
from diskord.ext import commands

class HelpButtons(diskord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @diskord.ui.button(label="Home", emoji="<:home_button:918467896592719902>", style=diskord.ButtonStyle.red)
    async def home(self, button: diskord.ui.Button, interaction: diskord.Interaction):
        embed = diskord.Embed(
            title="Home",
            description="""  
            Press the <:utilities_button:918468783000150016> button to view the utilities commands.
            
            Press the <:mod_button:918474582271356928> button to view the moderation commands.
            
            Press the <:fun_button:918478578054725632> button to view the fun commands.
            """,
            color=0x538AEE
        )

        await interaction.message.edit(content=None, embed=embed)

    @diskord.ui.button(label="Utilities", emoji="<:utilities_button:918468783000150016>", style=diskord.ButtonStyle.green)
    async def utilities(self, button: diskord.ui.Button, interaction: diskord.Interaction):
        embed = diskord.Embed(
            title="Utilities",
            description="""
            `!github`: Check our organization on GitHub.
            
            `![developers|devs]`: Check the list our developers.
            
            `!codehelp`: Check how to ask for help.
            
            `!report`: Report a member to the staff.

            Press the <:home_button:918467896592719902> button to return to the home.
            Press the <:mod_button:918474582271356928> button to view the moderation commmands.
            Press the <:fun_button:918478578054725632> button to view the fun commands.
            """,
            color=0x538AEE
        )

        await interaction.message.edit(content=None, embed=embed)

    @diskord.ui.button(label="Moderation", emoji="<:mod_button:918474582271356928>", style=diskord.ButtonStyle.green)
    async def moderation(self, button: diskord.ui.Button, interaction: diskord.Interaction):
        embed = diskord.Embed(
            title="Moderation",
            description="""
            `!lock [#channel] [reason]`: Lock a channel.
            
            `!unlock [#channel] [reason]`: Unlock a channel.
            
            `!kick <@user> [reason]`: Kick a user.
            
            `!ban <@user> [reason]`: Ban a user.
            
            `!mute <@user> [reason]`: Mute a user.
            
            `!unmute <@user>`: Unmute a user.
            
            `!slowmode <seconds>`: Set the slowmode.
            
            `!clear <messages>`: Clear an amount of messages.
            
            Press the <:home_button:918467896592719902> button to return to the home.
            Press the <:utilities_button:918468783000150016> button to view the utilities commands.
            Press the <:fun_button:918478578054725632> button to view the fun commands.
            """,
            color=0x538AEE
        )

        await interaction.message.edit(content=None, embed=embed)

    @diskord.ui.button(label="Fun", emoji="<:fun_button:918478578054725632>", style=diskord.ButtonStyle.green)
    async def fun(self, button: diskord.ui.Button, interaction: diskord.Interaction):
        embed = diskord.Embed(
            title="Fun",
            description="""
            `!meme [subreddit]`: Get a meme from Reddit (add a subreddit name if you want the meme from that subreddit).

            Press the <:home_button:918467896592719902> button to return to the home.
            Press the <:utilities_button:918468783000150016> button to view the utilities commands.
            Press the <:mod_button:918474582271356928> button to view the moderation commmands.                
            """,
            color=0x538AEE
        )

        await interaction.message.edit(content=None, embed=embed)

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["h"])
    async def help(self, ctx):
        embed = diskord.Embed(
            title="Home",
            description="""
            Press the <:utilities_button:918468783000150016> button to view the utilities commands.

            Press the <:mod_button:918474582271356928> button to view the moderation commands.
            
            Press the <:fun_button:918478578054725632> button to view the fun commands.
            """,
            color=0x538AEE
        )

        await ctx.send(embed=embed, view=HelpButtons())

def setup(client):
    client.add_cog(Help(client))
