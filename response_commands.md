## Botty-5000 response commands

When adding a command into a Botty response it must first be surrounded by `{}` characters. Then you build the command
in 3 parts. `<command_prefix>_<command>(<comma seperated arguments>)`


##### yahoo finance get price example
In this example we are expanding our shrimp pricing to get today's high price for the ticker `SHMP`.
```
  [
    {
        "name": "Cant put a price on shrimp",
        "triggers": ["wut da shrimp worth?", "how much should I shell out?"],
        "responses": [":fried_shrimp: NaturalShrimp Inc had a ${yfin_get_price(SHMP)} high today! :fried_shrimp:"]
    }
]
```
Now Botty's response is more realistic and uses the yahoo finance api it will look something like this...
> 🍤 NaturalShrimp Inc had a $0.14 high today! 🍤