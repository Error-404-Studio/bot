from discord import *
from discord.ext.commands import *
from requests import *

class Fun(Cog):
    def __init__(self, client):
        self.client = client
    @command()
    async def dog(self, ctx):
        await ctx.send(get("https://dog.ceo/api/breeds/image/random").json()["message"],view=ui.View(ui.Button(ButtonStyle.primary,custom_id="cat_next",label="NEXT")))
        
    @command()
    async def cat(self, ctx):
        await ctx.send(get("https://api.thecatapi.com/v1/images/search").json()["url"],view=ui.View(ui.Button(ButtonStyle.primary,custom_id="dog_next",label="NEXT")))
    @command()
    async def meme(self, ctx, *, subreddit: str = None):
        if subreddit:
            json = get(
                f"https://meme-api.herokuapp.com/gimme/{subreddit}"
            ).json()
        else:
            json = get(f"https://meme-api.herokuapp.com/gimme").json()

        try:
            if json["code"]:
                await ctx.send(
                    json["message"]
                )
                return
        except KeyError:
            if not json["nsfw"]:
                title = (
                    json["title"][:253]+"..."
                    if len(json["title"]) > 256
                    else json["title"]
                )
                meme_embed = Embed(
                    title=title,
                    description=f"r/{json['subreddit']}",
                    color=0x538AEE,
                    url=json["postLink"]
                )
                meme_embed.set_image(url=json["url"])
                await ctx.send(embed=meme_embed)

        if json["nsfw"]:
            await ctx.send(f"❗ Warning: NSFW post!\n\n<{json ['postLink']}>")

def setup(client):
    client.add_cog(Fun(client))
