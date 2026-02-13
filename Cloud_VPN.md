# What is Hybrid Networking?
Hybrid networking is connecting your on-premises infrastructure (your own data centers, office networks) with cloud resources (GCP, AWS, Azure) to create a unified network environment.

**Key Concept:**  
Instead of having completely separate networks, you create a single extended network that spans both:

- Your physical infrastructure (on-prem servers, databases, storage)  
- Cloud infrastructure (VMs, managed services, storage)


**Common Use Cases:**

**Gradual Cloud Migration**

- Keep some workloads on-prem while moving others to cloud  
- Migrate applications step-by-step without disruption


**Data Residency & Compliance**

- Store sensitive data on-premises  
- Process/analyze in the cloud


**Disaster Recovery**

- Primary systems on-prem  
- Backup/DR in the cloud


**Burst to Cloud**

- Normal workloads run on-prem  
- Scale to cloud during peak demand


**Hybrid Networking Solutions:**  
In GCP:

**Cloud VPN**

- VPN tunnel between on-prem and GCP  
- Encrypted over public internet  
- ✅ Easy, cheap  
- ❌ Lower bandwidth, variable latency


**Cloud Interconnect**

**Dedicated Interconnect:** Direct physical connection (10 Gbps or 100 Gbps)   
**Partner Interconnect:** Via service provider  
- ✅ High bandwidth, low latency, reliable  
- ❌ Expensive, complex setup  


**Cloud Router**

- Uses BGP for dynamic routing  
- Works with VPN or Interconnect  
