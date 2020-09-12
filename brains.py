from quandl_commands import execute_quandl_command, quandl_command_pattern
from discord.ext import commands
import json
import random
import re

with open('./props.json') as props_file:
    props = json.load(props_file)

client = commands.Bot(command_prefix=props['bot-command-prefix'])
chat_data = list()
chat_triggers = list()
chat_responses = list()
does_command_exist_pattern = re.compile(r"""\{.*\}""")
command_args_pattern = re.compile(r"""\((.*)\)""")
BOTTY_5000_TRIGGER = props['bot-chat-trigger']


with open('./chat_responses.json') as chat_response_file:
    chat_data = json.load(chat_response_file)

for chat in chat_data:
    chat_triggers.append(chat['triggers'])
    chat_responses.append(chat['responses'])


def message_is_in_trigger(message, listOfPhrases):
    return any(x.lower() in message.content.lower() for x in listOfPhrases)


def process_response_commands(response):
    if does_command_exist_pattern.search(response):
        command = quandl_command_pattern.search(response).group(1)
        args = command_args_pattern.search(command).group(1)
        if 'quandl' in command:
            result = execute_quandl_command(command[:command.index('(')], args.split(','))
            response = re.sub(r"""\{.*\}""", str(result), response)

    return response


@client.event
async def on_ready():
    print("Brains Are Warm")


@client.command()
async def ping(ctx):
    await ctx.send('wassup')


@client.command()
async def commands(ctx):
    response = 'Things :robot:s like to hear from you... \n'
    commands_to_say = '```'
    for trigger_list in chat_triggers:
        for trigger in trigger_list:
            commands_to_say = commands_to_say + trigger + '\n'

    commands_to_say = commands_to_say + '```'
    response = response + commands_to_say + '**Example:** ' + BOTTY_5000_TRIGGER + ', ' + chat_triggers[0][0]
    await ctx.send(response)

#https://store.steampowered.com/app/976730/ this is the store page
#https://store.steampowered.com/api/appdetails?appids=976730 this is the store api
#Fields we care about {name, is_free, controller_support, price_in_cents, price_in_cents_with_discount}
#we should save the app id once its put in

@client.event
async def on_message(message):
    if message.content.lower().startswith(BOTTY_5000_TRIGGER.lower()):
        channel = message.channel
        for idx, triggers in enumerate(chat_triggers):
            if message_is_in_trigger(message, triggers):
                response = random.choice(chat_responses[idx])
                response = process_response_commands(response)
                await channel.send(response)

    await client.process_commands(message)
client.run(props['bot-key'])
