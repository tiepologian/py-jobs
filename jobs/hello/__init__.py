'''
Job: hello
Description: This job says hello!
'''

import time

def preload():
    print "Executing some long pre-loading activity..."
    time.sleep(2)
    print "pre-loading finished!"

def run(params):
    return "Hello, World!"
