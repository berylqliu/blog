# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

HOST = '0.0.0.0'
PORT = '8411'

DEBUG = True

#DB config
MYSQL_READ = "mysql://datamap_read:4PBo5zxcGK7bEv@dx-data-mysql-datamap02:5002/datamap?charset=utf8"
MYSQL_WRITE = "mysql://datamap_write:SEtC4Xj3d5aGL9@dx-data-mysql-datamap01:5002/datamap?charset=utf8"
MYSQL_CREATE = "mysql://data_etl:91PhNVUm3qTdGa@dx-data-mysql-datamap01:5002/datamap?charset=utf8"
ECHO_FLAG = False
POOL_RECYCLE = 1200