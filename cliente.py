import socket

HOST = 'localhost'
PORT = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

for i  in range(3)

ecuacion1 = input(int("ingrese valor de"  "para ecuacion1: " ))

s.sendall(''.encode())
data = s.recv(1024)
cadena = data.decode("utf-8")
s.close()
print ('el cliente recibio ', cadena)