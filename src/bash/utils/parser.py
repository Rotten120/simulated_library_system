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
            
            if line == "" or line[0] == "#" or not(0 < equal_pos < len(line)):
                continue
            
            if line[0] == '[' and line[-1:] == ']':
                namespace = line[1:-1]
                config[namespace] = {}
            else:
                config[namespace][line[:pos]] = line[pos + 1:]
        return config

