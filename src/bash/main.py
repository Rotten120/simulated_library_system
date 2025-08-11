import utils.import_shared as imp
imp.port_shared()

from cmds import get_cmd_class
from core.libsys_bash import LibSysBash
from utils.parser import ConfigParser

if __name__ == "__main__":
    cmd_dict = get_cmd_class()
    config = open("CONFIG", 'r')
    config_parsed = ConfigParser.parse_config(config)
    LibSysBash.init(config_parsed, cmd_dict)
    LibSysBash.run()

