import diskord
from diskord.ext import commands
import datetime

success = "<:success:918581057798955080>"
fail = "<:fail:918581058029621260>"

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_any_role("Helper", "Moderator")
    async def lock(self, ctx, channel: diskord.TextChannel = None):
        channel = ctx.channel or channel

        channels_ids = [918168012731850782, 918168042121338881, 918168914914070598, 918168946430070814, 918168981024673873, 918169023676547073, 918413264390606849, 918413300419686400, 918428080727527444, 918413356673679380, 918449539403382864]

        if channel.id in channels_ids:
            await ctx.message.delete()
            await ctx.send(f"{fail} You can't lock that channel!", delete_after=3)
        else:
            await channel.set_permissions(ctx.guild.default_role, send_messages=False, add_reactions=False)
            await ctx.send(f"{success} Successfully locked {channel.mention}", delete_after=2)

            embed = diskord.Embed(
                title="Channel locked",
                description=f"This channel was locked by {ctx.author.mention} 🔒",
                color=0x538AEE
            )
            embed.timestamp = datetime.datetime.utcnow()

            await channel.send(embed=embed)

    @commands.command()
    @commands.has_any_role("Helper", "Moderator", "Owner")
    async def unlock(self, ctx, channel: diskord.TextChannel = None):
        channel = ctx.channel or channel

        channels_ids = [918168012731850782, 918168042121338881, 918168914914070598, 918168946430070814, 918168981024673873, 918169023676547073, 918413264390606849, 918413300419686400, 918428080727527444, 918413356673679380, 918449539403382864]

        if channel.id in channels_ids:
            await ctx.message.delete()
            await ctx.send(f"{fail} You can't unlock that channel!", delete_after=3)
        else:
            await channel.set_permissions(ctx.guild.default_role, send_messages=False, add_reactions=False)
            await ctx.send(f"{success} Successfully unlocked {channel.mention}", delete_after=2)

            embed = diskord.Embed(
                title="Channel unlocked",
                description=f"This channel was unlocked by {ctx.author.mention} 🔓",
                color=0x538AEE
            )
            embed.timestamp = datetime.datetime.utcnow()

            await channel.send(embed=embed)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: commands.MemberConverter, *, reason: str = None):
        if member == ctx.author:
            await ctx.message.delete()
            await ctx.send(f"{fail} You can't kick yourself!", delete_after=3)
            return
        elif member.top_role >= ctx.author.top_role or member == ctx.guild.owner:
            await ctx.message.delete()
            await ctx.send(f"{fail} That user is above you or he/she is the owner of {ctx.guild}, so you can't kick "
                           f"him/her.",
                           delete_after=4.5)
            return
        elif member.id == self.client.user.id:
            await ctx.message.delete()
            await ctx.send(f"{fail} I can't kick myself!", delete_after=3)
            return
        elif ctx.guild.me.top_role <= member.top_role:
            await ctx.message.delete()
            await ctx.send(
                f"{fail} The user has a higher role or the same top role as mine.\n"
                + "Please move my role higher!", delete_after=3
            )
            return

        try:
            await member.send(f"You were kicked from {ctx.guild}! Reason: {reason}.")
        except:
            pass

        await ctx.guild.kick(member, reason=f"Kicked by {ctx.author}. Reason: {reason}")

        embed = diskord.Embed(
            title="User kicked",
            description=f"{member.mention} was kicked by {ctx.author.mention}.",
            color=0x538AEE
        )
        embed.add_field(name="Reason", value=str(reason.capitalize()))
        embed.timestamp = datetime.datetime.utcnow()

        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: commands.MemberConverter, *, reason: str = None):
        if member == ctx.author:
            await ctx.message.delete()
            await ctx.send(f"{fail} You can't ban yourself!", delete_after=3)
            return
        elif member.top_role >= ctx.author.top_role or member == ctx.guild.owner:
            await ctx.message.delete()
            await ctx.send(
                f"{fail} That user is above you or he/she is the owner of {ctx.guild}, so you can't ban him/her.",
                delete_after=4.5)
            return
        elif member.id == self.client.user.id:
            await ctx.message.delete()
            await ctx.send(f"{fail} I can't ban myself!", delete_after=3)
            return
        elif ctx.guild.me.top_role <= member.top_role:
            await ctx.message.delete()
            await ctx.send(
                f"{fail} The user has a higher role or the same top role as mine.\n"
                + "Please move my role higher!", delete_after=3
            )
            return

        try:
            await member.send(f"You were banned from {ctx.guild}! Reason: {reason}.")
        except:
            pass

        await ctx.guild.ban(member, reason=f"Banned by {ctx.author}. Reason: {reason}")

        embed = diskord.Embed(
            title="User banned",
            description=f"{member.mention} was banned by {ctx.author.mention}.",
            color=0x538AEE
        )
        embed.add_field(name="Reason", value=str(reason.capitalize()))
        embed.timestamp = datetime.datetime.utcnow()

        await ctx.send(embed=embed)

    async def mute_checker(self, ctx, bot_role, member, muted_role):
        bot_role = ctx.guild.me.top_role

        if member == ctx.author:
            await ctx.message.delete()
            await ctx.send(f"{fail} You can't mute yourself!", delete_after=3)
            return False
        elif member == self.client.user:
            await ctx.message.delete()
            await ctx.send(f"{fail} I can't mute myself!", delete_after=3)
            return False
        elif bot_role <= member.top_role:
            await ctx.message.delete()
            await ctx.send(
                f"{fail} The user has a higher role or the same top role as mine.\n"
                + "Please move my role higher!", delete_after=3
            )
            return False
        elif member.guild_permissions.administrator:
            await ctx.message.delete()
            await ctx.send(f"{fail} This user has `Adminstrator` perms in this server, so you can't mute him/her.",
                           delete_after=3)
            return False
        elif member.top_role > ctx.author.top_role or member.top_role == ctx.author.top_role or member == ctx.guild.owner:
            await ctx.message.delete()
            await ctx.send(f"{fail} That user is above you or he/she is the wwner of {ctx.guild}, "
                           "so you can't mute him/her.", delete_after=3)
            return False
        elif bot_role <= muted_role:
            await ctx.message.delete()
            await ctx.send(
                f"{fail} My role is too low. I can only mute users if my role is higher than "
                "the Muted role!", delete_after=3
            )
            return False
        elif muted_role in member.roles:
            await ctx.message.delete()
            await ctx.send(f"{fail} This user is muted yet!", delete_after=3)
            return False

    @commands.command()
    @commands.has_any_role("Helper", "Moderator", "Owner")
    async def mute(self, ctx, member: commands.MemberConverter, *, reason: str = None):
        muted_role = diskord.utils.get(ctx.guild.roles[::-1], name="Muted")

        if (
                await self.mute_checker(ctx, ctx.guild.me.top_role, member, muted_role)
                == False
        ):
            return
        else:
            await member.add_roles(muted_role, reason=f"Muted by {ctx.author}. Reason: {str(reason.capitalize())}")

            embed = diskord.Embed(
                title="User muted",
                description=f"{member.mention} was muted by {ctx.author.mention}.",
                color=0x538AEE
            )
            embed.add_field(name="Reason", value=str(reason.capitalize()))

            await ctx.send(embed=embed)

            embeddm = diskord.Embed(
                title="You were muted",
                description=f"You were muted in **{ctx.guild}** by **{ctx.author}**.",
                color=0x538AEE
            )
            embeddm.add_field(name="Reason", value=str(reason.capitalize()))

            await member.send(embed=embeddm)

    @commands.command()
    async def unmute(self, ctx, member: commands.MemberConverter):
        muted_role = diskord.utils.get(ctx.guild.roles[::-1], name="Muted")

        if not muted_role in member.roles:
            await ctx.message.delete()
            await ctx.send(f"{fail} This user isn't muted!")
            return

        elif ctx.guild.me.top_role <= muted_role:
            await ctx.message.delete()
            await ctx.send(
                f"{fail} My role is too low. I can only unmute users if my role is higher than "
                "the Muted role!", delete_after=3
            )
            return

        elif ctx.guild.me.top_role <= member.top_role:
            await ctx.message.delete()
            await ctx.send(
                f"{fail} The user has a higher role or the same top role as mine.\n"
                + "Please move my role higher!", delete_after=3
            )
            return

        await member.remove_roles(muted_role)

        embed = diskord.Embed(
            title="User unmuted",
            description=f"{member.mention} was unmuted by {ctx.author.mention}.",
            color=0x538AEE
        )

        await ctx.send(embed=embed)

        embeddm = diskord.Embed(
            title="You were unmuted",
            description=f"You were unmuted in **{ctx.guild.name}** by **{ctx.author}**.",
            color=0x538AEE
        )
        await member.send(embed=embeddm)

    @commands.command()
    @commands.has_any_role("Helper", "Moderator", "Owner")
    async def clear(self, ctx, amount: int):
        if amount > 100:
            await ctx.message.delete()
            await ctx.send(f"{fail} You can delete up to 100 messages!", delete_after=3)
        else:
            try:
                await ctx.channel.purge(limit=amount)
                await ctx.send(f"{success} {amount} messages have been deleted by {ctx.author}.", delete_after=3)
            except diskord.Forbidden:
                pass
                await ctx.send(f"{fail} Due to Discord's ToS, you can't delete messages that are more than 14 days old.")

    @commands.command()
    @commands.has_any_role("Helper", "Moderator", "Owner")
    async def slowmode(self, ctx, seconds: int):
        if seconds > 21600:
            await ctx.message.delete()
            await ctx.send(f"{fail} Can't set the slowmode to {seconds} seconds because the "
                           "maximum delay is 6 hours (21600 seconds).", delete_after=3)
        elif seconds < 0:
            await ctx.message.delete()
            await ctx.send(f"{fail} Can't set the slowmode to {seconds} seconds because "
                           "seconds must be greater than or equal to 0 (if you put 0, the slowmode will be off).",
                           delete_after=3)
        elif seconds == 1:
            await ctx.channel.edit(slowmode_delay=seconds)
            await ctx.send(f"{success} Set the slowmode in this channel to `1` second.")
        elif seconds == 0:
            await ctx.channel.edit(slowmode_delay=seconds)
            await ctx.send(f"{success} Disabled the slowmode in this channel.")
        else:
            await ctx.channel.edit(slowmode_delay=seconds)
            await ctx.send(f"{success} Set the slowmode delay in this channel to `{seconds}` seconds.")

def setup(client):
    client.add_cog(Moderation(client))
