import discord
from discord.ext import commands
import dotenv
import os
import aiohttp
import random

# 150, 300
TARGET_MIN = 10
TARGET_MAX = 100

ID_SELF = 1089381933710065804
ID_JASON = 857779900869640192
ID_MONKEY = 642484843401183272
ID_CEASE = 743340045628342324

dotenv.load_dotenv()
TOKEN = os.getenv("OLIVIA_TOKEN")
DEEPAI_KEY = os.getenv("DEEPAI_KEY")

class MyBot(commands.Bot):
    def __init__(self, *, intents: discord.Intents = discord.Intents.default()):
        super().__init__(
            intents=intents,
            command_prefix="o!",
            owner_id=ID_CEASE
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

count = 0
target = random.randint(TARGET_MIN, TARGET_MAX)
print(f"Original target set to {target}")

async def get_adj():
    traits = ["mentally ill", "very pretty", "annoying", "flirtatious", "catlike"]
    return f"{traits[random.randint(0, 4)]} and {traits[random.randint(0, 4)]}"

async def generate(prompt):
    prompt = prompt.replace("$DEBUG", "")

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
    result = await generate(f"Say something about yourself, as if you are a {await get_adj()} girl named Olivia.")
    await interaction.followup.send(result)

@bot.event
async def on_message(message: discord.Message):
    global count, target

    is_reply = False
    misspell = None
    query = None
    message_bot_replied_to = None

    if message.reference:
        channel = await bot.fetch_channel(message.reference.channel_id)
        message_user_replied_to = await channel.fetch_message(message.reference.message_id)
        if message_user_replied_to.author.id == ID_SELF:
            is_reply = True
            if message_user_replied_to.reference:
                message_bot_replied_to = await channel.fetch_message(message_user_replied_to.reference.message_id)

    for possible_misspell in ["olvia", "oliva", "oliivia", "olivi", "oliver", "ovilia", "olviia", "olivao"]:
        if possible_misspell in message.content.lower():
            misspell = possible_misspell
            break

    if message.author.id != ID_SELF:
        if message.author.id == ID_MONKEY:
            if random.randint(1, 3) == 3:
                try:
                    await message.add_reaction("\u26a0")
                except:
                    pass

        if f"<@{ID_SELF}>" in message.content:
            await message.channel.typing()
            query = f"Respond as if you are a {await get_adj()} girl named Olivia to the following message: \"{message.content.replace(f'<@{ID_SELF}>', 'Olivia')}\""

        elif "olivia" in message.content.lower():
            await message.channel.typing()
            query = f"Respond as if you are a {await get_adj()} girl named Olivia to the following message: \"{message.content}\""

        elif misspell:
            await message.channel.typing()
            query = f"Paraphrase the following, using expletives and all capitalized: YOU STUPID IDIOT! MY NAME ISN'T FREAKING {misspell.capitalize()} IT'S OLIVIA YOU DUMBASS!"

        elif is_reply:
            await message.channel.typing()
            query = f"Complete the following conversation as a {await get_adj()} girl named Olivia.\n\n"
            if message_bot_replied_to:
                query += f"{message_bot_replied_to.author.name}: {message_bot_replied_to.content}\n"
            query += f"Olivia: {message_user_replied_to.content}\n{message.author.name}: {message.content}\nOlivia: "

        elif message.guild.id == 1015038824549716019:
            count += 1

            if count > target:
                await message.channel.typing()
                count = 0
                target = random.randint(TARGET_MIN, TARGET_MAX)
                print(f"Target reached and funny sent! new target is {target}")
                query = f"Someone named {message.author.name} just sent the following message: \"{message.content}\". Respond as if you are a {await get_adj()} girl named Olivia."

        if query:
            result = await generate(query)
            if "$DEBUG" in message.content:
                result = f"[DEBUG MODE] **Query:** `{query}`" + result
            await message.reply(result)

bot.run(TOKEN)