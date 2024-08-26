import multiprocessing

workers = multiprocessing.cpu_count() * 2 + 1
bind = 'unix:titan.sock'
umask = 0o007
reload = True
timeout = 600
graceful_timeout = 600
max_requests = 1000
max_requests_jitter = 50

#logging
accesslog = '-'
errorlog = '-'
