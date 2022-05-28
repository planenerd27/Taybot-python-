from random import randint

import discord
from discord import Embed, app_commands
from discord.ext import commands

class Shlong(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @app_commands.command(name="shlong", description="shlong size reveal!!")
    @app_commands.describe(member="see this person's shlong size sussy O_O")
    async def shlong(
        self,
        interaction: discord.Interaction,
        member: discord.Member = None
    ):
        await interaction.response.send_message(
            embed=self.__create_embed(interaction, member)
        )
    
    def __create_embed(
        self,
        interaction: discord.Interaction,
        member: discord.Member
    ) -> Embed:
        person: discord.Member = interaction.user
        if member: person = member

        vin_id = 443149017472434197
    
        min_len = 1 if person.id == vin_id else 2
        max_len = 1 if person.id == vin_id else 10

        embed = Embed(
            title=f"Taylor's examination of {person.name}'s shlong",
            description=f"{person.name}'s shlong length\n"
                + self.__gen_shlong(min_len, max_len),
            color=0xe91e63  # magenta
        )

        embed.set_author(
            name=f"{person.name}#{person.discriminator}",
            icon_url=person.avatar.url
        )

        return embed
    
    def __gen_shlong(self, min_len, max_len) -> str:
        return f"8{'=' * randint(min_len, max_len)}D"

async def setup(bot: commands.Bot):
    await bot.add_cog(Shlong(bot))
