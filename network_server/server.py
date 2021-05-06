import socket
import sys
import threading
from network_common.wrappers import Request,Response
from network_server.config import Configuration

class MyThread(threading.Thread):
    def __init__(self,client_socket,requestHandler):
        self.client_socket=client_socket
        self.requestHandler=requestHandler
        threading.Thread.__init__(self)
        self.start()
    def run(self):
            data_bytes=b''
            to_receive=1024
            while len(data_bytes)<to_receive:
                bytes_read=self.client_socket.recv(to_receive-len(data_bytes))
                data_bytes+=bytes_read
            request_data_length=int(data_bytes.decode("utf-8").strip())
            data_bytes=b''
            to_receive=request_data_length
            while len(data_bytes)<to_receive:
                bytes_read=self.client_socket.recv(to_receive-len(data_bytes))
                data_bytes+=bytes_read
            request_data=data_bytes.decode("utf-8")
            request=Request.from_json(request_data)
            response=self.requestHandler(request)
            response_data=response.to_json()
            self.client_socket.sendall(bytes(str(len(response_data)).ljust(1024),'utf-8'))
            self.client_socket.sendall(bytes(response_data,'utf-8'))
            self.client_socket.close()


    

class NetworkServer:
    def __init__(self,requestHandler):
        self.server_configuration=Configuration()
        self.requestHandler=requestHandler
        self.server_configuration._obj._validate_values()
        if self.server_configuration._obj.has_exceptions:
            for exception in self.server_configuration._obj.exceptions.values():
                print(exception[1])
            sys.exit() # needs to be converted to code that raises exception

    def start(self):
        server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server_socket.bind(("localhost",self.server_configuration._obj.port))
        server_socket.listen()
        while True:
            print(f"Server is listening on {self.server_configuration._obj.port} ")
            client_socket,socket_name=server_socket.accept()
            t=MyThread(client_socket,self.requestHandler)