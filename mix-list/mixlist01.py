#!/usr/bin/env python3
#my_list = [ "192.168.0.5", 5060, "UP" ]
#print("The first item in the list (IP): " + my_list[0] )
#print("The second item in the list (port): " + str(my_list[1]) )
#print("The last item in the list (state): " + my_list[2] )

iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]
print(f"The ip addresses are {iplist[-3]}, and {iplist[-2]}.")
print(f"The network ip in the IP addresses are {iplist[-3][0:6]}.0, and {iplist[-2][0:8]}.0.")


