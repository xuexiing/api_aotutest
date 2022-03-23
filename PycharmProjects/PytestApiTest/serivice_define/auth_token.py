#coding=utf-8
#登陆认证

import requests
from common.ApiautoLogging import LoggerForApitest

from common import basic_information, httprequest, data_util
from common.readconfig import ReadConfig

import hashlib

DOMAIN_NAME = ReadConfig().get_userInfo("domain_name")
USER_NAME = ReadConfig().get_userInfo("user_name")
PROJECT_ID = ReadConfig().get_userInfo("project_id")
PASSWORD = ReadConfig().get_userInfo("password")

def get_md5(pwd):
    '''

    :param paassword:
    :return:返回加密值
    '''
    md5 = hashlib.md5()
    md5.update(pwd.encode('utf-8'))
    return md5.hexdigest()

def get_token():
    '''

    :return:
    '''
    iam_endpoint = "https://" + basic_information.sbc_service_endponits['IAM']
    iam_uri = '/v3/auth/tokens'
    url = iam_endpoint + iam_uri
    headers = {"Content-Type": "application/json;charset=utf8"}
    data = {
        "auth": {
            "identity": {
                "methods": [
                    "password"
                ],
                "password": {
                    "user": {
                        "name": USER_NAME,
                        "password": PASSWORD,
                        "domain": {
                            "name": DOMAIN_NAME
                        }
                    }
                }
            },
            "scope": {
                "project": {
                    "id": PROJECT_ID
                }
            }
        }
    }
#    res =httprequest.http_request(url=url, data=data, headers=headers)
    res = requests.post(url=url, json=data, headers=headers, verify=False, timeout=30)
    if res.status_code == 201:
        token = res.headers['X-Subject-Token']
        LoggerForApitest.writeInfoLog('token 获取成功')
        return token
    elif res.status_code in [400,401,403,404,500,503]:
        LoggerForApitest.writeErrorLog('token 获取失败')


if __name__ == '__main__':
    print(get_token())
    print(get_md5("CBU2021Q3&#baseline"))
