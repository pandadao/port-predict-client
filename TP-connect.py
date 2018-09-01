# -*- coding: utf-8 -*-
'''
TP-connect include these function:
    1. connect to server 1 and server 2 to get the public IP and port number
    2. After check the connect information and the network state, startup the TP-registered for the TP system
'''
# Welcome to PR this project to improve the reality. Any question can talked with me: cgsh112@gmail.com

import socket
from uuid import getnode as get_mac

'''
This function is communicating with server1 to get the public port and IP.
'''
def Server1_getport():
    #  新增一個TCP連線instance
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server1_ip = "127.0.0.1"
    server1_port = 30333

    s.connect((server1_ip, server1_port))
    s.send("I am client")
    port1_get_from_server1, public_IP_get_from_server1 = s.recv(1024).split(" ")
#    print "Information get from server1 " + port1_get_from_server1
    s.close()
    return port1_get_from_server1, public_IP_get_from_server1


# Get the device mac address.
def Get_Mac_Value():
    mac = get_mac()
    return mac
    

'''
This part is to get port from server2 and send the port get from server1, so that server2 can have two port to predict
the NAT system using port method ( increasing or decreasing or others).
'''
def Server2_getport(port1_get_from_server1, public_IP_get_from_server1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server2_ip = "127.0.0.1"
    server2_port = 30344

    mac_address = Get_Mac_Value()

    #send the information get from server1 about self public IP and first port, and the mac address is to check which the device is.
    send_msg = port1_get_from_server1 + " " + public_IP_get_from_server1 + " " + mac_address
    s.connect((server2_ip, server2_port))
#    s.send(port1_get_from_server1, public_IP_get_from_server1)
    s.send(send_msg)
#    port2_get_from_server2, public_IP_get_from_server2 = s.recv(1024)
    public_IP_get_from_server2, port2_get_from_server2, port1_get_from_server1 = s.recv(1024).split(",")
    print "server2 function get information of public IP: " + public_IP_get_from_server2 + " port2 get from server2: " + port2_get_from_server2 + " port1 get from server1: " + port1_get_from_server1
    s.close



def main():
    port1_get_from_server1, public_IP_get_from_server1 = Server1_getport()
#    print "main information of port and IP: " + port1_get_from_server1 + " " + public_IP_get_from_server1

    print "main information of port: " + port1_get_from_server1 + " and IP is: " + public_IP_get_from_server1
#    Server1_getport()
    Server2_getport(port1_get_from_server1, public_IP_get_from_server1)


if __name__ == "__main__":
    main()
