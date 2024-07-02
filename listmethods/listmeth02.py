#!/usr/bin/env python3
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(proto)
proto.append("dns") # this line will add "dns" to the end of our list
protoa.append("dns") # this line will add "dns" to the end of our list
print(proto)

proto2 = [ 22, 80, 443, 53 ] # a list of common ports

proto.extend(proto2) # pass proto2 as an argument to the extend method
ip_address = ['192.168.1.0', '192.168.1.2', ['127.0.1.1','127.0.1.2']]


print(proto)
protoa.append(proto2) # pass proto2 as an argument to the append method
protoa.append(ip_address)
print(protoa)

ip = ip_address[0]
split_ip = ip.split(".")
print(split_ip)

