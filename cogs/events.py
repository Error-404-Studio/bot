from discord import *
from discord.ext.commands import *
from requests import *

class Events(Cog):
    def __init__(self, client):
        self.client = client

    @Cog.listener()
    async def on_member_join(self, member):
        channel = await self.client.fetch_channel(918167289721913419)
        role = member.guild.get_role(918430918144819210)

        embed = Embed(
            title="Welcome",
            description=f"Hello {member.mention}, welcome to **{member.guild}**! You'd better check the "
                        "<#918168914914070598> and have a good stay!",
            color=0x538AEE
        )
        embed.set_thumbnail(url=f"{member.avatar}")

        message = await channel.send(content=f"{member.mention}", embed=embed)
        await message.add_reaction("👋")

        await member.add_roles(role)

    @Cog.listener()
    async def on_interaction(self, interaction):
        if interaction.custom_id and interaction.message:
            if interaction.custom_id == 'cat_next':
                return await interaction.message.edit(content=get("https://api.thecatapi.com/v1/images/search").json()["url"])
            elif interaction.custom_id == 'dog_next':
                return await interaction.message.edit(content=get("https://dog.ceo/api/breeds/image/random").json()["message"])

def setup(client):
    client.add_cog(Events(client))
