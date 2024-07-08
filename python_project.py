
cisco_devices = {
    "Routers": {
        "ISR Series": {
            "Common Errors": {
                "Interface Down": {
                    "Description": "The network interface is currently inactive or has no connectivity.",
                    "Commands": ["show ip interface brief", "show interface"],
                    "Fixes": ["Check physical connections.", "Verify interface configuration.", "Check for hardware issues."],
                    "OSI_Layer": "Layer 1 (Physical) and Layer 2 (Data Link)",
                    "More_Info": "https://www.cisco.com/c/en/us/support/interfaces-modules/index.html"
                },
                "BGP Neighbor Down": {
                    "Description": "A BGP (Border Gateway Protocol) session with a neighbor has gone down.",
                    "Commands": ["show ip bgp summary", "show ip bgp neighbors"],
                    "Fixes": ["Verify BGP configuration.", "Check network connectivity.", "Ensure correct BGP neighbor IP address."],
                    "OSI_Layer": "Layer 3 (Network)",
                    "More_Info": "https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/index.html"
                },
                "No Route to Host": {
                    "Description": "The router is unable to find a valid path to the destination IP address.",
                    "Commands": ["show ip route", "traceroute"],
                    "Fixes": ["Check routing table.", "Verify static routes.", "Check for routing protocol issues."],
                    "OSI_Layer": "Layer 3 (Network)",
                    "More_Info": "https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13730-9.html"
                }
            }
        },
        "ASR Series": {
            "Common Errors": {
                "Memory Allocation Failure": {
                    "Description": "The device is unable to allocate memory for a process, potentially due to resource exhaustion.",
                    "Commands": ["show memory", "show processes memory"],
                    "Fixes": ["Reboot the device.", "Upgrade memory.", "Check for memory leaks in configurations."],
                    "OSI_Layer": "Layer 7 (Application)",
                    "More_Info": "https://www.cisco.com/c/en/us/support/docs/ios-nx-os-software/ios-software-releases-12-2.html"
                },
                "OSPF Neighbor Down": {
                    "Description": "An OSPF (Open Shortest Path First) session with a neighbor has gone down.",
                    "Commands": ["show ip ospf neighbor", "debug ip ospf adj"],
                    "Fixes": ["Check OSPF configurations.", "Ensure network connectivity.", "Verify OSPF authentication settings."],
                    "OSI_Layer": "Layer 3 (Network)",
                    "More_Info": "https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13684-12.html"
                },
                "MTU Exceeded": {
                    "Description": "The packet size exceeds the Maximum Transmission Unit (MTU) size configured on an interface.",
                    "Commands": ["show interface", "ping -l <size>"],
                    "Fixes": ["Adjust MTU size on interfaces.", "Ensure MTU consistency across the network."],
                    "OSI_Layer": "Layer 3 (Network)",
                    "More_Info": "https://www.cisco.com/c/en/us/support/docs/ip/ip-fragmentation-ip-reassembly/25885-pmtud-ip.html"
                }
            }
        }
    },
    "Switches": {
        "Catalyst Series": {
            "Common Errors": {
                "Port Security Violation": {
                    "Description": "A security breach has been detected on a switch port.",
                    "Commands": ["show port-security", "show port-security interface"],
                    "Fixes": ["Check port security settings.", "Investigate unauthorized devices.", "Adjust port security policies."],
                    "OSI_Layer": "Layer 2 (Data Link)",
                    "More_Info": "https://www.cisco.com/c/en/us/support/docs/switches/catalyst-6500-series-switches/12013-53.html"
                },
                "CRC Errors": {
                    "Description": "Cyclic Redundancy Check errors, indicating possible physical layer issues such as bad cables or interference.",
                    "Commands": ["show interfaces", "show interfaces counters errors"],
                    "Fixes": ["Replace faulty cables.", "Check for electromagnetic interference.", "Inspect and replace faulty hardware."],
                    "OSI_Layer": "Layer 1 (Physical)",
                    "More_Info": "https://www.cisco.com/c/en/us/support/docs/lan-switching/ethernet/11661-47.html"
                },
                "Input Errors": {
                    "Description": "Errors detected in incoming frames on an interface, often due to collisions or physical layer issues.",
                    "Commands": ["show interfaces", "show interfaces status"],
                    "Fixes": ["Check for network collisions.", "Verify cable and connector integrity.", "Monitor network traffic."],
                    "OSI_Layer": "Layer 1 (Physical) and Layer 2 (Data Link)",
                    "More_Info": "https://www.cisco.com/c/en/us/support/docs/ios-nx-os-software/ios-software-releases-12-2/11730-ethernet-collisions.html"
                }
            }
        },
        "Nexus Series": {
            "Common Errors": {
                "Spanning Tree Protocol Loop": {
                    "Description": "A loop has been detected in the network by the Spanning Tree Protocol.",
                    "Commands": ["show spanning-tree", "show spanning-tree summary"],
                    "Fixes": ["Check STP configurations.", "Identify and remove redundant links.", "Implement BPDU guard."],
                    "OSI_Layer": "Layer 2 (Data Link)",
                    "More_Info": "https://www.cisco.com/c/en/us/support/docs/lan-switching/spanning-tree-protocol/10553-17.html"
                },
                "Interface Flapping": {
                    "Description": "An interface is going up and down repeatedly, indicating instability.",
                    "Commands": ["show interfaces", "show log"],
                    "Fixes": ["Check physical connections.", "Investigate network configuration changes.", "Replace faulty hardware."],
                    "OSI_Layer": "Layer 1 (Physical) and Layer 2 (Data Link)",
                    "More_Info": "https://www.cisco.com/c/en/us/support/docs/ios-nx-os-software/nx-os-software/200786-Troubleshooting-Interface-Flapping-on-Cis.html"
                },
                "Duplex Mismatch": {
                    "Description": "There is a duplex mismatch between two connected devices, leading to communication issues.",
                    "Commands": ["show interfaces", "show running-config interface"],
                    "Fixes": ["Ensure both ends of the link have matching duplex settings.", "Set interfaces to auto-negotiate."],
                    "OSI_Layer": "Layer 1 (Physical)",
                    "More_Info": "https://www.cisco.com/c/en/us/support/docs/switches/catalyst-2960-x-series-switches/200785-Duplex-Mismatch-Detection-on-2960X.html"
                }
            }
        }
    },
    "Firewalls": {
        "ASA Series": {
            "Common Errors": {
                "ACL Deny": {
                    "Description": "A packet has been denied by an Access Control List (ACL) configured on the device.",
                    "Commands": ["show access-list", "show asp drop"],
                    "Fixes": ["Review ACL configurations.", "Update ACL rules to allow necessary traffic.", "Check for conflicting ACL entries."],
                    "OSI_Layer": "Layer 3 (Network) and Layer 4 (Transport)",
                    "More_Info": "https://www.cisco.com/c/en/us/support/docs/security/asa-5500-x-series-next-generation-firewalls/113600-asa-access-lists.html"
                },
                "NAT Translation Failure": {
                    "Description": "Network Address Translation (NAT) failed to translate an IP address.",
                    "Commands": ["show nat detail", "show xlate"],
                    "Fixes": ["Verify NAT configurations.", "Check NAT rules for conflicts.", "Ensure sufficient NAT resources are available."],
                    "OSI_Layer": "Layer 3 (Network)",
                    "More_Info": "https://www.cisco.com/c/en/us/support/docs/security/asa-5500-x-series-next-generation-firewalls/113609-asa-nat-troubleshoot.html"
                },
                "Authentication Failure": {
                    "Description": "An authentication attempt has failed, often due to incorrect credentials or misconfigurations.",
                    "Commands": ["show aaa-server", "show vpn-sessiondb"],
                    "Fixes": ["Verify user credentials.", "Check AAA server configurations.", "Ensure network connectivity to AAA servers."],
                    "OSI_Layer": "Layer 7 (Application)",
                    "More_Info": "https://www.cisco.com/c/en/us/support/docs/security/asa-5500-x-series-next-generation-firewalls/118079-config-asa-00.html"
                }
            }
        },
        "Firepower Series": {
            "Common Errors": {
                "Configuration Mismatch": {
                    "Description": "There is a mismatch in the configuration settings between devices, causing operational issues.",
                    "Commands": ["show managers", "show config"],
                    "Fixes": ["Synchronize configurations between devices.", "Check for firmware compatibility.", "Update device configurations as needed."],
                    "OSI_Layer": "Layer 7 (Application)",
                    "More_Info": "https://www.cisco.com/c/en/us/support/docs/security/firepower-management-center/213184-troubleshooting-config-sync-issues-fire.html"
                },
                "SNMP Timeout": {
                    "Description": "A Simple Network Management Protocol (SNMP) request timed out.",
                    "Commands": ["show snmp", "debug snmp packets"],
                    "Fixes": ["Verify SNMP configurations.", "Check network connectivity to SNMP server.", "Ensure SNMP server is operational."],
                    "OSI_Layer": "Layer 7 (Application)",
                    "More_Info": "https://www.cisco.com/c/en/us/support/docs/ip/simple-network-management-protocol-snmp/21311-snmp-timeout.html"
                },
                "DHCP Lease Expired": {
                    "Description": "A DHCP client has lost its IP address lease.",
                    "Commands": ["show dhcpd binding", "debug dhcp detail"],
                    "Fixes": ["Check DHCP server configurations.", "Ensure DHCP server is reachable.", "Verify DHCP lease times."],
                    "OSI_Layer": "Layer 3 (Network)",
                    "More_Info": "https://www.cisco.com/c/en/us/support/docs/ip/dynamic-host-configuration-protocol-dhcp/21632-dhcp-troubleshoot.html"
                }
            }
        }
    },
    "Wireless Controllers": {
        "AireOS Series": {
            "Common Errors": {
                "AP Join Failure": {
                    "Description": "An Access Point (AP) is unable to join the wireless controller.",
                    "Commands": ["show ap join stats", "debug capwap events"],
                    "Fixes": ["Check AP configurations.", "Ensure AP is authorized to join the controller.", "Verify network connectivity."],
                    "OSI_Layer": "Layer 2 (Data Link)",
                    "More_Info": "https://www.cisco.com/c/en/us/support/docs/wireless-mobility/wlan/113443-lap-not-join-wlc-ts.html"
                },
                "RADIUS Server Unreachable": {
                    "Description": "The wireless controller cannot reach the RADIUS server for authentication.",
                    "Commands": ["show radius summary", "debug client <MAC>"],
                    "Fixes": ["Verify RADIUS server configurations.", "Check network connectivity to RADIUS server.", "Ensure RADIUS server is operational."],
                    "OSI_Layer": "Layer 7 (Application)",
                    "More_Info": "https://www.cisco.com/c/en/us/support/docs/wireless-mobility/wlan/212545-radius-server-unreachable.html"
                },
                "High Client Retransmissions": {
                    "Description": "A high number of client retransmissions, indicating potential wireless interference or configuration issues.",
                    "Commands": ["show client summary", "debug client <MAC>"],
                    "Fixes": ["Investigate sources of interference.", "Optimize wireless channel settings.", "Check client device configurations."],
                    "OSI_Layer": "Layer 2 (Data Link)",
                    "More_Info": "https://www.cisco.com/c/en/us/support/docs/wireless-mobility/wlan/118624-technote-wlan-00.html"
                }
            }
        },
        "Catalyst 9800 Series": {
            "Common Errors": {
                "WLC Interface Down": {
                    "Description": "The Wireless LAN Controller (WLC) interface is down.",
                    "Commands": ["show interface status", "debug interface"],
                    "Fixes": ["Check physical connections.", "Verify interface configurations.", "Inspect and replace faulty hardware."],
                    "OSI_Layer": "Layer 1 (Physical) and Layer 2 (Data Link)",
                    "More_Info": "https://www.cisco.com/c/en/us/support/docs/wireless-mobility/wireless-lan-controller-software/213945-troubleshooting-wlc-interfaces.html"
                },
                "Rogue AP Detection": {
                    "Description": "A rogue Access Point (AP) has been detected in the network.",
                    "Commands": ["show wids rogue ap summary", "debug rogue ap"],
                    "Fixes": ["Investigate the rogue AP source.", "Implement rogue AP containment policies.", "Update wireless security settings."],
                    "OSI_Layer": "Layer 2 (Data Link)",
                    "More_Info": "https://www.cisco.com/c/en/us/support/docs/wireless-mobility/wlan/214221-detecting-rogue-access-points.html"
                },
                "Channel Utilization High": {
                    "Description": "High channel utilization detected, indicating possible interference or overuse of the wireless channel.",
                    "Commands": ["show advanced 802.11a summary", "debug 802.11 radio"],
                    "Fixes": ["Optimize channel settings.", "Reduce the number of clients on the channel.", "Investigate sources of interference."],
                    "OSI_Layer": "Layer 2 (Data Link)",
                    "More_Info": "https://www.cisco.com/c/en/us/support/docs/wireless-mobility/wlan/213216-high-channel-utilization.html"
                }
            }
        }
    }
}

#Example of accessing the dictionary
for category, devices in cisco_devices.items():
    print(f"Category: {category}")
    for device_type, details in devices.items():
        print(f"  Device Type: {device_type}")
        for error, info in details["Common Errors"].items():
            print(f"    Error: {error}")
            print(f"      Description: {info['Description']}")
            print(f"      Commands: {', '.join(info['Commands'])}")
            print(f"      Fixes: {', '.join(info['Fixes'])}")
            print(f"      OSI_Layer: {info['OSI_Layer']}")
            print(f"      More_Info: {info['More_Info']}")



