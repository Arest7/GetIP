import sys
import socket

def get_ip(target_host):
    try:
        ip = socket.gethostbyname(target_host)
        return ip
    except:
        print("Invalid IP...")

if __name__ == "__main__":
    try:
        read_hostname = sys.argv[1]
        IP = get_ip(read_hostname)
        print("{} ==> {}".format(read_hostname, IP))
    except Exception as e:
        print("Using --> python3 getip.py website_name.com")
