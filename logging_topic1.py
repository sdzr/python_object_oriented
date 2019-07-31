import logging.config
import yaml
import os
import logging.handlers

#a = logging.handlers.SMTPHandler

path='config'
with open(path) as f:
    config_dict = yaml.full_load(f)
print(config_dict)
logging.config.dictConfig(config_dict)

# 此处的log命令必须以verbose命名,与congig中的log名一致，可以加后缀verbose.example
verbose = logging.getLogger('verbose.example.SomeClass')
audit = logging.getLogger('audit.example.SomeClass')
verbose.info("verbose informations")
audit.info("audit record with before and after")
#print(config_dict)