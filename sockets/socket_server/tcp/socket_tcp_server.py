import socketserver


class EchoTCPHandler(socketserver.BaseRequestHandler):

    def setup(self):
        print("SETUP method before request handling")

    def handle(self):
        data = self.request.recv(1024).strip()
        print('Address: {}'.format(self.client_address[0]))
        print('Data: {}'.format(data.decode()))
        self.request.sendall(data)

    def finish(self):
        print("Closing method afterwards")


if __name__ == '__main__':
    with socketserver.TCPServer(('', 8888), EchoTCPHandler) as server:
        server.serve_forever()
