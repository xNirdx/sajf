import discord
import socket
import json
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

host = config['NET']['HOST']
port = int(config['NET']['PORT'])


class MessagePacket:
    def __init__(self, message):
        self.message = message

    def construct(self):
        data = {
            "type": "message",
            "author": self.message.author.nick,
            "content": self.message.content
        }

        return json.dumps(data)

    def send(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((host, port))
            sock.sendall(bytes(self.construct(), "utf-8"))


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        mp = MessagePacket(message)
        mp.send()


client = MyClient()
client.run(config['BOT']['TOKEN'])
