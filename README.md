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

