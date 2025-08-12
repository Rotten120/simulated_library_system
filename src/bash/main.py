import utils.import_shared as imp
imp.port_shared()

from cmds import get_cmd_class
from core.libsys_bash import LibSysBash
from utils.config_translate import ConfigTranslation

def fetch_config(file_path = "CONFIG"):
    config = open(file_path, 'r')
    config_parsed = ConfigTranslation.parse_config(config)
    config.close()

    return config_parsed

if __name__ == "__main__":
    cmd_dict = get_cmd_class()
    config_parsed = fetch_config()
    
    LibSysBash.init(config_parsed, cmd_dict)
    LibSysBash.run()

