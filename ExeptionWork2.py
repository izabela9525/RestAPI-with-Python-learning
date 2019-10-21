from configparser import ConfigParser

# Created object of Configparser class
config = ConfigParser()

# Read data from config file, we don't need full path to Config file
# if we have it in the Directory
config.read("./InputFiles/Config.cfg")

print(config.get("Section1", "username"))