from configparser import ConfigParser

def readConfig(section, key):
    config = ConfigParser()
    config.read("/home/yogesh/PycharmProjects/pythonProject1/testdata/config.ini")
    return config.get(section, key)