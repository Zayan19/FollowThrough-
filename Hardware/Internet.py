import threading
import subprocess

class Internet:
    probing = False
    connected = False

    def __init__(self, probing):
        self.probing = probing
        threading.Timer(2.0, self.test).start()


    # # test if the internet is working by pinging google
    # def test(self, timeout=1.0):
    #     try:
    #         self.connected = subprocess.run(['wget', '-q', '--spider', 'google.com'], timeout=timeout).returncode == 0
    #     except subprocess.TimeoutExpired:
    #         print "nig"
    #
    #     print "[STATUS] Internet: " , self.connected
    #     threading.Timer(2.0, self.test).start()

        # return self.connected
