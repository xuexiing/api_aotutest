#coding=utf-8
import requests
import urllib3
from common.ApiautoLogging import LoggerForApitest

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

LoggerForApitest.setlogger('http_request')

def http_request(token, url, action='get',data=None):
    headers = {"Content-Type": "application/json;charset=utf8", "X-Auth-Token": token}
    retry = 0
    res = None
    while 1:
        try:
            if action == 'post':
                res = requests.post(url=url, headers=headers, json=data, verify=False, timeout=30)
            if action == 'put':
                res = requests.put(url=url,json=data, headers=headers, verify=False,timeout=30)
            if action == 'get':
                res = requests.get(url=url, headers=headers, verify=False, timeout=30)
            if action == 'delete':
                res = requests.delete(url=url, headers=headers, verify=False, timeout=30)
            break
        except urllib3.exceptions.ConnectionError:
            LoggerForApitest.writeErrorLog("http request ConnectionError")
            retry += 1
        except urllib3.exceptions.ConnectTimeoutError:
            LoggerForApitest.writeErrorLog("http request ConnectTimeoutError")
            retry += 1
        except urllib3.exceptions.TimeoutError:
            LoggerForApitest.writeErrorLog("http request TimeoutError")
            retry += 1
        except Exception as exce:
            LoggerForApitest.writeErrorLog("unknow error")
            retry += 1
        if retry >= 3:
            LoggerForApitest.writeErrorLog("retry gather 3, back to False")
            return False
    return res