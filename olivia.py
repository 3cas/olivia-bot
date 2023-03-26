import discord
from discord.ext import commands
import dotenv
import os
import aiohttp
import random

dotenv.load_dotenv()
TOKEN = os.getenv("OLIVIA_TOKEN")
DEEPAI_KEY = os.getenv("DEEPAI_KEY")

class MyBot(commands.Bot):
    def __init__(self, *, intents: discord.Intents = discord.Intents.default()):
        super().__init__(
            intents=intents,
            command_prefix="o!",
            owner_id=743340045628342324
        )

    async def setup_hook(self) -> None:
        async for guild in self.fetch_guilds():
            print(f"Registering commands for {guild}")
            self.tree.copy_global_to(guild=guild)
        await self.tree.sync()

intents = discord.Intents.default()
#intents.members = True
intents.message_content = True

bot = MyBot(intents=intents)

# 150, 300
TARGET_MIN = 10
TARGET_MAX = 100

count = 0
target = random.randint(TARGET_MIN, TARGET_MAX)
print(f"Original target set to {target}")

async def generate(prompt):
    url = "https://api.deepai.org/api/text-generator"
    headers = {"api-key": DEEPAI_KEY}
    data = {"text": (None, prompt)}

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, data=data) as response:
            try:
                result = (await response.json())["output"]
            except KeyError:
                result = await response.text()
    
    return result

@bot.tree.command(name="simulate", description="Roleplays as Olivia C.")
async def simulate(interaction: discord.Interaction):
    await interaction.response.defer()
    result = await generate("Say something about yourself, as if you are a mentally ill girl named Olivia.")
    await interaction.followup.send(result)

@bot.event
async def on_message(message: discord.Message):
    global count, target

    is_reply = False
    the_misspell = None
    result = None

    if message.reference:
        channel = await bot.fetch_channel(message.reference.channel_id)
        reply_to_message = await channel.fetch_message(message.reference.message_id)
        if reply_to_message.author.id == 1089381933710065804:
            is_reply = True

    for misspell in ["olvia", "oliva", "oliivia", "olivi", "oliver", "ovilia"]:
        if misspell in message.content.lower():
            the_misspell = misspell
            break

    if message.author.id != 1089381933710065804:
        if message.author.id == 857779900869640192:
            message.add_reaction("\u26A0")

        if "<@1089381933710065804>" in message.content:
            await message.channel.typing()
            result = await generate(f"Respond as if you are a mentally ill girl named Olivia to the following message: \"{message.content.replace('<@1089381933710065804>', '')}\"")

        elif "olivia" in message.content.lower():
            await message.channel.typing()
            result = await generate(f"Respond as if you are a mentally ill girl named Olivia to the following message: \"{message.content}\"")

        elif the_misspell:
            await message.channel.typing()
            result = await generate(f"Paraphrase the following: YOU STUPID BITCH! MY NAME ISN'T FUCKING {the_misspell} IT'S OLIVIA YOU RETARD!")

        elif is_reply:
            await message.channel.typing()
            result = await generate(f"You are a mentally ill girl named Olivia and you are engaged in conversation. You have just said \"{reply_to_message.content}\", and someone replied with the following message: \"{message.content}\". Create a reply back.")

        elif message.guild.id == 1015038824549716019:
            count += 1

            if count > target:
                await message.channel.typing()
                count = 0
                target = random.randint(TARGET_MIN, TARGET_MAX)
                print(f"Target reached and funny sent! new target is {target}")

                result = await generate(f"Respond as if you are a mentally ill girl named Olivia to the following message: {message.content}")

        if result:
            await message.reply(result)

bot.run(TOKEN)