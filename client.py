from tokenize import Name
from bot_tp4 import MyBot
from discord.ext import commands
import json
import discord 
from argparse import ArgumentParser, Namespace

def parse_arg() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument(
        "-c", "--config", help="Config file", required=True, dest="config"
    )
    return parser.parse_args()

def get_config(config_file: str) -> dict:
    with open (config_file, "r") as f:
        config = json.load(f)
    return config

def main (config:dict) -> bool:
    token = config["TOKEN"]
    prefix = config["prefix"]
    intents = discord.Intents.default()
    intents.presences = True
    intents.members = True
    Bot = MyBot (command_prefix=prefix, intents=intents)
    Bot.run(token)
    pass

if __name__ =="__main__":
    args = parse_arg()
    config = get_config(args.config)
    main(config)
    pass
