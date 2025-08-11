import sys
from cmds import get_cmd_class
from core.libsys import LibSys

def get_args(args):
    return args if args != [] else sys.argv

if __name__ == "__main__":
    cmd_dict = get_cmd_class()    
    argv = get_args(["config", "-l"])

    cmd = argv[0]
    cmd_li[cmd].execute(argv[1:])
