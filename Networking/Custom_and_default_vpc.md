When creating a network in GCP, you have two main options:

- Default VPC  
- Custom VPC  

Let’s break them clearly.

# 1️⃣ Default VPC

When you create a new GCP project, Google automatically creates:

     default VPC network

**Characteristics**

- Auto mode network  
- Automatically creates subnets  
- One subnet per region  
- Pre-created firewall rules (SSH, RDP, internal)  
- Egress allowed by default  

**Example:**  
If 20 regions exist → 20 subnets automatically created.

Each subnet has predefined CIDR ranges.

**Good For**

- Testing  
- Learning    
- Quick setup   

**Problems in Production**

- Harder to control IP ranges  
- Less control over subnet design  
- Not recommended for enterprise architecture

**2️⃣ Custom VPC**

When creating a network manually, you choose:

Custom mode

**Characteristics**

- No automatic subnets  
- You manually create subnets  
- Full control over CIDR ranges  
- No unnecessary regions  
- Better segmentation  

**Example:**  
You create:
```
Subnet-1 (Mumbai) → 10.0.1.0/24
Subnet-2 (Singapore) → 10.0.2.0/24
```

Only where needed.

**Used In**

- Production  
- Enterprise  
- Dev / QA / Prod separation  
- Secure architecture

<img width="916" height="468" alt="image" src="https://github.com/user-attachments/assets/b288208f-41b9-490b-8205-ec458bb49038" />
