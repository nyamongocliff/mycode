#! /usr/bin/env python3

#  Import the ipaddress module
import ipaddress
            
#  Define the function to process the user's IP network input
def process_ip_network(user_input):
    try:
        #  Create an IP network object from the user input
        network = ipaddress.ip_network(user_input, strict=False)
        
            #  Print network details
        print(f"Network: {network}")
        print(f"Network address: {network.network_address}")
        print(f"Broadcast address: {network.broadcast_address}")
        print(f"Netmask: {network.netmask}")
        
        #print the range of hosts
        hosts = list(network.hosts()) 
        if len(hosts) > 0:
            first_host = hosts[0]
            last_host = hosts[-1]
            print(f"Usable IP: {first_host} - {last_host}")
        else:
            print(f"Single host: {hosts[0]}")


    except ValueError as e:
        #  Handle exceptions if the input is not a valid IP network
        print(f"Error: {e}")
        

#Get the IP class
def get_ip_class(user_input):
    
    first_octet = int(user_input.split('.')[0])
    if 1 <= first_octet <= 126:
        return 'Class A'
    elif 128 <= first_octet <= 191:
        return 'Class B'
    elif 192 <= first_octet <= 223:
        return 'Class C'
    elif 224 <= first_octet <= 239:
        return 'Class D (Multicast)'
    elif 240 <= first_octet <= 255:
        return 'Class E (Experimental)'
    else:
        return 'Unknown'


    ip_class = get_ip_class(user_input)
    print(f"Class: {ip_class}")
    get_ip_class(user_input)


while True:
    user_input = input("Enter an IP address and network prefix (e.g., '192.168.1.0/24')or 'Exit' to quit: ").strip().lower()   #  Allow user input

    if user_input.lower =="Exit":
        print("Exiting the program.")
        break
    process_ip_network(user_input)

           



    


    
