"""Server for multithreaded (asynchronous) chat application."""
import socket
from threading import Thread


HOST = 'localhost'
PORT = 5091
BUF_SIZ = 1024
ADDR = (HOST, PORT)
clients = {}


def broadcast(msg, prefix=""):  # prefix is for name identification.
	"""Broadcasts a message to all the clients."""

	for sock in clients:
		sock.send(bytes(prefix, "utf8") + msg)


def send_user_list():
	clients_info = clients.values()
	msg = ""
	for client_info in clients_info:
		msg += str(client_info) + " "
	return msg


def accept_incoming_connections():
	"""Sets up handling for incoming clients."""
	while True:
		client, client_address = SERVER.accept()
		print(f'{client_address} has connected.')
		client.send(bytes("Hello! Type your name and press Enter!", "utf8"))
		th = Thread(target=handle_client, args=(client, client_address, ))
		th.start()


def handle_client(client, client_address):  # Takes client socket as argument.
	"""Handles a single client connection."""
	name = client.recv(BUF_SIZ).decode("utf8")
	welcome = f"""Welcome {name}! \
1. See the list of users: type "list of users". \
2. Write specific users: type "write to user". \
3. Quit: type "quit".
"""
	client.send(bytes(welcome, "utf8"))
	msg = f'{name} has joined the chat!'
	broadcast(bytes(msg, "utf8"))
	clients[client] = (client_address, name)

	while True:
		msg = client.recv(BUF_SIZ)
		if msg.decode("utf-8") == "quit":
			client.close()
			print(f'{client_address} disconnected')
			del clients[client]
			broadcast(bytes(f'{name} has left the chat.', "utf8"))
			return
		elif msg.decode("utf-8") == "write to user":
			client.send(bytes("Enter username:", "utf-8"))
			user_name = client.recv(BUF_SIZ).decode("utf-8")
			client.send(bytes("Enter message:", "utf-8"))
			message = client.recv(BUF_SIZ).decode("utf-8")
			for sock, info in clients.items():
				if info[1] == user_name:
					sock.send(bytes(f'from {name}:' + message, "utf-8"))
		elif msg.decode("utf-8") == "list of users":
			client.send(bytes(send_user_list(), "utf-8"))
		else:
			broadcast(msg, name + ": ")


SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
	SERVER.listen(5)
	print(f'Server is running on port {PORT}:')
	accept_incoming_connections()
	SERVER.close()
