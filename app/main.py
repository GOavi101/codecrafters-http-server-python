# Uncomment this to pass the first stage
import socket


def main():
    server_socket = socket.create_server(("localhost", 4221), reuse_port=False)
    client_socket, client_address =server_socket.accept() # wait for client
    
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = client_socket.recv(4096).decode()
        if not data:
            # if data is not received break
            break
        data_list=data.split("\r\n")
        path=data_list[0].split(" ")[1]
        print(str(path))
        if str(path)=="/":
            client_socket.sendall(b"HTTP/1.1 200 OK\r\n\r\n")
        else:
            client_socket.sendall(b"HTTP/1.1 404 Not Found\r\n\r\n")
    client_socket.close()  # close the connection
    server_socket.close()
        


if __name__ == "__main__":
    main()