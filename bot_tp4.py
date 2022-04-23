from turtle import title
from discord.ext import commands
import os
import argparse
import json
import discord 
from datetime import datetime

from dotenv import load_dotenv
load_dotenv(dotenv_path="config")

import logging
logging.basicConfig (filename="fichier_log.log", filemode='w', encoding="utf-8", level=logging.DEBUG)

class MyBot(commands.Bot):
    
    async def on_ready(self):
        print("Le bot est prêt.")
        time = str(datetime.now())
        f = open("fichier_log.log","a")
        f.write(time + "Le bot est prêt \n")
        f.close()

    async def on_ready2(self):
        print(f"{self.user.display_name} est connecté au serveur.")

    async def on_member_join(member):
        general_channel: discord.TextChannel = commands.Bot.get_channel(958688288930148375)
        await general_channel.send(content=f"Bienvenue sur le serveur {member.display_name} !")

    async def on_message(self,message):
        if message.content.lower() == "ping":
            await message.channel.send("pong", delete_after=5)

        if message.content.lower() == "salut":
            await message.channel.send("Hey, comment ça va ?")
            time = str(datetime.now())
            f = open ("fichier_log.log","a")
            f.write(time + "Vous avez salué le bot")

        if message.content.lower() == "bye":
            await message.channel.send("A la prochaine !")
            time = str(datetime.now())
            f = open ("fichier_log.log","a")
            f.write(time + "Vous avez dit au revoir le bot")

        if message.content.lower() == "musique":
            await message.channel.send("https://www.youtube.com/watch?v=x8VYWazR5mE")
            time = str(datetime.now())
            f = open ("fichier_log.log","a")
            f.write(time + "Vous avez demandé de la bonne musique")

        if message.content.lower() == "film":
            await message.channel.send("https://tiermaker.com/list/movies/films-1576197/2132957")
            time = str(datetime.now())
            f = open ("fichier_log.log","a")
            f.write(time + "Vous avez demandé les meilleurs films proposés")

        if message.content.lower() == "restau":
            await message.channel.send("Kintaro à Opéra, Paris. https://www.tripadvisor.fr/Restaurant_Review-g187147-d793685-Reviews-Kintaro_Ramen-Paris_Ile_de_France.html")
            time = str(datetime.now())
            f = open ("fichier_log.log","a")
            f.write(time + "Vous avez demandé un excellent restaurant japonais")

        if message.content == "!help":
            embed=discord.Embed(title="Commandes du bot")
            embed.add_field(name="salut", value="Hey, comment ça va ?", inline=False)
            embed.add_field(name="bye", value="A la prochaine !", inline=False)
            embed.add_field(name="musique", value="Un link vers une chanson sympathique", inline=False)
            embed.add_field(name="film", value="Un link vers une tier list de très bons films", inline=False)
            embed.add_field(name="restau", value="Un excellent restaurant japonais", inline=False)
            await message.channel.send(embed=embed)

        if message.content.startswith("!del"):
            number = int(message.content.split()[1])
            messages = await message.channel.history(limit=number + 1).flatten()
        
        for each_message in messages:
            await each_message.delete()
    
    
