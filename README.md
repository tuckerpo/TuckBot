# TuckBot - generic Discord bot template written in Python 3.6


## Getting Started
1. Clone this codebase to your local machine. You could also fork it, or copy and paste it into your IDE/text editor of choice.
2. Head over to [the Discord developer API suite](https://discordapp.com/developers/docs/intro) and register your app.
3. Mark your app as a bot. This cannot be undone. This will generate the token needed to launch your bot.
4. Paste the generated token into the bot.run('<your_discord_token_here>') method call.
5. Head over to [OpenWeatherMap](https://www.openweathermap.org/api) and register an account. Then, subscribe (it's free) to the 'Current weather data' API.
6. Generate an API key for this API subscription. Add it to the code where prompted.

At this point, you should be able to either click whatever build button you have in your IDE to run your program and it should run, error free, assuming your API keys are valid.

Alternatively one can just run python3 discordBot.py from the CL. Be sure that all the pip dependencies are installed if going the CL route.

### Getting your bot to a server
1. Head back to [the Discord developer API suite](https://discordapp.com/developers/docs/intro) and click on your bot.
2. Click the 'Generate OAuth2 URL' button. Mark all permissions you would like the bot to have. There's no reason not to give the bot all permissions, so go ahead and do so by clicking 'Administrator'. This will also enable adding more functionality to the bot without having to regenerate an OAuth key with new permissions.
3. Take the generated OAuth2 link and paste it into your browser. You may be asked to log in. Do so. You will then be prompted to add your bot to a server. You can only add bots to servers in which you have 'Manage Server' privileges.
4. Your bot should now be a part of your server. You can now run your bot and test your functionality. I recommend making your own temporary server to do this.


### The API calls
1. The included API calls all assume a free account, meaning the APIs are probably rate limited. Be mindful of this when testing your bot.
2. Imports for working with Reddit, Yelp, OpenWeatherMap and Discord are all included, but in my example, only Discord and OpenWeatherMap code is implemented. The rest is left to you.
3. Documentation for each of the provided libraries are linked in the discordBot.py Python file. The code assumes you want API calls to return JSON as opposed to XML or some other parsable format.


#### Further Development
This is a great project for someone who is new to programming, as Python is a dynamically typed language and is rather forgiving. This is also a great exercise in working with APIs and integrating API functionality into an application of your own.
