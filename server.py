import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)

# A server may have more than one interface. Sockets can be bound to a single/multiple interfaces
# 0.0.0.0 binds to all interfaces , 127.0.0.1 bounds to localhost
# using a specific IP address will bound only to that interface.
server_socket.bind(("127.0.0.1", 6543)) 
backlog = 10
server_socket.listen(backlog)


# we accept an established connection from the backlog queue.
# client_address is the remote IP and port of the accepted connection.
client_socket, client_address = server_socket.accept()  



print(type(server_socket))
print(server_socket.fileno())


print(client_address)
print(client_socket.getpeername())
print(client_socket.getsockname())

data_buffer = []

while True:
    data = client_socket.recv(2048)
    if not data:
        break
    data_buffer.append(data)

print(data_buffer)
client_socket.sendall(b"".join(data_buffer))

client_socket.close()