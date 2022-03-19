import diskord
from diskord.ext import commands

class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = await self.client.fetch_channel(918167289721913419)
        role = member.guild.get_role(918430918144819210)

        embed = diskord.Embed(
            title="Welcome",
            description=f"Hello {member.mention}, welcome to **{member.guild}**! You'd better check the "
                        "<#918168914914070598> and have a good stay!",
            color=0x538AEE
        )
        embed.set_thumbnail(url=f"{member.avatar}")

        message = await channel.send(content=f"{member.mention}", embed=embed)
        await message.add_reaction("👋")

        await member.add_roles(role)

def setup(client):
    client.add_cog(Events(client))
