import multiprocessing


bind = "0.0.0.0:8013"
worker_class = 'gevent'

workers = multiprocessing.cpu_count() * 2 + 1


max_requests = 500
timeout = 3600
