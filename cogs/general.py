import nextcord
from nextcord.ext.commands.core import command
from utils.languageembed import languageEmbed
import settings
import asyncio
from bs4 import BeautifulSoup
import aiohttp
from urllib.parse import urlencode

from nextcord.ext import commands

class General(commands.Cog): 
    def __init__(self, bot: commands.AutoShardedBot):
        self.bot = bot

    @commands.command()
    async def lmgtfy(self, ctx, *, message):
        languageserver = await settings.collectionlanguage.find_one({"guild_id":ctx.guild.id})
        if languageserver is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self,ctx))
            await message.add_reaction('đ')
        
        else:
            server_language = languageserver["Language"]
            
            r = urlencode({"q": message})
            url = (f'<https://lmgtfy.com/?{r}>')

            if server_language == "Thai": 
                embed= nextcord.Embed(
                    colour =0x00FFFF,
                    title= f"ā¸Ĩā¸´ā¸ā¸āš lmgtfy ā¸ā¸­ā¸ā¸ā¸¸ā¸ {ctx.author}",
                    description = f"{url}"
                )

                message = await ctx.send(embed=embed)
                await message.add_reaction('đ')
            
            if server_language == "English": 
                embed= nextcord.Embed(
                    colour =0x00FFFF,
                    title= f"lmgtfy link for {ctx.author}",
                    description = f"{url}"
                )

                message = await ctx.send(embed=embed)
                await message.add_reaction('đ')
        
    @lmgtfy.error
    async def lmgtfy_error(self, ctx, error):
        languageserver = await settings.collectionlanguage.find_one({"guild_id":ctx.guild.id})
        if languageserver is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self,ctx))
            await message.add_reaction('đ')
        
        else:
            server_language = languageserver["Language"]
            
            if server_language == "Thai":
                if isinstance(error, commands.MissingRequiredArgument):
                    embed = nextcord.Embed(
                            colour = 0x983925,
                            description = f" â ī¸``{ctx.author}`` ā¸ā¸°ā¸āšā¸­ā¸ā¸ā¸´ā¸Ąā¸Ēā¸´āšā¸ā¸ā¸ĩāšā¸ā¸°ā¸āšā¸ā¸Ģā¸˛āšā¸ lmgtfy ``{settings.COMMAND_PREFIX}lmgtfy [message]``"
                        )
                    embed.set_footer(text=f"âRequested by {ctx.author}")

                    message = await ctx.send(embed=embed ) 
                    await message.add_reaction('â ī¸')
            
            if server_language == "English":
                if isinstance(error, commands.MissingRequiredArgument):
                    embed = nextcord.Embed(
                            colour = 0x983925,
                            description = f" â ī¸``{ctx.author}`` need to specify what to search on lmgtfy ``{settings.COMMAND_PREFIX}lmgtfy [message]``"
                        )
                    embed.set_footer(text=f"âRequested by {ctx.author}")

                    message = await ctx.send(embed=embed ) 
                    await message.add_reaction('â ī¸')

    @commands.command()
    async def timer(self,ctx, second : int):
        languageserver = await settings.collectionlanguage.find_one({"guild_id":ctx.guild.id})
        if languageserver is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self,ctx))
            await message.add_reaction('đ')
        
        else:
            server_language = languageserver["Language"]
            
            if server_language == "Thai":

                number = second
                embed = nextcord.Embed(
                        colour = 0x00FFFF,
                        title = f"âąī¸ ā¸ā¸ąā¸ā¸ā¸­ā¸ĸā¸Ģā¸Ĩā¸ąā¸ {second} ā¸§ā¸´ā¸ā¸˛ā¸ā¸ĩ",
                        description = f"{number}"
                    )
                embed.set_footer(text=f"âRequested by {ctx.author}")
                message = await ctx.send(embed=embed)

                while number >= 0:
                    embed = nextcord.Embed(
                        colour = 0x00FFFF,
                        title = f"âąī¸ ā¸ā¸ąā¸ā¸ā¸­ā¸ĸā¸Ģā¸Ĩā¸ąā¸ {second} ā¸§ā¸´ā¸ā¸˛ā¸ā¸ĩ",
                        description = f"```{number}```"
                    )
                    embed.set_footer(text=f"âRequested by {ctx.author}")
                    number = number - 1 
                    await asyncio.sleep(1)
                    await message.edit(embed=embed)

                embed = nextcord.Embed(
                    colour = 0x00FFFF,
                    title = f"âąī¸ ā¸ā¸ąā¸ā¸ā¸­ā¸ĸā¸Ģā¸Ĩā¸ąā¸ {second} ā¸§ā¸´ā¸ā¸˛ā¸ā¸ĩ",
                    description = "āšā¸Ēā¸Ŗāšā¸"
                )
                embed.set_footer(text=f"âRequested by {ctx.author}")

                await message.edit(embed=embed)
            
            if server_language == "Thai":

                number = second
                embed = nextcord.Embed(
                        colour = 0x00FFFF,
                        title = f"âąī¸ countdown for {second} second",
                        description = f"{number}"
                    )
                embed.set_footer(text=f"âRequested by {ctx.author}")
                message = await ctx.send(embed=embed)

                while number >= 0:
                    embed = nextcord.Embed(
                        colour = 0x00FFFF,
                        title = f"âąī¸ countdown for {second} second",
                        description = f"```{number}```"
                    )
                    embed.set_footer(text=f"âRequested by {ctx.author}")
                    number = number - 1 
                    await asyncio.sleep(1)
                    await message.edit(embed=embed)

                embed = nextcord.Embed(
                    colour = 0x00FFFF,
                    title = f"âąī¸ countdown for {second} second",
                    description = "Finished"
                )
                embed.set_footer(text=f"âRequested by {ctx.author}")

                await message.edit(embed=embed)

    @timer.error
    async def timer_error(self,ctx, error):
        languageserver = await settings.collectionlanguage.find_one({"guild_id":ctx.guild.id})
        if languageserver is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self,ctx))
            await message.add_reaction('đ')
        
        else:
            server_language = languageserver["Language"]
            
            if server_language == "Thai":
                if isinstance(error, commands.MissingRequiredArgument):
                    embed = nextcord.Embed(
                        colour = 0x983925,
                        description = f" â ī¸``{ctx.author}`` ā¸ā¸°ā¸āšā¸­ā¸ā¸ā¸´ā¸Ąā¸§ā¸´ā¸ā¸˛ā¸ā¸ĩā¸ā¸ĩāšā¸āšā¸­ā¸ā¸ā¸˛ā¸Ŗā¸ā¸°ā¸ā¸ąā¸ā¸ā¸­ā¸ĸā¸Ģā¸Ĩā¸ąā¸ ``{settings.COMMAND_PREFIX}timer (second)``"
                    )
                    embed.set_footer(text=f"âRequested by {ctx.author}")

                    message = await ctx.send(embed=embed ) 
                    await message.add_reaction('â ī¸')
            
            if server_language == "English":
                if isinstance(error, commands.MissingRequiredArgument):
                    embed = nextcord.Embed(
                        colour = 0x983925,
                        description = f" â ī¸``{ctx.author}`` need to specify how long to countdown ``{settings.COMMAND_PREFIX}timer (second)``"
                    )
                    embed.set_footer(text=f"âRequested by {ctx.author}")

                    message = await ctx.send(embed=embed ) 
                    await message.add_reaction('â ī¸')

    @commands.command()
    async def count(self,ctx, second : int):
        languageserver = await settings.collectionlanguage.find_one({"guild_id":ctx.guild.id})
        if languageserver is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self,ctx))
            await message.add_reaction('đ')
        
        else:
            server_language = languageserver["Language"]
            
            if server_language == "Thai":
                number = 0
                embed = nextcord.Embed(
                        colour = 0x00FFFF,
                        title = f"âąī¸ ā¸ā¸ąā¸āšā¸Ĩā¸ā¸ā¸ļā¸ {second} ā¸§ā¸´ā¸ā¸˛ā¸ā¸ĩ",
                        description = f"{number}"
                    )

                embed.set_footer(text=f"âRequested by {ctx.author}")
                message = await ctx.send(embed=embed)

                while number <= second:
                    embed = nextcord.Embed(
                        colour = 0x00FFFF,
                        title = f"âąī¸ ā¸ā¸ąā¸āšā¸Ĩā¸ā¸ā¸ļā¸ {second} ā¸§ā¸´ā¸ā¸˛ā¸ā¸ĩ",
                        description = f"```{number}```"
                    )
                    embed.set_footer(text=f"âRequested by {ctx.author}")
                    number = number + 1 
                    await asyncio.sleep(1)
                    await message.edit(embed=embed)

                embed = nextcord.Embed(
                    colour = 0x00FFFF,
                    title = f"âąī¸ ā¸ā¸ąā¸āšā¸Ĩā¸ā¸ā¸ļā¸ {second} ā¸§ā¸´ā¸ā¸˛ā¸ā¸ĩ",
                    description = "āšā¸Ēā¸Ŗāšā¸"
                )
                embed.set_footer(text=f"âRequested by {ctx.author}")

                await message.edit(embed=embed)
            
            if server_language == "English":
                number = 0
                embed = nextcord.Embed(
                        colour = 0x00FFFF,
                        title = f"âąī¸ ā¸ā¸ąā¸āšā¸Ĩā¸ā¸ā¸ļā¸ {second} ā¸§ā¸´ā¸ā¸˛ā¸ā¸ĩ",
                        description = f"{number}"
                    )

                embed.set_footer(text=f"âRequested by {ctx.author}")
                message = await ctx.send(embed=embed)

                while number <= second:
                    embed = nextcord.Embed(
                        colour = 0x00FFFF,
                        title = f"âąī¸ ā¸ā¸ąā¸āšā¸Ĩā¸ā¸ā¸ļā¸ {second} ā¸§ā¸´ā¸ā¸˛ā¸ā¸ĩ",
                        description = f"```{number}```"
                    )
                    embed.set_footer(text=f"âRequested by {ctx.author}")
                    number = number + 1 
                    await asyncio.sleep(1)
                    await message.edit(embed=embed)

                embed = nextcord.Embed(
                    colour = 0x00FFFF,
                    title = f"âąī¸ ā¸ā¸ąā¸āšā¸Ĩā¸ā¸ā¸ļā¸ {second} ā¸§ā¸´ā¸ā¸˛ā¸ā¸ĩ",
                    description = "āšā¸Ēā¸Ŗāšā¸"
                )
                embed.set_footer(text=f"âRequested by {ctx.author}")

                await message.edit(embed=embed)

    @count.error
    async def count_error(self,ctx, error):
        languageserver = await settings.collectionlanguage.find_one({"guild_id":ctx.guild.id})
        if languageserver is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self,ctx))
            await message.add_reaction('đ')
        
        else:
            server_language = languageserver["Language"]
            
            if server_language == "Thai":
                if isinstance(error, commands.MissingRequiredArgument):
                    embed = nextcord.Embed(
                        colour = 0x983925,
                        description = f" â ī¸``{ctx.author}`` ā¸ā¸°ā¸āšā¸­ā¸ā¸ā¸´ā¸Ąā¸§ā¸´ā¸ā¸˛ā¸ā¸ĩā¸ā¸ĩāšā¸āšā¸­ā¸ā¸ā¸˛ā¸Ŗā¸ā¸°ā¸ā¸ąā¸ ``{settings.COMMAND_PREFIX}count (second)``"
                    )
                    embed.set_footer(text=f"âRequested by {ctx.author}")

                    message = await ctx.send(embed=embed ) 
                    await message.add_reaction('â ī¸')
            
            if server_language == "English":
                if isinstance(error, commands.MissingRequiredArgument):
                    embed = nextcord.Embed(
                        colour = 0x983925,
                        description = f" â ī¸``{ctx.author}`` need to specify how long to coun ``{settings.COMMAND_PREFIX}count (second)``"
                    )
                    embed.set_footer(text=f"âRequested by {ctx.author}")

                    message = await ctx.send(embed=embed ) 
                    await message.add_reaction('â ī¸')

    @commands.command()
    async def upper(self,ctx, *, message):
        languageserver = await settings.collectionlanguage.find_one({"guild_id":ctx.guild.id})
        if languageserver is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self,ctx))
            await message.add_reaction('đ')
        
        else:
            server_language = languageserver["Language"]
            
            if server_language == "Thai":
                big = message.upper()
                embed = nextcord.Embed(
                    colour = 0x00FFFF,
                    title = "UPPERCASE GENERATOR",
                    description = f"""```
ā¸āšā¸­ā¸ā¸§ā¸˛ā¸Ąā¸ā¸ā¸ā¸´ : {message}
ā¸āšā¸­ā¸ā¸§ā¸˛ā¸Ąā¸ā¸ąā¸§ā¸ā¸´ā¸Ąā¸āšāšā¸Ģā¸āš : {big}```"""

                )

                embed.set_footer(text=f"âRequested by {ctx.author}")
                await ctx.send(embed=embed)
            
            if server_language == "English":
                big = message.upper()
                embed = nextcord.Embed(
                    colour = 0x00FFFF,
                    title = "UPPERCASE GENERATOR",
                    description = f"""```
Normal text : {message}
Uppercase text : {big}```"""

                )

                embed.set_footer(text=f"âRequested by {ctx.author}")
                await ctx.send(embed=embed)

    @upper.error
    async def upper_error(self,ctx, error):
        languageserver = await settings.collectionlanguage.find_one({"guild_id":ctx.guild.id})
        if languageserver is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self,ctx))
            await message.add_reaction('đ')
        
        else:
            server_language = languageserver["Language"]
            
            if server_language == "Thai":
                if isinstance(error, commands.MissingRequiredArgument):
                    embed = nextcord.Embed(
                        colour = 0x983925,
                        description = f" â ī¸``{ctx.author}`` ā¸ā¸°ā¸āšā¸­ā¸āšā¸Ēāšā¸ā¸Ŗā¸°āšā¸ĸā¸ā¸Ģā¸Ŗā¸ˇā¸­ā¸āšā¸˛ā¸ā¸ĩāšā¸āšā¸­ā¸ā¸ā¸˛ā¸Ŗā¸ā¸ĩāšā¸ā¸°ā¸āšā¸˛āšā¸āšā¸ā¸ā¸´ā¸Ąāšā¸Ģā¸āš ``{settings.COMMAND_PREFIX}upper (message)``"
                    )
                    embed.set_footer(text=f"âRequested by {ctx.author}")

                    message = await ctx.send(embed=embed ) 
                    await message.add_reaction('â ī¸')
            
            if server_language == "English":
                if isinstance(error, commands.MissingRequiredArgument):
                    embed = nextcord.Embed(
                        colour = 0x983925,
                        description = f" â ī¸``{ctx.author}`` need to specify what to make into uppercase ``{settings.COMMAND_PREFIX}upper (message)``"
                    )
                    embed.set_footer(text=f"âRequested by {ctx.author}")

                    message = await ctx.send(embed=embed ) 
                    await message.add_reaction('â ī¸')

    @commands.command()
    async def lower(self,ctx, *, message):
        languageserver = await settings.collectionlanguage.find_one({"guild_id":ctx.guild.id})
        if languageserver is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self,ctx))
            await message.add_reaction('đ')
        
        else:
            server_language = languageserver["Language"]
            
            if server_language == "Thai":
                lower = message.lower()
                embed = nextcord.Embed(
                    colour = 0x00FFFF,
                    title = "LOWERCASE GENERATOR",
                    description = f"""```
ā¸āšā¸­ā¸ā¸§ā¸˛ā¸Ąā¸ā¸ā¸ā¸´ : {message}
ā¸āšā¸­ā¸ā¸§ā¸˛ā¸Ąā¸ā¸ąā¸§ā¸ā¸´ā¸Ąā¸āšāšā¸Ģā¸āš : {lower}```"""

            )

                embed.set_footer(text=f"âRequested by {ctx.author}")
                await ctx.send(embed=embed)
            
            if server_language == "English":
                lower = message.lower()
                embed = nextcord.Embed(
                    colour = 0x00FFFF,
                    title = "LOWERCASE GENERATOR",
                    description = f"""```
Normal text : {message}
Lowercase text : {lower}```"""

            )

                embed.set_footer(text=f"âRequested by {ctx.author}")
                await ctx.send(embed=embed)

    @lower.error
    async def lower_error(self,ctx, error):
        languageserver = await settings.collectionlanguage.find_one({"guild_id":ctx.guild.id})
        if languageserver is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self,ctx))
            await message.add_reaction('đ')
        
        else:
            server_language = languageserver["Language"]
            
            if server_language == "Thai":
                if isinstance(error, commands.MissingRequiredArgument):
                    embed = nextcord.Embed(
                        colour = 0x983925,
                        description = f" â ī¸``{ctx.author}`` ā¸ā¸°ā¸āšā¸­ā¸āšā¸Ēāšā¸ā¸Ŗā¸°āšā¸ĸā¸ā¸Ģā¸Ŗā¸ˇā¸­ā¸āšā¸˛ā¸ā¸ĩāšā¸āšā¸­ā¸ā¸ā¸˛ā¸Ŗā¸ā¸ĩāšā¸ā¸°ā¸āšā¸˛āšā¸āšā¸ā¸ā¸´ā¸Ąāšā¸Ĩāšā¸ ``{settings.COMMAND_PREFIX}lower (message)``"
                    )
                    embed.set_footer(text=f"âRequested by {ctx.author}")

                    message = await ctx.send(embed=embed ) 
                    await message.add_reaction('â ī¸')
            
            if server_language == "English":
                if isinstance(error, commands.MissingRequiredArgument):
                    embed = nextcord.Embed(
                        colour = 0x983925,
                        description = f" â ī¸``{ctx.author}`` need to specify what to make into lowercase ``{settings.COMMAND_PREFIX}lower (message)``"
                    )
                    embed.set_footer(text=f"âRequested by {ctx.author}")

                    message = await ctx.send(embed=embed ) 
                    await message.add_reaction('â ī¸')

    @commands.command()
    async def reverse(self,ctx, *, message):
        languageserver = await settings.collectionlanguage.find_one({"guild_id":ctx.guild.id})
        if languageserver is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self,ctx))
            await message.add_reaction('đ')
        
        else:
            server_language = languageserver["Language"]
            
            if server_language == "Thai":

                reverse = message[::-1]
                embed = nextcord.Embed(
                    colour = 0x00FFFF,
                    title = "REVERSE GENERATOR",
                    description = f"""```
ā¸āšā¸­ā¸ā¸§ā¸˛ā¸Ąā¸ā¸ā¸ā¸´ : {message}
ā¸āšā¸­ā¸ā¸§ā¸˛ā¸Ąā¸ā¸Ĩā¸ąā¸ā¸Ģā¸Ĩā¸ąā¸ : {reverse}```"""
            )

                embed.set_footer(text=f"âRequested by {ctx.author}")
                await ctx.send(embed=embed)
            
            if server_language == "English":

                reverse = message[::-1]
                embed = nextcord.Embed(
                    colour = 0x00FFFF,
                    title = "REVERSE GENERATOR",
                    description = f"""```
Normal text : {message}
Reverse text : {reverse}```"""
            )

                embed.set_footer(text=f"âRequested by {ctx.author}")
                await ctx.send(embed=embed)

    @reverse.error
    async def reverse_error(self,ctx, error):
        languageserver = await settings.collectionlanguage.find_one({"guild_id":ctx.guild.id})
        if languageserver is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self,ctx))
            await message.add_reaction('đ')
        
        else:
            server_language = languageserver["Language"]
            
            if server_language == "Thai":
                if isinstance(error, commands.MissingRequiredArgument):
                    embed = nextcord.Embed(
                        colour = 0x983925,
                        description = f" â ī¸``{ctx.author}`` ā¸ā¸°ā¸āšā¸­ā¸āšā¸Ēāšā¸ā¸Ŗā¸°āšā¸ĸā¸ā¸Ģā¸Ŗā¸ˇā¸­ā¸āšā¸˛ā¸ā¸ĩāšā¸āšā¸­ā¸ā¸ā¸˛ā¸Ŗā¸ā¸ĩāšā¸ā¸°ā¸ā¸Ĩā¸ąā¸ā¸āšā¸˛ā¸ ``{settings.COMMAND_PREFIX}reverse (message)``"
                    )
                    embed.set_footer(text=f"âRequested by {ctx.author}")

                    message = await ctx.send(embed=embed ) 
                    await message.add_reaction('â ī¸')
            
            if server_language == "English":
                if isinstance(error, commands.MissingRequiredArgument):
                    embed = nextcord.Embed(
                        colour = 0x983925,
                        description = f" â ī¸``{ctx.author}`` need to specify what to reverse ``{settings.COMMAND_PREFIX}reverse (message)``"
                    )
                    embed.set_footer(text=f"âRequested by {ctx.author}")

                    message = await ctx.send(embed=embed ) 
                    await message.add_reaction('â ī¸')

    @commands.command()
    async def enbinary(self,ctx, *, text): 
        languageserver = await settings.collectionlanguage.find_one({"guild_id":ctx.guild.id})
        if languageserver is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self,ctx))
            await message.add_reaction('đ')
        
        else:
            server_language = languageserver["Language"]
            
            if server_language == "Thai":
                async with aiohttp.ClientSession() as session:
                    async with session.get(f"https://some-random-api.ml/binary?text={text}") as r:
                        r = await r.json()

                binary = r['binary']

                embed = nextcord.Embed(
                    colour=0x00FFFF,
                    title= "Encode Binary",
                    description = f"""```
ā¸āšā¸˛ā¸ā¸ā¸ā¸´ : {text}
Binary : {binary}```"""
                )
                
                embed.set_footer(text=f"âRequested by {ctx.author}")
                message =await ctx.send(embed=embed)
                await message.add_reaction('đģ')
            
            if server_language == "English":
                async with aiohttp.ClientSession() as session:
                    async with session.get(f"https://some-random-api.ml/binary?text={text}") as r:
                        r = await r.json()

                binary = r['binary']

                embed = nextcord.Embed(
                    colour=0x00FFFF,
                    title= "Encode Binary",
                    description = f"""```
Normal text : {text}
Binary : {binary}```"""
                )
                
                embed.set_footer(text=f"âRequested by {ctx.author}")
                message =await ctx.send(embed=embed)
                await message.add_reaction('đģ')

    @commands.command()
    async def debinary(self,ctx, *,text): 
        languageserver = await settings.collectionlanguage.find_one({"guild_id":ctx.guild.id})
        if languageserver is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self,ctx))
            await message.add_reaction('đ')
        
        else:
            server_language = languageserver["Language"]
            
            if server_language == "Thai":
                async with aiohttp.ClientSession() as session:
                    async with session.get(f"https://some-random-api.ml/binary?decode={text}") as r:
                        r = await r.json()

                binary = r['text']

                embed = nextcord.Embed(
                    colour=0x00FFFF,
                    title= "Encode Binary",
                    description = f"""```
Binary : {text}
Normal text : {binary}```"""
                )
                
                embed.set_footer(text=f"âRequested by {ctx.author}")
                message =await ctx.send(embed=embed)
                await message.add_reaction('đģ')
            
            if server_language == "Thai":
                async with aiohttp.ClientSession() as session:
                    async with session.get(f"https://some-random-api.ml/binary?decode={text}") as r:
                        r = await r.json()

                binary = r['text']

                embed = nextcord.Embed(
                    colour=0x00FFFF,
                    title= "Encode Binary",
                    description = f"""```
Binary : {text}
Normal text : {binary}```"""
                )
                
                embed.set_footer(text=f"âRequested by {ctx.author}")
                message =await ctx.send(embed=embed)
                await message.add_reaction('đģ')

    @commands.command()
    async def length(self,ctx, *, text):
        languageserver = await settings.collectionlanguage.find_one({"guild_id":ctx.guild.id})
        if languageserver is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self,ctx))
            await message.add_reaction('đ')
        
        else:
            server_language = languageserver["Language"]

            num = len(text)
            if server_language == "Thai": 
                embed = nextcord.Embed(
                    colour = 0x00FFFF,
                    title = "LENGTH COUNTER",
                    description = f"""```
ā¸āšā¸­ā¸ā¸§ā¸˛ā¸Ą : {text}
ā¸ā¸§ā¸˛ā¸Ąā¸ĸā¸˛ā¸§ : {num}```"""

                )

                embed.set_footer(text=f"âRequested by {ctx.author}")
                await ctx.send(embed=embed)
            
            if server_language == "English": 
                embed = nextcord.Embed(
                    colour = 0x00FFFF,
                    title = "LENGTH COUNTER",
                    description = f"""```
text : {text}
length : {num}```"""

                )

                embed.set_footer(text=f"âRequested by {ctx.author}")
                await ctx.send(embed=embed)

    @length.error
    async def length_error(self,ctx, error):
        languageserver = await settings.collectionlanguage.find_one({"guild_id":ctx.guild.id})
        if languageserver is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self,ctx))
            await message.add_reaction('đ')
        
        else:
            server_language = languageserver["Language"]

            if server_language == "Thai":
                if isinstance(error, commands.MissingRequiredArgument):
                    embed = nextcord.Embed(
                        colour = 0x983925,
                        description = f" â ī¸``{ctx.author}`` ā¸ā¸°ā¸āšā¸­ā¸āšā¸Ēāšā¸ā¸Ŗā¸°āšā¸ĸā¸ā¸Ģā¸Ŗā¸ˇā¸­ā¸āšā¸˛ā¸ā¸ĩāšā¸āšā¸­ā¸ā¸ā¸˛ā¸Ŗā¸ā¸ĩāšā¸ā¸°ā¸ā¸ąā¸ā¸ā¸ąā¸§ā¸­ā¸ąā¸ā¸Šā¸Ŗ ``{settings.COMMAND_PREFIX}length (text)``"
                    )
                    embed.set_footer(text=f"âRequested by {ctx.author}")

                    message = await ctx.send(embed=embed ) 
                    await message.add_reaction('â ī¸')
            
            if server_language == "English":
                if isinstance(error, commands.MissingRequiredArgument):
                    embed = nextcord.Embed(
                        colour = 0x983925,
                        description = f" â ī¸``{ctx.author}`` need to specify a text ``{settings.COMMAND_PREFIX}length (text)``"
                    )
                    embed.set_footer(text=f"âRequested by {ctx.author}")

                    message = await ctx.send(embed=embed ) 
                    await message.add_reaction('â ī¸')

    @commands.command()
    async def calculator(self,ctx , *,equation):
        languageserver = await settings.collectionlanguage.find_one({"guild_id":ctx.guild.id})
        if languageserver is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self,ctx))
            await message.add_reaction('đ')
        
        else:
            server_language = languageserver["Language"]
            
            if server_language == "Thai":
            
                url = f"https://api.mathjs.org/v4/?expr={equation}"
                async with aiohttp.ClientSession() as session:
                    async with session.get(url) as req:
                        result = BeautifulSoup(await req.text(), "html.parser")

                embed = nextcord.Embed(
                    colour = 0x00FFFF,
                    title = "āšā¸ā¸Ŗā¸ˇāšā¸­ā¸ā¸ā¸´ā¸āšā¸Ĩā¸",
                    description = f"""
    ```
    āšā¸ā¸ā¸ĸāš : {equation}
    ā¸āšā¸˛ā¸ā¸­ā¸ : {result}
    ```""")
                embed.set_footer(text=f"âRequested by {ctx.author}")
                await ctx.send(embed=embed)
            
            if server_language == "English":
            
                url = f"https://api.mathjs.org/v4/?expr={equation}"
                async with aiohttp.ClientSession() as session:
                    async with session.get(url) as req:
                        result = BeautifulSoup(await req.text(), "html.parser")

                embed = nextcord.Embed(
                    colour = 0x00FFFF,
                    title = "Calculator",
                    description = f"""
    ```
    Equation : {equation}
    Answer : {result}
    ```""")
                embed.set_footer(text=f"âRequested by {ctx.author}")
                await ctx.send(embed=embed)

    @calculator.error
    async def calculator_error(self,ctx, error):
        languageserver = await settings.collectionlanguage.find_one({"guild_id":ctx.guild.id})
        if languageserver is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self,ctx))
            await message.add_reaction('đ')
        
        else:
            server_language = languageserver["Language"]
            
            if server_language == "Thai":
                if isinstance(error, commands.MissingRequiredArgument):
                    embed = nextcord.Embed(
                        colour = 0x983925,
                        title = "ā¸Ŗā¸°ā¸ā¸¸ā¸Ēā¸´āšā¸ā¸ā¸ĩāšā¸ā¸°ā¸āšā¸˛ā¸ā¸§ā¸",
                        description = f" â ī¸``{ctx.author}`` ā¸ā¸°ā¸āšā¸­ā¸ā¸Ŗā¸°ā¸ā¸¸āšā¸Ēāšā¸Ēā¸´āšā¸ā¸ā¸ĩāšā¸ā¸°ā¸āšā¸˛ā¸ā¸§ā¸ ``{settings.COMMAND_PREFIX}calculator (equation)``"
                        )
                    embed.set_footer(text=f"âRequested by {ctx.author}")

                    message = await ctx.send(embed=embed ) 
                    await message.add_reaction('â ī¸')
            
            if server_language == "English":
                if isinstance(error, commands.MissingRequiredArgument):
                    embed = nextcord.Embed(
                        colour = 0x983925,
                        title = "Specify an equation",
                        description = f" â ī¸``{ctx.author}`` need to specify a math equation ``{settings.COMMAND_PREFIX}calculator (equation)``"
                        )
                    embed.set_footer(text=f"âRequested by {ctx.author}")

                    message = await ctx.send(embed=embed ) 
                    await message.add_reaction('â ī¸')

def setup(bot: commands.Bot):
    bot.add_cog(General(bot))