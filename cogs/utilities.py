import diskord
from diskord.ext import commands
import asyncio

class Utilities(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def github(self, ctx):
        embed = diskord.Embed(
            title="GitHub",
            description="You can check our organization on GitHub clicking [here](https://github.com/Error-404-Studio).",
            color=0x538AEE
        )

        await ctx.send(embed=embed)

    @commands.command(aliases=["devs"])
    async def developers(self, ctx):
        embed = diskord.Embed(
            title="Our developers",
            description="""
            - <@825292137338765333> (AKA the founder of **Error 404 Studio**)
            """,
            color=0x538AEE
        )

        await ctx.send(embed=embed)

    @commands.command()
    async def codehelp(self, ctx):
        embed = diskord.Embed(
            title="How to ask for help",
            description="If you need help with your code, please check the guidelines at <#918170064560209940>. Also "
                        "remember to ask in the correct channel (if your programming language is not in the list, "
                        "ask in <#918171141384863794>).",
            color=0x538AEE
        )

        await ctx.send(embed=embed)

    @commands.command()
    async def report(self, ctx):
        questions = [
            "Which user would you like to report? (Enter his/her ID or his/her username, don't mention him/her)",
            "Why are you reporting him/her? (If you have proofs like images, upload them to https://imgur.com)",
        ]
        answers = []

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        for question in questions:
            await ctx.send(question)
            try:
                message = await self.client.wait_for("message", timeout=90.0, check=check)
            except asyncio.TimeoutError:
                await ctx.send(
                    "You didn't answer in time. Please try again and be sure to send your answer within 60 seconds of "
                    "the question.")
                return
            else:
                answers.append(message.content)

        channel = await self.client.fetch_channel(918449539403382864)

        embed = diskord.Embed(
            title=f"New user reported",
            description=f"""
            **Reporter:** {ctx.author.mention} (`{ctx.author}` | `{ctx.author.id}`)
            
            **Reported user (ID or username):** `{answers[0]}`
            
            **Reason:** {answers[1]}
            """,
            color=0x538AEE
        )

        await channel.send(embed=embed)
        await ctx.send("The report was sent successfully!")

def setup(client):
    client.add_cog(Utilities(client))
