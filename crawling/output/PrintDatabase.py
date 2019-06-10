# -*- coding:UTF-8 -*-

from crawling.databases.SqlHelper import SqlHelper

class PrintDatabase(object):

    def __init__(self):
        self.sqlHelper = SqlHelper()
        print("1")

    def save(self, map, tableName):
        self.sqlHelper.insertByTable(tableName, map)
        return

