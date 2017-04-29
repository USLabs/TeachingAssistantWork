try:
    import docker
except Exception as e:
    print "Docker library not found. Please install it. \nHint: pip install docker"

try:
    import requests
except Exception as e:
    print "Requests library not found. Please install it. \nHint: pip install requests"
try:
    import os
except Exception as e:
    print "OS library not found. Please install it. \nHint: pip install os"
try:
    import subprocess
except Exception as e:
    print "Subprocess library not found. Please install it. \nHint: pip install subprocess"
try:
    import unittest
except Exception as e:
    print "Unittest library not found. Please install it. \nHint: pip install unittest"
try:
    import app
except Exception as e:
    print "App module not found. \nHint: Make sure you this script is in the same folder as app.py"



class Util(object):

    marks = 0

    @staticmethod
    def upDocker(arg):
        client = docker.from_env()
        i = client.images.build(path='.', tag='image')
        print i
        if(arg is not null)
            return client.containers.run(image='image', name='test', ports={5000:5000}, detach=True)
        return client.containers.run(image='image', command=[arg], name='test', ports={5000:5000}, detach=True)

    @staticmethod
    def cleanDocker(container):
        client = docker.APIClient(base_url='unix://var/run/docker.sock')
        client.stop(c)
        client.remove_container(c)
        client.remove_image(c)

    @staticmethod
    def threaded_function(arg):
        os.system('python app.py https://github.com/USLabs/assignment1')

class Assignment1Tests(unittest.TestCase):

    def testDockerizable(self):
        m = 0
        c = Util.upDocker()
        r = requests.get('http://localhost:5000/')
        if r.status_code == 200 and r.text.lower().find("hello from dockerized") != -1:
            m = 3
        else:
            m = 0
        Util.marks += m
        Util.cleanDocker(c)
        self.assertTrue(m==3)

    def testDockerizableWithArguement(self):
        m = 0
        c = Util.upDocker('https://github.com/USLabs/assignment1')
        r = requests.get('http://localhost:5000/')
        if r.status_code == 200 and r.text.lower().find("hello from dockerized") != -1:
            m = 1
        Util.marks += m
        Util.cleanDocker(c)
        self.assertTrue(m==1)

    def testRunnableAndWorking(self):
        thread = Thread(target = Util.threaded_function, args = (10, ))
        thread.start()
        sleep(3)
        r = requests.get('http://localhost:5000/v1/dev-config.yml')
        if r.status_code == 200 and r.text.lower().find("message") and r.text.lower().find("hello from dockerized") != -1:
            variable = raw_input('Did you update all files ? (y/n) : ')
            m1 = 0
            m2 = 0
            if variable == "y":
                r2 = requests.get('http://localhost:5000/v1/dev-config.yml')
                if r2.status_code == 200 and r2.text.lower().find("updated") != -1:
                    m1 += 3
                if m1 < 3:
                    r2 = requests.get('http://localhost:5000/v1/dev-config.json')
                    if r2.status_code == 200 and r2.text.lower().find("updated") != -1:
                        m1 += 3
                r3 = requests.get('http://localhost:5000/v1/test-config.yml')
                if r3.status_code == 200 and r3.text.lower().find("updated") != -1:
                    m2 += 3
                if m2 < 3:
                    r3 = requests.get('http://localhost:5000/v1/test-config.json')
                    if r3.status_code == 200 and r3.text.lower().find("updated") != -1:
                        m2 += 3
        server = Process(target=app.run)
        server.terminate()
        print "Server shot down, Hence shut down !"
        Util.marks += (m1 + m2)
        self.assertTrue((m1 + m2)==6)

# ip = client.inspect_container('30cd4a56d975')['NetworkSettings']['Ports']['5000/tcp'][0]['HostIp']
# port = client.inspect_container('30cd4a56d975')['NetworkSettings']['Ports']['5000/tcp'][0]['HostPort']

def main():
    unittest.main()
    print Util.marks

if __name__ == '__main__':
    main()
