#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : leimingming_wx405299
# @Time     : 2021/7/15 15:41
# @File     : ApiautoLogging.py
# @Project  : PytestApiTest
import glob
import logging
import os

from common import readconfig


class LoggerForApitest(object):

    LOG_LEVEL = logging.INFO
    LOGGER = logging.getLogger()
    LOGGER_FORMATTER = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
    LOG_FILE_HANDLE = None
    LOG_STREAM_HANDLE = None
    @staticmethod
    def __getUserSetLevel():
        '''
        获取用户设置日志等级
        :return:
        '''
        read = readconfig.ReadConfig()
        return read.get_usersettlogger('log_level')

    @staticmethod
    def __getkeepoldlogflag():
        '''
        选择是否保存旧日志flag
        :return:
        '''
        read = readconfig.ReadConfig()
        return read.get_usersettlogger('keep_old_log')

    @staticmethod
    def __getlogdir():
        '''
        获取日志路径
        :return:
        '''
        log_dir = os.getcwd() + os.sep + "log" + os.sep
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        return log_dir

    @staticmethod
    def __setlogger(casename):
        usersetlevel = LoggerForApitest.__getUserSetLevel()
        if usersetlevel:
            if usersetlevel == 'info':
                LoggerForApitest.LOG_LEVEL = logging.INFO
            elif usersetlevel == 'debug' or usersetlevel == 'trace':
                LoggerForApitest.LOG_LEVEL = logging.DEBUG
            else:
                print("no support log level")
        LoggerForApitest.LOGGER.setLevel(logging.INFO)
        keepoldlogflag = LoggerForApitest.__getkeepoldlogflag()
        if keepoldlogflag:
            if keepoldlogflag == 'no':
                files = glob.glob(LoggerForApitest.__getlogdir() + '*.log')
                if len(files) > 0:
                    for file in files:
                        os.unlink(file)
        loggerfile = LoggerForApitest.__getlogdir() + casename+ ".log"

        LoggerForApitest.LOG_STREAM_HANDLE = logging.StreamHandler()
        LoggerForApitest.LOG_STREAM_HANDLE.setLevel(logging.INFO)
        LoggerForApitest.LOG_STREAM_HANDLE.setFormatter(LoggerForApitest.LOGGER_FORMATTER)

        LoggerForApitest.LOG_FILE_HANDLE = logging.FileHandler(loggerfile,'a',encoding='utf-8')
        LoggerForApitest.LOG_FILE_HANDLE.setLevel(logging.INFO)
        LoggerForApitest.LOG_FILE_HANDLE.setFormatter(LoggerForApitest.LOGGER_FORMATTER)

        LoggerForApitest.LOGGER.addHandler(LoggerForApitest.LOG_FILE_HANDLE)
        LoggerForApitest.LOGGER.addHandler(LoggerForApitest.LOG_STREAM_HANDLE)

    @staticmethod
    def setlogger(casename):
        LoggerForApitest.__setlogger(casename)

    @staticmethod
    def writeDebugLog(msg):
        LoggerForApitest.LOGGER.debug(msg)

    @staticmethod
    def writeInfoLog(msg):
        LoggerForApitest.LOGGER.info(msg)

    @staticmethod
    def writeWarningLog(msg):
        LoggerForApitest.LOGGER.warning(msg)

    @staticmethod
    def writeErrorLog(msg):
        LoggerForApitest.LOGGER.error(msg)

    @staticmethod
    def quitLogger():
        LoggerForApitest.LOGGER.removeHandler(LoggerForApitest.LOG_STREAM_HANDLE)
        LoggerForApitest.LOGGER.removeHandler(LoggerForApitest.LOG_FILE_HANDLE)

if __name__ == '__main__':
    LoggerForApitest.setlogger('vpc')
    LoggerForApitest.writeWarningLog('123')
    LoggerForApitest.writeDebugLog('234')
    LoggerForApitest.writeErrorLog('234')
    LoggerForApitest.writeInfoLog('234')