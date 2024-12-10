# example 2 (UDP unix socket) - CRAP, NOT WORKING!
# import os
# import socket
#
# unix_sock_name = 'unix.sock'
# sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
#
# if os.path.exists(unix_sock_name):
#     os.remove(unix_sock_name)
#
# sock.bind(unix_sock_name)
#
# while True:
#     try:
#         result = sock.recv(1024)
#     except KeyboardInterrupt:
#         sock.close()
#         break
#     else:
#         print('Message', result.decode('utf-8'))

import win32pipe, win32file, pywintypes

pipe_name = r'\\.\pipe\my_pipe'

pipe = win32pipe.CreateNamedPipe(
    pipe_name,
    win32pipe.PIPE_ACCESS_DUPLEX,
    win32pipe.PIPE_TYPE_MESSAGE | win32pipe.PIPE_READMODE_MESSAGE | win32pipe.PIPE_WAIT,
    1, 65536, 65536,
    0,
    None)

win32pipe.ConnectNamedPipe(pipe, None)

while True:
    try:
        result, _ = win32file.ReadFile(pipe, 1024)
        print('Message:', result.decode('utf-8'))
    except pywintypes.error as e:
        if e.winerror == 109:  # Broken pipe
            print('Client disconnected')
            break
        else:
            raise
    except KeyboardInterrupt:
        break

win32file.DisconnectNamedPipe(pipe)
win32file.CloseHandle(pipe)
