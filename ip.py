from requests import get
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print(f"Device IP: {s.getsockname()[0]}")
s.close()

ip = get('https://api.ipify.org').text
print(f"Public IP: {ip}")