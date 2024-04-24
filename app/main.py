import socket
import threading

def handle_client(client_socket):
    while True:
        data = client_socket.recv(4096).decode()
        if not data:
            break
        data_list = data.split("\r\n")
        path = data_list[0].split(" ")[1]

        if str(path) == "/":
            client_socket.sendall(b"HTTP/1.1 200 OK\r\n\r\n")
        elif "/echo/" in str(path):
            msg = path.split("/echo/")[-1]
            response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(msg)}\r\n\r\n{msg}"
            client_socket.sendall(response.encode())
        elif str(path) == "/user-agent":
            user_info = data_list[2].split(" ")[-1]
            response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(user_info)}\r\n\r\n{user_info}"
            client_socket.sendall(response.encode())
        else:
            client_socket.sendall(b"HTTP/1.1 404 Not Found\r\n\r\n")
    client_socket.close()

def main():
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)

    while True:
        client_socket, _ = server_socket.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()