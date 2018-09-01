# -*- coding: utf-8 -*-

import socket
from uuid import getnode as get_mac


def Get_Mac_Value():
    mac = get_mac()
    return mac



# Connect to server2 get the device ID and password. the password will change after a service is closed.
def Register_to_Server2():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server2_ip = "127.0.0.1"  # This value have change to the server2 IP.
    server2_port = 30345

    mac_address = Get_Mac_Value()

    s.connect((server2_ip, server2_port))
    s.send(mac_address)

    Device_ID, Device_password = s.recv(1024).split(" ")
    print "The device ID and password is "+ Device_ID + " " + Device_password

    s.close

def main():


if __name__ == "__main__":
    main()
