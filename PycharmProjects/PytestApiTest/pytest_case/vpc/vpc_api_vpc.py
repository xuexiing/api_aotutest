#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : leimingming_wx405299
# @Time     : 2021/8/4 8:30
# @File     : vpc_api_vpc.py
# @Project  : PytestApiTest
import json

import pytest

from get_root_path import get_path
from common import data_util
from common.ApiautoLogging import LoggerForApitest

from serivice_define.vpc import Vpc

LoggerForApitest.setlogger('vpc')

class TestVpcApi:
    # 创建vpc
    @pytest.mark.parametrize('create_vpc', data_util.Data_Read_Write_util(
        read_yaml_path=get_path() + r'\data\vpc\create_vpc.yaml').load_yaml())
    def test_create_vpc_vpc(self, get_project_id, get_token, create_vpc):
        '''
        :desc 框架读取yaml测试用例自动分组读取多测试用例数据，已相应值对于，只需对response，及预期结果进行数据出来即可
        :param getProjectId:
        :param getToken:
        :param create_vpc:
        :return:
        '''
        #读取测试用例
        case_num = len(create_vpc)
        LoggerForApitest.writeInfoLog(case_num)
        url = create_vpc['request']['url'] % get_project_id
        data = create_vpc['request']['data']
        global res
        try:
            #接口精确创建vpc
            res = Vpc().create_vpc(get_token, url, data)
            #接口输出变量
            vpc_id = {'vpc_id': json.loads(res.text)['vpc']['id']}
            #将输出的变量写入extract.yaml
            data_util.Data_Read_Write_util(write_yaml_path='./../../extract.yaml').dump_yaml(vpc_id)
        except:
            pass

        exptvalue_code = create_vpc['validate'][0]['eq']['status_code']
        exptvalue_text = create_vpc['validate'][0]['eq']['message']
        #断言
        assert res.status_code == exptvalue_code
        if res.status_code == 200:
            assert json.loads(res.text)['vpc']['name'] == exptvalue_text
            LoggerForApitest.writeInfoLog("create vpc succuss")
        else:
            assert exptvalue_text in json.loads(res.text)['message']
            LoggerForApitest.writeInfoLog(exptvalue_text)

    # 删除VPC
    @pytest.mark.parametrize('delete_vpc', data_util.Data_Read_Write_util(
        read_yaml_path=get_path() + r'\data\vpc\delete_vpc.yaml').load_yaml())
    def test_delete_vpc_vpc(self, get_project_id, get_token, delete_vpc):
        '''
        :param getProjectId:
        :param getToken:
        :param delete_vpc:
        :return:
        '''
        url = delete_vpc['request']['url'] % (
            get_project_id,
            data_util.Data_Read_Write_util(read_yaml_path='./../../extract.yaml').load_yaml()['vpc_id'])
        res = Vpc().delete_vpc(get_token, url)
        #断言
        assert res.status_code == delete_vpc['validate'][0]['eq']['status_code']
        LoggerForApitest.writeInfoLog("vpc deleted successfull")


if __name__ == '__main__':
    pytest.main(['-v', 's'])
