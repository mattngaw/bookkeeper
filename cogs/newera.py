import gspread
import random
from discord import app_commands, Interaction, Embed
from discord.ext import commands
from discord.ext.commands import Context

LOOTTABLE_URL = "https://docs.google.com/spreadsheets/d/12E81Rvhvy4UfFA4frtyMXLXXbyXyTGaZqdCtTFAY3Bo/edit?usp=sharing"

class NE(commands.Cog, name="newera"):
    def __init__(self, bot) -> None:
        self.bot = bot

    """
    /loottable
    """
    @commands.hybrid_command(
        name="loottable",
        description="Returns a link to the loot table sheet.",
    )
    async def loottable(self, context: Context) -> None:
        """
        :param context: The application command context.
        """
        e = Embed()
        e.description = f"Loot table can be found [**here**]({LOOTTABLE_URL})."
        await context.send(embed=e)

    """
    /cost <item name>
    """
    @commands.hybrid_command(
        name="cost",
        description="Reports the cost of an item.",
    )
    @app_commands.describe(item="Choose an option")
    async def cost(self, context: Context, item: str) -> None:
        """
        :param context: The application command context.
        :param item: The selected item.
        """
        e = Embed()
        if item not in self.bot.items:
            e.description = f"**{item}** not found on the [list]({LOOTTABLE_URL}). It either does not exist or it is rolled."
        else:
            sh = self.bot.loottable.get_worksheet(0)
            row = sh.find(item).row
            cost = sh.cell(row, 5).value
            pic_url = sh.cell(row, 8).value
            e.description = f"**{item}** costs **{cost}** attends."
            e.set_image(url=pic_url)
        await context.send(embed=e)
    @cost.autocomplete("item")
    async def cost_autocomplete(
        self, interaction: Interaction, current: str
    ) -> list[app_commands.Choice[str]]:
        """
        Autocompletion handler for the 'option' parameter.

        :param interaction: The interaction object.
        :param current: The current input from the user.
        :return: A list of choices matching the user's input.
        """
        choice_items = [app_commands.Choice(name=item, value=item) for item in self.bot.items]
        choices = [choice for choice in choice_items if current.lower() in choice.name.lower()]
        # return [] if len(choices) > 25 else choices
        return random.sample(choices, min(len(choices), 25)) if choices else []

async def setup(bot) -> None:
    await bot.add_cog(NE(bot))
