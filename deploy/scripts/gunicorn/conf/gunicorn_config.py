command = 'gunicorn'
bind = '0.0.0.0:8001'
workers = 12
loglevel = 'info'
pythonpath='${INSTALL_DIR}/seqr'
# errorlog = '${INSTALL_DIR}/logs/gunicorn-error.log'
# accesslog = '${INSTALL_DIR}/logs/gunicorn-access.log'
timeout = 120   # seconds (default is 30)
worker_tmp_dir = '${INSTALL_DIR}/gunicorn'
