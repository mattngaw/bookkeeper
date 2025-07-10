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
        await context.send(f"You selected: {item}")
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
        choices = [
            app_commands.Choice(name="Godly-Bloodfang-Helm-of-Rejuvination", value="Godly-Bloodfang-Helm-of-Rejuvination"),
            app_commands.Choice(name="Imperial-Bloodfang-Helm-of-Rejuvination", value="Imperial-Bloodfang-Helm-of-Rejuvination"),
            app_commands.Choice(name="Royal-Bloodfang-Helm-of-Rejuvination", value="Royal-Bloodfang-Helm-of-Rejuvination"),
            app_commands.Choice(name="Godly-Bloodfang-Helm-of-Prosperity", value="Godly-Bloodfang-Helm-of-Prosperity"),
            app_commands.Choice(name="Imperial-Bloodfang-Helm-of-Prosperity", value="Imperial-Bloodfang-Helm-of-Prosperity"),
            app_commands.Choice(name="Royal-Bloodfang-Helm-of-Prosperity", value="Royal-Bloodfang-Helm-of-Prosperity"),
        ]
        return [choice for choice in choices if current.lower() in choice.name.lower()]

async def setup(bot) -> None:
    await bot.add_cog(NE(bot))
