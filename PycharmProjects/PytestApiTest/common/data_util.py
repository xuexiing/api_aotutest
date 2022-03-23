import yaml
import json
import os
import time
import requests
import configparser
import urllib3
import subprocess
import sys
import re




class Data_Read_Write_util():

    def __init__(self,read_yaml_path='',write_yaml_path=''):
        #self.read_yaml_path = r'C:\Users\Administrator\PycharmProjects\PytestApiTest\data\user.yaml'
        self.read_yaml_path = read_yaml_path
        self.write_yaml_path = write_yaml_path

    def load_yaml(self):
        with open(self.read_yaml_path, 'r', encoding='utf-8') as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
            return data

    def dump_yaml(self,data):

        with open(self.write_yaml_path, 'a+', encoding='utf-8') as file:
            yaml.dump(data, file)

    def clear_yaml(self):

        with open(self.write_yaml_path, 'w', encoding='utf-8') as file:
            file.truncate()

if __name__ == '__main__':
    token = Data_Read_Write_util(read_yaml_path='../data/token/token.yaml').load_yaml()
    print(token)
