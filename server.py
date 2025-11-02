# from flask import Flask
import threading
import socket
import requests

HOST = "0.0.0.0"  # Listen on all interfaces
PORT = 5000       # Port number

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

print(f"Server listening on port {PORT}...")

while True:
    conn, addr = s.accept()
    print(f"Connected by {addr}")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(data)  # Echo back
    conn.close()
    # daca primesti recieve de la client ca initiezi conexiunea atunci fa conexiunea la server, altfel conecteaza-te la server
    # Cu alte cuvinte, daca dai call la convo, atunci esti server, daca primesti mesaj, sau conexiunea a fost initiata,
    # atunci conecteaza-te la server
    # Cand aplicatia este pe fundal, odata la 5 secunde da listen sa vezi daca server-ul este deschis, iar daca este trimite notif daca primesti msj

            # sunt server, clientul meu se conecteaza la localhost, iar celalalt client se conecteaza la sv prin adresa publica
            # cel care initiaza conexiunea P2P, sa fie serverul, trebuie sa salvez mesajele dupa ce inchei conexiunea
            # Trebuie sa fac o functie sa se dea autodelete la mesaje
            # Trebuie sa encryptez mesajele, sa le fac semnatura si hash