import os
from configparser import ConfigParser
from defenition import ROOT

file = os.path.join(ROOT,'resource','config.ini')
config = ConfigParser()
config.read(file)

path = config['PATH']
host = path['localhost']
port = path['port']


