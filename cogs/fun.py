import diskord
from diskord.ext import commands
import requests

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def meme(self, ctx, *, subreddit = None):
        if subreddit:
            json=requests.get(
                f"https://meme-api.herokuapp.com/gimme/{subreddit}"
            ).json()
        else:
            json=requests.get(f"https://meme-api.herokuapp.com/gimme").json()

        try:
            if json["code"]:
                await ctx.send(
                    json["message"]
                )
                return
        except KeyError:
            if not json["nsfw"]:
                title=(
                    json["title"][:253]+"..."
                    if len(json["title"])>256
                    else json["title"]
                )
                meme_embed = diskord.Embed(
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
