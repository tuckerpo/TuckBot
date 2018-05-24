import discord, logging, json
import praw                         # https://praw.readthedocs.io/en/latest/
import pyowm                        # https://github.com/csparpa/pyowm
import yelp                         # https://github.com/Yelp/yelp-python
import random
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

owm = pyowm.OWM('<your_openweathermap_api_key>')

greetings = ['Howdy ', 'Hey ', 'Hello ', 'What\'s up ', 'How\'s it going ']

print("Initializing Discord bot...")


@bot.event
async def on_ready():
    # Print to console when the bot first runs
    print(bot.user.name)
    print(bot.user.id)
    print("Connected.")


@bot.listen()
async def on_message(ctx, message):
    # Will be called asynchronously whenever a message is sent to the channel in which the bot resides.
    pass


@bot.command(pass_context=True)
async def weather(ctx, loc):
    # Calls upon the openweathermap API. Bot tells you the location the weather data is coming from, the temperature
    # returned as a non-rounded floating point in °F, and the humidity %. This function can be extended in many
    # different ways by looking at the openweathermap API - https://openweathermap.org/current
    # @usage: !weather <city_name> OR !weather <zip_code>,<country_code>
    # examples: !weather london, !weather 14261,us
    obs = owm.weather_at_place(loc)
    data = obs.get_weather()
    datalist = []
    datalist.append("Fetching weather data from " + str(loc))
    datalist.append("Current temperature: " + str(data.get_temperature()['temp'] * (9 / 5) - 459.67) + " °F")
    datalist.append("Current humidity: " + str(data.get_humidity()) + " % ")
    datalist.append(str(data.get_detailed_status()))
    for x in range(len(datalist)):
        await bot.send_message(ctx.message.channel, datalist[x])


@bot.command(pass_context=True)
async def greet(ctx):
    # Sends a random greeting with the !greet command.
    msg = greetings[random.randint(0, len(greetings) - 1)] + str(ctx.message.author) + '!'
    await bot.send_message(ctx.message.channel, msg)


@bot.command(pass_context=True)
async def purge(ctx, num):
    # Will recursively delete all messages you have sent within the last 14 days.
    # If you are the server owner, it will delete all everyone's messages up to the limit you pass in as an argument.
    # @usage: !purge 20 : will delete the last 20 messages in the current channel.
    msgs = []
    number = int(num)
    await bot.send_message(ctx.message.channel, "Deleting " + str(number) + " messages from client side.")
    async for x in bot.logs_from(ctx.message.channel, limit=number):
        msgs.append(x)
    await bot.delete_messages(msgs)


bot.run('<your_discord_bot_key>')
