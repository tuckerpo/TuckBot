import discord, logging, json
import praw  # https://praw.readthedocs.io/en/latest/
import pyowm  # https://github.com/csparpa/pyowm
import yelp  # https://github.com/Yelp/yelp-python
import random
import os
from yelpapi import YelpAPI

from discord.ext import commands

yelp_api = YelpAPI(os.environ.get('YELP_KEY'))

# API constants, you shouldn't have to change these.
API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
BUSINESS_PATH = '/v3/businesses/'  # Business ID will come after slash.'

bot = commands.Bot(command_prefix='!')

owm = pyowm.OWM(os.environ.get('OWM_KEY'))

greetings = ['Howdy ', 'Hey ', 'Hello ', 'What\'s up ', 'How\'s it going ']

print("Initializing Discord bot...")


@bot.event
async def on_ready():
    # Print to console when the bot first runs
    print(bot.user.name)
    print(bot.user.id)
    print("Connected.")


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
    datalist.append(
        "Current temperature: " + str(data.get_temperature()['temp'] * (9 / 5) - 459.67).split(".")[0] + " °F")
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
async def food(ctx, yumyums, loc, sort):
    response = yelp_api.search_query(term=str(yumyums), location=str(loc), sort_by=str(sort), limit=5)
    await bot.send_message(ctx.message.channel,
                           "Here is the top location in the " + loc + " area, sorted by " + sort + ".")
    await bot.send_message(ctx.message.channel, response['businesses'][0]['name'])


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


bot.run(os.environ.get('DISCORD_KEY'))
