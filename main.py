import socket
import multiprocessing

BUF_SIZE = 512


def handler(conn, addr):
    conn.send("HTTP/1.1 200 OK\n")
    conn.send("Transfer-Encoding: chunked\n")
    conn.send("\r\n")

    while True:
        data = conn.recv(BUF_SIZE)
        if not data:
            break

        n = len(data)

        conn.send("{0:02x}\r\n".format(n))
        conn.send(data)
        conn.send("\r\n")

        if n < BUF_SIZE:
            break

    conn.send("0\r\n\r\n")
    conn.close()


if __name__ == '__main__':
    sock = socket.socket()
    sock.bind(('', 8000))
    sock.listen(100)
    print("Start listening 8000 port for connections")

    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())

    while True:
        conn, addr = sock.accept()

        pool.Process(target=handler, args=(conn, addr))
