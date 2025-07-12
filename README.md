# NewEra Bookkeeper

A bookkeeping Discord bot that tracks DKP for NewEra, a Celtic Heroes clan on the Belenus server.

## Features

The bot features Discord-style autocomplete for command arguments where applicable.

```text
Clanny commands:
/attends                                    # Returns the overall attends leaderboard
/attends <class>                            # Returns the per-class attends leaderboard
/attends <toon>                             # Returns the amount of attends a toon has
/kills <toon>                               # Returns the kill counts for a toon
/cost <item>                                # Returns the attends cost of an item
/log <toon> <boss>                          # Records a boss attend for toon

Leader commands:
/handout <toon> <item> <optional-coupon>    # Deducts attends from toon for the item
/refund <toon> <item> <half|full>           # Adds attends to toon for the item
/sub <toon> <amount>                        # Manually deducts attends from toon
/add <toon> <amount>                        # Manually adds attends to toon
```

## How to start

To start the bot you simply need to launch, either your terminal (Linux, Mac & Windows), or your Command Prompt (
Windows).

Before running the bot you will need to install all the requirements with this command:

```sh
python -m pip install -r requirements.txt
```

After that you can start it with

```sh
python bot.py
```

> **Note**: You may need to replace `python` with `py`, `python3`, `python3.11`, etc. depending on what Python versions you have installed on the machine.

## Credit

This bot is built from [kkrypt0nn](https://github.com/kkrypt0nn)'s [Python-Discord-Bot-Template](https://github.com/kkrypt0nn/Python-Discord-Bot-Template).
Credit for most of the code in this repo goes to them.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE.md](LICENSE.md) file for details
