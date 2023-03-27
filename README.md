# olivia-bot
This bot is a bot I made for a server I'm in, to mess with a user known as lestz AKA Olivia. She is okay with it and thinks it's funny, so the purpose isn't to make fun of her or to offend anyone.

### How to activate the bot
There are 5 ways of activating Olivia bot.
- **Randomly** - It will activate randomly every 10-100 messages (if they are sent in her native server) and it will reply to a message. Then, it resets the countdown to a randomly chosen number in that range.
- **/simulate** - This slash command causes it to generate a few sentences about itself.
- **Mentioning** - Mentioning the bot, either with an "@" or by your message containing "olivia" will cause it to reply to you.
- **Replying** - Replying to the bot does a similar thing as mentioning it, but it takes into account its message you replied to and possibly the message it replied to before. This is very WIP and glitchy.
- **Misspelling** - If you misspell its name, it sometimes activates, very angrily calling you out for that.

### How it works
Depending on the input given, Olivia bot queries [DeepAI's Text Generation API](https://deepai.org/machine-learning-model/text-generator) to generate a response, given varying contexts. Most activations generate two random adjectives from a pool of adjectives that describe Olivia, and tell the AI to respond as an \<adjective> girl named Olivia. This is fairly straightforward except when trying to give the AI context, which it struggles with, sometimes producing a script-like fictional response.

### Can I use this bot?
You can invite the bot using [this link](https://discord.com/api/oauth2/authorize?client_id=1089381933710065804&permissions=414531832896&scope=bot%20applications.commands) if you want to try it out, but the server it was made for is private, so I can't provide that invite link. If you want to adapt this bot for your own purposes, feel free to do so, but if you do, you must do it as a fork of this repository and give me credit. Also, please consider starring this repository or following me if you like this bot. It means a lot to me as I don't have much of a following on GitHub.
