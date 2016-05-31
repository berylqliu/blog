# -*- coding: utf-8 -*-
from multiprocessing import cpu_count

workers = cpu_count() * 2 + 1

bind = ['0:8420']
timeout = 600
accesslog = '/var/sankuai/logs/gunicorn_accesslog.log'
errorlog = '/var/sankuai/logs/gunicorn_errorlog.log'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(T)s %(p)s %({Header}i)s '
