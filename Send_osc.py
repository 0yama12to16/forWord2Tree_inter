from pythonosc.udp_client import SimpleUDPClient
ip = "127.0.0.1"
port = 12000
  # Create client
# Send message with int, float and string

class Send_osc:
    def __init__(self, msg):
        self.msg = msg
        self.client = SimpleUDPClient(ip, port)

    def send(self):
        self.client.send_message("/comment", self.msg.encode('utf-8'))
        return 
        
