import socket
import multiprocessing

BUF_SIZE = 512


def handler(conn, addr):
    conn.send("HTTP/1.1 200 OK\n".encode())
    conn.send("Transfer-Encoding: chunked\n".encode())
    conn.send("\r\n".encode())

    while True:
        data = conn.recv(BUF_SIZE)
        if not data:
            break

        n = len(data)

        conn.send("{0:02x}\r\n".format(n).encode())
        conn.send(data)
        conn.send("\r\n".encode())

        if n < BUF_SIZE:
            break

    conn.send("0\r\n\r\n".encode())
    conn.close()

if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())

    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('', 8000))
    sock.listen(100)

    print("Start listening 8000 port for connections")
    while True:
        conn, addr = sock.accept()

        process = pool.Process(target=handler, args=(conn, addr))
        process.daemon = True
        process.start()
