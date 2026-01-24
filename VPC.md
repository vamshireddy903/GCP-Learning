# What is VPC?

VPC (Virtual Private Cloud) is like a private network in GCP where your resources (VMs, databases, load balancers, etc.) live.

Think of it as a network you control in the cloud — you decide:

- IP ranges  
- Subnets  
- Firewalls  
- Routes

# 2️⃣ Key Components of GCP VPC

**Subnets**

- A smaller network inside the VPC.  
- Each subnet has an IP range.
- Can be regional (spans only one region).

Example:
```
VPC: 10.0.0.0/16
Subnet 1: 10.0.1.0/24
Subnet 2: 10.0.2.0/24
```
**IP Ranges**

- IPv4 only by default (GCP supports IPv6 optionally).  
- Subnets need non-overlapping IP ranges.

**Routes**

- Decide how traffic moves between subnets and outside the VPC.  
- Default routes exist (like internet access if a NAT or gateway is present).  

**Firewall Rules**

- Control who can access which resource.  
- Example: allow HTTP traffic from the internet to a VM.

**Peering / VPN / Interconnect**

- Connect VPCs together or to on-prem networks.

<img width="1113" height="467" alt="image" src="https://github.com/user-attachments/assets/87f2002b-cb6b-4c0b-83b4-b7c8dc953f5d" />

# How networking works in GCP VPC

**🔹 Internet Gateway**

- GCP has an implicit (built-in) Internet Gateway  
- You do NOT create it manually  
- It automatically exists for every VPC

👉 Unlike AWS, there is no Internet Gateway resource in GCP.

**🔹 Route Table**

GCP does have routes, but:

- They are global  
- Automatically created  
- Not tied to subnets

When you create a VPC:

  - Default routes (like 0.0.0.0/0 → Internet Gateway) are auto-added

You only create custom routes if needed.

**What you actually “select” during VPC creation**

When creating a VPC in GCP, you choose:

- Auto mode or Custom mode  
- Subnet IP ranges  
- Firewall rules (allow HTTP/HTTPS/SSH)
  
Internet access and routing are already there by default.
