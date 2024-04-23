# Uncomment this to pass the first stage
import socket


def main():
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    client_socket, client_address =server_socket.accept() # wait for client
    
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = client_socket.recv(4096).decode()
        if not data:
            # if data is not received break
            break
        output=b"HTTP/1.1 200 OK\r\n\r\n"
        client_socket.sendall(output)
    client_socket.close()  # close the connection
    server_socket.close()
        


if __name__ == "__main__":
    main()
