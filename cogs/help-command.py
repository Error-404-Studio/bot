from discord import *
from discord.ext.commands import *

class HelpButtons(ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @ui.button(label="Home", emoji="<:home_button:918467896592719902>", style=ButtonStyle.red)
    async def home(self, button: ui.Button, interaction: Interaction):
        embed = Embed(
            title="Home",
            description="""  
Press the <:utilities_button:918468783000150016> button to view the utilities commands.

Press the <:mod_button:918474582271356928> button to view the moderation commands.

Press the <:fun_button:918478578054725632> button to view the fun commands.
            """,
            color=0x538AEE
        )

        await interaction.message.edit(content=None, embed=embed)

    @ui.button(label="Utilities", emoji="<:utilities_button:918468783000150016>", style=ButtonStyle.green)
    async def utilities(self, button: ui.Button, interaction: Interaction):
        embed = Embed(
            title="Utilities",
            description="""
`!github`: Check our organization on GitHub.

`![developers|devs]`: Check the list our developers.

`!codehelp`: Check how to ask for help.

`!report`: Report a member to the staff.

Press the <:home_button:918467896592719902> button to return to the home.
Press the <:mod_button:918474582271356928> button to view the moderation commands.
Press the <:fun_button:918478578054725632> button to view the fun commands.
            """,
            color=0x538AEE
        )

        await interaction.message.edit(content=None, embed=embed)

    @ui.button(label="Moderation", emoji="<:mod_button:918474582271356928>", style=ButtonStyle.green)
    async def moderation(self, button: ui.Button, interaction: Interaction):
        embed = Embed(
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

    @ui.button(label="Fun", emoji="<:fun_button:918478578054725632>", style=ButtonStyle.green)
    async def fun(self, button: ui.Button, interaction: Interaction):
        embed = Embed(
            title="Fun",
            description="""
`!meme [subreddit]`: Get a meme from Reddit (add a subreddit name if you want the meme from that subreddit).

Press the <:home_button:918467896592719902> button to return to the home.
Press the <:utilities_button:918468783000150016> button to view the utilities commands.
Press the <:mod_button:918474582271356928> button to view the moderation commands.                
            """,
            color=0x538AEE
        )

        await interaction.message.edit(content=None, embed=embed)

class Help(Cog):
    def __init__(self, client):
        self.client = client

    @command(aliases=["h"])
    async def help(self, ctx):
        embed = Embed(
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
