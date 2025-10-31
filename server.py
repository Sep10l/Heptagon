from flask import Flask
import socket

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
server_sock.bind(('0.0.0.0', 12345))
server_sock.listen()
a = 2

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
client_sock.connect(('server_ip_address', 12345))


