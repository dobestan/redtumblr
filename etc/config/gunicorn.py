import multiprocessing
import os


bind = "0.0.0.0:8000"
workers = multiprocessing.cpu_count() * 2 + 1
pythonpath = os.path.join("redtumblr")
