#!/usr/bin/python

import sys, os, imp, SocketServer, socket

gjobs = []

def main():
    if len(sys.argv) < 2:
	print "No arguments passed to manager!"
	sys.exit(1)
    options = {'start': start, 'stop': stop, 'run': run}
    options[sys.argv[1]]()


def start():
    for j,i in enumerate(getJobs()):
        print("*("+str(j)+") Loading job " + i["name"])
	job = loadJob(i)
	job.preload()
    startTcp()
	

def stop():
    print "Stop called!"

def run():
    # run test 'Hello, World!'
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(sys.argv[2] + " " + sys.argv[3] + "\n", ('localhost', 2000))
    received = sock.recv(1024)
    print received

def getJobs():
    global gjobs
    possiblejobs = os.listdir("./jobs")
    for i in possiblejobs:
        location = os.path.join("./jobs", i)
        if not os.path.isdir(location) or not "__init__" + ".py" in os.listdir(location):
            continue
        info = imp.find_module("__init__", [location])
        gjobs.append({"name": i, "info": info})
    return gjobs

def loadJob(job):
    return imp.load_module("__init__", *job["info"])

class UDPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
	data = self.request[0].strip()
	jobName = data.split(" ")[0]
	params = data.split(" ", 1)[1]
	self.request[1].sendto(loadJob(gjobs[int(jobName)]).run(params) + "\n", self.client_address)

def startTcp():
    print "* Listening on localhost:2000"
    server = SocketServer.UDPServer(('localhost', 2000), UDPHandler)
    server.serve_forever()

if __name__ == "__main__":
    main()
