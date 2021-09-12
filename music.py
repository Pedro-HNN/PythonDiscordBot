import discord
from discord.ext import commands
import youtube_dl

# ydl/ffmpeg config
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options': '-vn'}
YDL_OPTIONS = {'format': 'bestaudio'}
queue = []

class music(commands.Cog):
    def __init__(self, client):
        self.client = client

    # play music
    @commands.command()
    async def play(self, context,*,url=None):
        if url is None:
            return await context.send("You must include a link")
        if context.author.voice is None:
            return await context.send("You are not in a voice channel")
        else:
            voice_channel = context.author.voice.channel
            if context.voice_client is None:
                await voice_channel.connect()
            else:
                await context.voice_client.move_to(voice_channel)

        # TODO: music lists system
        # TODO: play with spotify API and .mp3/.mp4
        # TODO: queue function

        context.voice_client.stop()

        vc = context.voice_client

        try:
            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(url, download=False)
                url2 = info['formats'][0]['url']
                source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
                vc.play(source)
                await context.send("Playing <fazer com que pegue o nome do vídeo e coloque aqui>")
        except:
            await context.voice_client.disconnect()
            return await context.send("You must use a valid URL!")

    # queue
    @commands.command()
    async def _queue(self, context,*,url):
        pass

    # disconnect voice chat
    @commands.command()
    async def disconnect(self, context):
        await context.voice_client.disconnect()

    # pause music
    @commands.command()
    async def pause(self, context):
        await context.voice_client.pause()

    # resume music
    @commands.command()
    async def resume(self, context):
        await context.voice_client.resume()

# setup cog
def setup(client):
    client.add_cog(music(client))
