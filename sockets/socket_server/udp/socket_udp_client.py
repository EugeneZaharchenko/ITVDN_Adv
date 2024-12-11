# example 1 (UDP client socket )
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(b'Test message: We will WIN!', ('127.0.0.1', 8887))
