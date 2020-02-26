import socket

HOST = 'localhost'
PORT = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

s.listen(1)

conn, addr = s.accept()

print(conn, ' conectado por', addr)
while 1:
    data = conn.recv(1024)
    print(type(data))
    cadena = data.decode("utf")
    print("el servidor recibio " + cadena)
    if not data:
        break

    conn.sendall(data)
conn.close()