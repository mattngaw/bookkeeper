import gspread
from discord import app_commands, Interaction
from discord.ext import commands
from discord.ext.commands import Context

class NE(commands.Cog, name="newera"):
    def __init__(self, bot) -> None:
        self.bot = bot

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
        if item not in self.bot.items:
            await context.send(f"Item '{item}' not found in the list.")
            return
        sh = self.bot.loottable.get_worksheet(0)
        row = sh.find(item).row
        cost = sh.cell(row, 5).value
        await context.send(f"The cost of **{item}** is **{cost}**.")
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
        return [] if len(choices) > 25 else choices

async def setup(bot) -> None:
    await bot.add_cog(NE(bot))
