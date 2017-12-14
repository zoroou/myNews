import ConfigParser
import os


def config():
    conf = ConfigParser.ConfigParser()
    path = os.path.realpath(os.getcwd() + '/source/init.conf')
    with open(path, 'r') as conf_file:
        conf.readfp(conf_file)
    return conf

config = config()
