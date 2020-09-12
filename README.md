### Botty-5000

To run Botty-5000, run the `brains.py` file after installing dependencies. You will need to create 2 files.

* props.json
* chat_responses.json

## props.json
props.json is a file you need to create so Botty-5000 can interact with Discord and Quandl.
Props.json has two possible properties right now

* bot-chat-trigger - When you talk to botty it needs to start with this string
* bot-command-prefix - All commands for Botty must start with this string
* bot-key - Discord bot key that gives Botty-5000 access to your channel
* quandl-key - quandl api key so Botty-5000 can grab quandl prices

##### example
```
{
  "bot-chat-trigger": "Hey Botty",
  "bot-command-prefix": "Botty-",
  "bot-key": "123456789123456",
  "quandl-key": "abcdefghijk"
}
```

## chat_responses.json
Chat responses is a list of json objects each with three properties...

**Name:** currently isn't used for anything besides easy reading of configured triggers.

**Triggers:** A list of phrases that botty can respond too

**Responses:** A list of responses that will be chosen at random when one of the corresponding trigger phrases are said.
##### example
```
  [
    {
        "name": "Shrimp Cars",
        "triggers": ["bring the car around", "bring the car", "the car"],
        "responses": ["https://v.redd.it/ndtjxhs9o7d51/DASH_720.mp4?source=fallback"]
    }
]
```
Using the above configuration we could trigger botty by saying `Hey Botty, bring the car around` or `Hey Botty, the car`
etc.

# Supported Commands
* ping - Botty will say something back in the channel you talk to him in. Using the above props file. `Botty-ping`.
* commands - Botty will dump a nice list of trigger phrases he recognizes. Using the above props file. `Botty-Commands`