'''
Job: reverse
Description: This job reverses a string
'''

import time

def preload():
    # simulate some long preloading
    time.sleep(1)

def run(params):
    return params[::-1]
