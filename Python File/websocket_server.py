
import socket
import threading
import time

class SimpleWebSocketServer:
    def __init__(self):
        self.port = 8765
        self.running = False
        
    def start(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.sock.bind(('localhost', self.port))
            self.sock.listen(5)
            self.running = True
            
            print(f"WebSocket server listening on port {self.port}")
            
            while self.running:
                try:
                    client, addr = self.sock.accept()
                    print(f"Connection from {addr}")
                    client.send(b"HTTP/1.1 200 OK\r\n\r\nWebSocket Server Active")
                    client.close()
                except:
                    break
                    
        except Exception as e:
            print(f"WebSocket error: {e}")
        finally:
            if hasattr(self, 'sock'):
                self.sock.close()

if __name__ == "__main__":
    server = SimpleWebSocketServer()
    server.start()
