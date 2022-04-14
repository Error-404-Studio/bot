from discord.ext.commands import *

fail = "<:fail:918581058029621260>"

class Errors(Cog):
    def __init__(self, client):
        self.client = client

    @Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, MissingAnyRole):
            await ctx.message.delete()
            await ctx.send(f"{fail} You don't have the required roles to execute this command.", delete_after=3)
        elif isinstance(error, MissingPermissions):
            await ctx.message.delete()
            await ctx.send(
                f"{fail} You need the {', '.join([err.lower().replace('_', ' ') for err in error.missing_permissions])}"
                " permission.", delete_after=4
            )
        elif isinstance(error, MissingRequiredArgument):
            await ctx.send(
                f"{fail} You haven't provided enough options.\n"
                + f"Missing option: `{error.param.name}`."
            )
        elif isinstance(error, TooManyArguments):
            await ctx.send(
                f"{fail} You've passed extra options to the command!\n"
                + "Check the help command to know what options to provide.",
            )
        elif isinstance(error, MemberNotFound):
            await ctx.send(f'{fail} I couldn\'t find the member "{error.argument}".', delete_after=4)
        elif isinstance(error, UserNotFound):
            await ctx.send(f'{fail} I couldn\'t find the user "{error.argument}".', delete_after=4)
        elif isinstance(error, BadArgument):
            await ctx.send(
                f"{fail} You haven't provided the correct types of options, please check the help command."
            )
        elif isinstance(error, NoPrivateMessage):
            await ctx.send(f"{fail} This command can't be used in DMs.")

def setup(client):
    client.add_cog(Errors(client))
