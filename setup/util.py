from configparser import ConfigParser
import os

config = ConfigParser()
config.read(os.path.abspath(os.curdir) + "\config.ini")
        
def get_config(section, key):
    return config.get(section, key)
    