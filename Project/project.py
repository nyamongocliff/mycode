#!/usr/bin/env python3
# 1. Import necessary modules from Scapy
from scapy.all import IP, TCP, send, sniff, wrpcap, sr1

# 2. Define the destination IP address
dst_ip = "8.8.8.8"  # Example IP address

# 3. Define the source IP address
src_ip = "192.168.1.100"  # Example source IP address

# 4. Define the destination port
dst_port = 80  # HTTP port

# 5. Define the source port
src_port = 12345  # Example source port

# 6. Create an IP packet with custom fields
ip_packet = IP(dst=dst_ip, src=src_ip)

# 7. Create a TCP packet with custom fields
tcp_packet = TCP(dport=dst_port, sport=src_port, flags="S")  # SYN flag set

# 8. Combine the IP and TCP packets
packet = ip_packet / tcp_packet

# 9. Display the packet details
packet.show()

# 10. Send the packet over the network
send(packet)

# 11. Define a function to create and send multiple TCP/IP packets with different payloads
def send_tcp_packets(dst_ip, src_ip, dst_port, src_port, count):
    for i in range(count):
        # Create IP packet
        ip_packet = IP(dst=dst_ip, src=src_ip)
        
        # Create TCP packet with varying source ports and sequence numbers
        tcp_packet = TCP(dport=dst_port, sport=src_port + i, flags="S", seq=i)
        
        # Add a custom payload to the TCP packet
        payload = f"Packet {i} payload"
        
        # Combine IP and TCP packets with the payload
        packet = ip_packet / tcp_packet / payload
        
        # Display packet details
        packet.show()
        
        # Send the packet
        send(packet)

# 12. Call the function to send 5 TCP/IP packets with custom payloads
send_tcp_packets(dst_ip, src_ip, dst_port, src_port, 5)

# 13. Define a packet sniffing function with a filter and custom action
def packet_sniffer(packet):
    # Check if the packet has TCP layer and contains the custom payload
    if packet.haslayer(TCP) and b"Packet" in bytes(packet[TCP].payload):
        print("Sniffed Packet:")
        packet.show()

# 14. Start sniffing for incoming TCP packets on the specified source port
sniff(filter=f"tcp and src port {dst_port}", prn=packet_sniffer, count=5)

# 15. Define a function to capture packets and save them to a PCAP file
def capture_and_save_packets(count, file_name):
    # Capture packets
    packets = sniff(count=count)
    
    # Save captured packets to a PCAP file
    wrpcap(file_name, packets)

# 16. Call the function to capture 10 packets and save them to a file
capture_and_save_packets(10, "captured_packets.pcap")

# 17. Define a function to analyze packets from a PCAP file
def analyze_pcap(file_name):
    # Read packets from a PCAP file
    packets = rdpcap(file_name)
    
    # Display summary of captured packets
    packets.summary()
    
    # Display detailed information for each packet
    for packet in packets:
        packet.show()

# 18. Call the function to analyze packets from the saved PCAP file
analyze_pcap("captured_packets.pcap")


