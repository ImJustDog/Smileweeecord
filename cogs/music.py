import settings
from discord.ext import commands
from utils.languageembed import languageEmbed
import discord
import wavelink
class Music(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        if not hasattr(bot, 'wavelink'):
            self.bot.wavelink = wavelink.Client(bot=self.bot)

        self.bot.loop.create_task(self.start_nodes())

    async def start_nodes(self):
        await self.bot.wait_until_ready()
        await self.bot.wavelink.initiate_node(host=settings.lavalinkip,
                                              port=settings.lavalinkport,
                                              rest_uri=f"http://{settings.lavalinkip}:{settings.lavalinkport}",
                                              password=settings.lavalinkpass,
                                              identifier=settings.lavalinkindentifier,
                                              region=settings.lavalinkregion)

    @commands.command(name='connect')
    async def connect_(self, ctx, *, channel: discord.VoiceChannel=None):
        if not channel:
            try:
                channel = ctx.author.voice.channel
            except AttributeError:
                raise discord.DiscordException('No channel to join. Please either specify a valid channel or join one.')

        player = self.bot.wavelink.get_player(ctx.guild.id)
        await ctx.send(f'Connecting to **`{channel.name}`**')
        await player.connect(channel.id)
        await ctx.guild.change_voice_state(channel=channel, self_mute=False, self_deaf=True)


    @commands.command()
    async def play(self, ctx, *, query: str):
        tracks = await self.bot.wavelink.get_tracks(f'ytsearch:{query}')

        if not tracks:
            return await ctx.send('Could not find any songs with that query.')

        player = self.bot.wavelink.get_player(ctx.guild.id)
        if not player.is_connected:
            await ctx.invoke(self.connect_)

        await ctx.send(f'Added {str(tracks[0])} to the queue.')
        await player.play(tracks[0])



def setup(bot):
    bot.add_cog(Music(bot))