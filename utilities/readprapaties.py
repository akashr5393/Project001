

import configparser
import os
config = configparser.RawConfigParser()
config.read(os.path.abspath(".\\configuration\\config.ini"))

class ReadConfig:
    @staticmethod
    def getApplication():
        return config.get('common info', 'baseurl')

    @staticmethod
    def getusername():
        return config.get('common info', 'username')

    @staticmethod
    def getadminpassword():
        return config.get('common info', 'admin_password')
