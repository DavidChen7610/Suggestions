# -*- coding: utf-8 -*-
__author__ = 'florije'

import logging
from threading import Thread


class SQLEngine(object):
    def __init__(self, DB_PATH):
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s:%(thread)d - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        self.logger = logging.getLogger('SQLLogger')
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(ch)

    def execute(self, SQL, ):
        self.logger.debug(SQL)
        print SQL


class DBWorker(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        db = SQLEngine('')
        db.execute('select 1,2')


if __name__ == '__main__':
    DBWorker('thread 1').start()
    DBWorker('thread 2').start()