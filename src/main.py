import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

class Taybot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    async def on_ready(self):
        print(f"{self.user.name} connected to Discord")
    
    async def setup_hook(self):
        for cmd_group in os.listdir("src/modules"):
            for cmd_name in os.listdir(f"src/modules/{cmd_group}"):
                if os.path.exists(f"src/modules/{cmd_group}/{cmd_name}/cog.py"):
                    await self.load_extension(
                        f"modules.{cmd_group}.{cmd_name}.cog"
                    )

                    await self.tree.sync()

                    print(f"modules.{cmd_group}.{cmd_name}.cog loaded")

def main():
    bot = Taybot(
        command_prefix=' ',
        activity=discord.Streaming(
            name="hentai",
            url="https://www.twitch.tv/e"
        ),
        intents=discord.Intents.all(),
        application_id=892191710468272148
    )

    load_dotenv()
    bot.run(os.getenv("TAYBOT_TOKEN"))

if __name__ == "__main__":
    main()
