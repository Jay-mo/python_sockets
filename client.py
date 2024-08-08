import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)


client_socket.connect(("127.0.0.1", 6543))


client_socket.sendall(b"Hello World. This is a message from John")
client_socket.f
#client_socket.shutdown(socket.SHUT_WR)



data_buffer = []
while True:
    data = client_socket.recv(2048)
    if not data:
        break
    data_buffer.append(data)

print("Received", repr(b''.join(data_buffer)))


client_socket.close()