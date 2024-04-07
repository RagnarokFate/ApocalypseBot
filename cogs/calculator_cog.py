from discord.ext import commands

class CalculatorCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.history = []

    @commands.command(name="calc", aliases=["calculate"], description="Calculate expression")
    async def calculate(self, ctx, *, expression: str):
        try:
            result = eval(expression)
            self.history.append(f"{expression} = {result}")
            await ctx.send(f"Result: {result}")
        except Exception as e:
            await ctx.send(f"Error: {str(e)}")

    @commands.command(name="history", description="Show latest calculations in history")
    async def show_history(self, ctx):
        if not self.history:
            await ctx.send("History is empty.")
        else:
            message = "\n".join(self.history[-5:])
            await ctx.send(f"**History:**\n{message}")

    @commands.command(name="clear", description="Clear history")
    async def clear_history(self, ctx):
        self.history.clear()
        await ctx.send("History cleared.")

def setup(bot):
    bot.add_cog(CalculatorCog(bot))
