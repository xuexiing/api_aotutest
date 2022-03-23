#coding=utf-8

#vpc服务接口
import json
import random

import requests
from common import basic_information
from common import httprequest

result = {}

class Vpc(object):

    def __init__(self):
        self.vpc_endpoint ="https://" + basic_information.sbc_service_endponits['vpc']

    #创建VPC
    def create_vpc(self,token,url,data):
        url = self.vpc_endpoint + url
        res = httprequest.http_request(token, url, action='post', data=data)
        return res


    #查询VPC详情
    def query_vpc_detail(self,token,url):
        url = self.vpc_endpoint + url
        res = httprequest.http_request(token, url, action='get')
        return res



    #查询VPC列表
    def qyery_vpc_list(self,token,url):
        url = self.vpc_endpoint + url
        res = httprequest.http_request(token, url, action='get')
        return res


    #删除VPC
    def delete_vpc(self,token,url):
        url = self.vpc_endpoint + url
        res = httprequest.http_request(token, url, action='delete')
        return res
