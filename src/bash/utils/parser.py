import sys
import os

class ConfigParser:
    def parse_config(file):
        lines = file.readlines()
        config = {}
        namespace = ""
        
        for line in lines:
            line = line[:-1] if line[-1:] == "\n" else line
            equal_pos = line.find('=')

            if line == "" or line[0] == "#":
                continue

            if line[0] == '[' and line[-1:] == ']':
                namespace = line[1:-1]
                config[namespace] = {}

            if (0 < equal_pos < len(line)):
                key = line[:equal_pos]
                val = line[equal_pos + 1:]
                if line[equal_pos + 1] == '"' and line[-1] == '"':
                    val = val[1:-1]
                config[namespace][key] = val
        return config

