import time
import socket

def check_connection():
    try:
        start = time.time()
        socket.create_connection(("8.8.8.8", 53), timeout=5)
        end = time.time()
        latency = round((end - start) * 1000, 2)
        return f"Connected! Latency: {latency}ms"
    except:
        return "No internet connection"

print(check_connection())
