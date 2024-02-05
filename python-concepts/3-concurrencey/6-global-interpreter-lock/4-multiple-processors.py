"""
This lesson discusses the implementation of the web-service using multiple
processors.

We'll rewrite our service from the previous section to use a
ProcessPoolExecutor to process requests instead of threads. The changes appear
in the widget below.
"""
from threading import Thread
from concurrent.futures import ProcessPoolExecutor

import socket, time, random, sys


def find_nth_prime(nth_prime):
    i = 2
    nth = 0

    while nth != nth_prime:
        if is_prime(i):
            nth += 1
            last_prime = i

        i += 1

    return last_prime


def is_prime(num):
    if num == 2 or num == 3:
        return True

    div = 2

    while div <= num / 2:
        if num % div == 0:
            return False
        div += 1
    return True


class PrimeService():

    def __init__(self, server_port, executor):
        self.server_port = server_port
        self.requests = 0
        self.executor = executor

    def monitor_requests_per_thread(self):

        while 1:
            time.sleep(1)
            print("{0} requests/min".format(self.requests))
            self.requests = 0

    def handle_client(self, client_socket):
        while 1:
            data = client_socket.recv(4096)
            nth_prime = int(data)

            future = self.executor.submit(find_nth_prime, nth_prime)
            prime = future.result()

            client_socket.send(str(prime).encode())
            self.requests += 1

    def run_service(self):
        connection = socket.socket()
        connection.bind(('127.0.0.1', self.server_port))

        # put the socket into listening mode
        connection.listen(5)

        while 1:
            client_socket, addr = connection.accept()
            Thread(target=self.handle_client, args=(client_socket,), daemon=True).start()


def run_simple_client(server_host, server_port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect((server_host, server_port))

    while 1:
        server_socket.send("1".encode())
        server_socket.recv(4096)


def run_long_request(server_host, server_port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect((server_host, server_port))

    while 1:
        server_socket.send("100000".encode())
        server_socket.recv(4096)


if __name__ == "__main__":
    sys.setswitchinterval(1)
    server_port = random.randint(10000, 65000)
    server_host = "127.0.0.1"
    pool = ProcessPoolExecutor()
    server = PrimeService(server_port, pool)

    server_thread = Thread(target=server.run_service, daemon=True)
    server_thread.start()

    monitor_thread = Thread(target=server.monitor_requests_per_thread, daemon=True)
    monitor_thread.start()

    simple_req_thread = Thread(target=run_simple_client, args=(server_host, server_port), daemon=True)
    simple_req_thread.start()

    time.sleep(3)

    Thread(target=run_long_request, args=(server_host, server_port), daemon=True).start()

    time.sleep(10)


"""
Note that the GIL and switch intervals become irrelevant when we move the 
implementation based on multiple processors. Also, note that the total number 
of requests completed per second without the long-running request being 
injected is less than the total number of requests completed when using 
threads or a single thread. The reason is that there's additional overhead 
because of inter-process communication. However, from the output, you can 
verify that the requests completed per second aren't meaningfully impacted 
when the long-running request is received by the server. The long-running 
request is contained to one process on a single processor and the rest of the 
CPUs can be used to serve other requests through the process pool.
"""