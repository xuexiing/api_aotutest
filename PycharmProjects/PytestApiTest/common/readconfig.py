#coding=utf-8

import configparser
import os


class ReadConfig():

    def __init__(self):
        config_path  = os.path.abspath(__file__).split('common')[0]+"configfile/config.ini"
        self.conf = configparser.ConfigParser()
        self.conf.read(config_path,encoding='utf-8')

    def get_userInfo(self,name):
        value = self.conf.get('user_info',name)
        return value

    def get_usersettlogger(self,name):
        value = self.conf.get('logger',name)
        return value
if __name__ == '__main__':
    print(ReadConfig().get_userInfo("domain_name"))
    print(ReadConfig().get_userInfo("user_name"))
    print(ReadConfig().get_userInfo("project_id"))
