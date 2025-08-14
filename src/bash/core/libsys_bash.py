import os
from utils.command_parser import CommandParser as CmdParse
from shared.core.lib_conn import LibConn

class LibSysBash(LibConn):
    __cmds = {}
    config = {}

    def init(config, cmds):
        dblog = config["dblog"]
        LibConn.init(
            dblog["host"],
            dblog["user"],
            dblog["pass"],
            dblog["db"]
        )

        LibSysBash.__cmds = cmds
        LibSysBash.config = config

    def run():
        prompt = ""
        while True:
            prompt = input("$ ")
            args = CmdParse.split(prompt)

            if args[0] == "lib":
                if args[1] == "quit":
                    quit()
                cmd = args[1]
                LibSysBash.run_cmd(cmd, CmdParse.parse(args[2:]))
            else:
                os.system(prompt)

    def run_cmd(cmd, params = []):
        try:
            LibSysBash.__cmds[cmd].execute(params)
        except KeyError:
            print(f"lib: `{cmd}` is not a lib command. See 'lib --help'")
    

    
    

