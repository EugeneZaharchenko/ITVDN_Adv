# udp client
import socket

server_address = ('localhost', 8888)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(server_address)

while True:
    data, address = sock.recvfrom(1024)
    print(f'Received {data.decode()} from {address}')
