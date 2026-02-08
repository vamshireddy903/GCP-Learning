# Classless Inter Domain Routing (CIDR)

CIDR(Classless Inter Domain Routing) is a method of IP address allocation and routing that allows more efficient use of IP addresses. Unlike traditional class-based addressing, CIDR allocates IP addresses based on a network prefix rather than a fixed class (A, B, or C).

**CIDR Notation:** a.b.c.d/n

n = number of bits in the network prefix.  
Example: 192.168.1.0/24 first 24 bits are the network, and the remaining 8 bits are the host ID.  

# Why CIDR?  
Classful addressing wastes IP addresses:

<img width="866" height="346" alt="image" src="https://github.com/user-attachments/assets/0f9575e4-8856-4311-8cab-621d7e84bef0" />

# Advantages of CIDR  
- **Efficient IP usage:** Minimizes IPv4 address wastage.  
- **Flexible allocation:** Supports networks of any size.  
- **Improved routing:** Aggregates addresses for faster, simpler routing.  
- **Lower administrative overhead:** Easier IP and network management.  

# Disadvantages of CIDR

- Complexity: CIDR is more complex to implement and manage compared to traditional class-based addressing.  
- Compatibility Issues: Some older network devices may not support CIDR.  
- Security Concerns: Implementing security measures like firewall rules and access control lists can be more difficult.

  https://aws.amazon.com/what-is/cidr/
