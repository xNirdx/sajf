import socket
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

host = config['NET']['HOST']
port = int(config['NET']['PORT'])


