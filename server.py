import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)

server_socket.bind(("127.0.0.1", 6543))
backlog = 10
server_socket.listen(backlog)

client_socket, client_address = server_socket.accept()



print(type(server_socket))
print(server_socket.fileno())


print(client_address)
print(client_socket.getpeername())
print(client_socket.getsockname())


data = client_socket.recv(2048)

client_socket.send(data)

client_socket.close()