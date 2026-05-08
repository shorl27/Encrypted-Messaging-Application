import socket
import threading


import  rsa

public_key, private_key = rsa.newkeys(1024)
public_partner = None


choice = input("Do you want to host [1] or to connect [2]: ")

if choice == "1":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 9999))  
    server.listen()

    print("Waiting for connection...")
    client, _ = server.accept()
    print("Connected!")

elif choice == "2":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("180.150.27.19", 9999))
    print("Connected to server!")

else:
    exit()


def send_messages(c):
    while True:
        message = input()
        c.send(message.encode())
        print("You:", message)


def receive_messages(c):
    while True:
        message = c.recv(1024).decode()
        print("Partner:", message)



threading.Thread(target=send_messages, args=(client,)).start()
threading.Thread(target=receive_messages, args=(client,)).start()
