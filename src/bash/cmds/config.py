from cmds.cmd import *

class Config:
    def execute(argv):
        if argv[0] == "-l":
            Config.print_config()

    def print_config():
        for namespace in LibBash.config:
            attrs = LibBash.config[namespace]
            for key in attrs:
                value = attrs[key]
                print(namespace, '.', key, '=', value, sep = '')
