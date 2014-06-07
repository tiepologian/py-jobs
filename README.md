py-jobs
=======

A simple Python job manager that uses threads &amp; sockets to execute async jobs

### Usage
First you write job files like this:
```
# Job: reverse
# Description: This job reverses a string

import time

def preload():
    # write code to be executed just once, when the job is loaded
    sleep(1)

def run(params):
    # this is the code that gets executed when you run the job
    return params[::-1]
```

Then you start the job manager:
```
python job-manager.py start
```

And you run jobs using the job-id and passing arguments on the command line:
```
python job-manager.py run 0 "Hello, World!"
```
