import socket
from threading import Thread

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(('localhost', 5091))
IS_RUNNING = True
THREADS = []


def listening():
    while True:
        if IS_RUNNING:
            print(c.recv(512).decode("utf-8"))
        else:
            return


def writing():
    while True:
        data = input()
        if data == "quit":
            global IS_RUNNING
            c.send(bytes(data, "utf-8"))
            IS_RUNNING = False
            return
        else:
            c.send(bytes(data, "utf-8"))


listen_thread = Thread(target=listening, )
listen_thread.start()
THREADS.append(listen_thread)
write_thread = Thread(target=writing, )
write_thread.start()
THREADS.append(write_thread)

for thread in THREADS:
    thread.join()

c.close()

# def listen(t):
#     while True:
#         if not IS_RUNNING:
#             return
#         print('listening', t)
#         sleep(2)
#
#
# IS_RUNNING = True
#
# listen_thread = Thread(target=listen, args=(123,))
#
# listen_thread.start()
#
# THREADS = []
#
# THREADS.append(listen_thread)
#
# input('PRESS ANY KEY TO STOP')
#
# IS_RUNNING = False
#
# for thread in THREADS:
#     thread.join()
